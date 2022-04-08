#######    Code example for : Test QA Sanity (Automation)       #########
#########################################################################

import os
from slash import g
from slash_step import STEP

from Scripts import Config, log

from tests.QA.common_functions.agent import get_not_running_processes,\
    run_application, check_mgmt_config_reached_agent, \
    is_application_seen_in_management
from tests.QA.common_functions.threats import run_test_threat_and_search_management
from tests.QA.functionality.agent.black_and_white_list.hashes_tests import blacklist_test, whitelist_test
from tests.QA.functionality.agent.mitigations.mitigation_tests_utils import mitigate_and_unquarantine_test
from tests.QA.functionality.agent.uninstall.uninstall_tests_utils import offline_uninstall_with_key_test
from tests.QA.common_functions.management import change_general_learning_mode, mitigate_threat, \
    check_threat_mitigation_status, check_agent_details_in_management, \
    change_management_mitigation_policy, check_threat_mitigation_report, \
    get_threat_id_by_name


def win32_run_threat_after_upgrade(os_handle, threat_name='sneezingpanda2006.exe'):
    """
    :param os_handle:
    :param threat_name:
    :return: there is a special test threat to be run after winagent upgrade
    we upload the test threat to the agent machine, run it and expect to find the threat in the management
    """
    with STEP('killing all running processes named {}'.format(threat_name)):
        # kill all threat processes to make sure none exist before sanity test
        os_handle.run('taskkill /f /im {}'.format(threat_name), verify_rc=False)

    with STEP('Uploading threat file to agent machine'):
        remote_file = 'c:\\temp\\' + threat_name
        threat_script = os.path.join(Config.automation_root_dir, 'tests', 'windows', 'assets', threat_name)
        os_handle.upload_local_file(threat_script, remote_file)

    with STEP('Run threat and expect to find it in the management'):
        init_threats = len(g.manager.get_threats(display_name=threat_name, agent=g.agent_id))
        os_handle.run('explorer.exe ' + remote_file, verify_rc=False, shell=False)
        threat_detected = g.manager.expect_threat(os_handle=os_handle, init_threats=init_threats,
                                                                   display_name=threat_name, agent=g.agent_id)

        assert threat_detected


def sanity_test(agent_machine, upgrade=False):
    """
    :param agent_machine:
    :param upgrade: True / False, relevant only for windows agent
    if the agent is after upgrade, its params are not patched so we need to run a different threat
    :return: runs all the functionality for agent sanity test:
    - checks that agent is up and that all of the agent processes are running.
    - checks agent device details in the management
    - runs a threat
    - sends quarantine command to the threat
    - checks blacklist
    - checks whitelist
    - checks that applications reach the management
    - checks that agent cpu and memory are normal
    - checks that there are no crash dumps on the machine
    """
    os_handle = agent_machine.os_handle

    if not upgrade:
        upgrade = Config.is_release

    with STEP('check agent services'):
        os_handle.check_agent()

    with STEP('check agent status and processes'):
        assert not get_not_running_processes(os_handle), 'AgentProcessesNotRunning'

    with STEP("Check agent's device details in the management"):
        agent_details = check_agent_details_in_management(os_handle)
        assert agent_details, 'agent details in the management are incorrect'

    with STEP('Setting management learning mode off and mitigation policy to Alert'):
        change_management_mitigation_policy('none')
        change_general_learning_mode()
        check_mgmt_config_reached_agent(os_handle, mitigation_policy='none', learning_mode=False)

    with STEP('Running threat and mitigating it'):
        mitigation = 'quarantine'

        if os_handle.platform == 'win32' and upgrade:
            win32_run_threat_after_upgrade(os_handle)

        else:
            threat_detected, investigate_str, threat_path, threat_pid = run_test_threat_and_search_management(os_handle, g.agent_id)
            assert threat_detected, investigate_str
            threat_name = os_handle.os.path.basename(threat_path)

            threat_id, mitigation_issues = mitigate_threat(os_handle, threat_name, g.agent_id, command=mitigation,
                                                           threat_pid=threat_pid)
            assert not mitigation_issues, 'mitigation failed: {}'.format(', '.join(mitigation_issues))

            mitigation_status = check_threat_mitigation_status(g.agent_id, threat_name, mitigation, threat_id=threat_id)
            assert mitigation_status, 'Unexpected_mitigation_status'

            mitigation_report_issues = check_threat_mitigation_report('quarantine', threat_id=threat_id)
            assert not mitigation_report_issues, ', '.join(mitigation_report_issues)

    with STEP('checking automatic quarantine and unquarantine'):
        mitigate_and_unquarantine_test(agent_machine, 'automatic', mitigation='quarantine')

    if os_handle.platform == 'darwin':
        # this is here because osx's deception-test creates files in this path which need to be deleted afterwards
        path = '/Library/LaunchDaemons/*'
        log.debug(os_handle.modules.glob.glob(path))

    with STEP('Checking blacklist'):
        threat_name = os_handle.os.path.basename(os_handle.valid_file())

        # Linux doesn't block blacklist threats, it performs the policy on them.
        # Change policy to quarantine for linux agents
        change_management_mitigation_policy('quarantine')
        # no need for sleep here. We have it in the blacklist test, when we remove the hash from the black list

        blacklist_test(agent_machine.os_handle)

        if os_handle.platform == 'linux2':  # for linux, the threat would be quarantined and have a mitigation report
            threat_id = get_threat_id_by_name(threat_name, g.agent_id)
            mitigation_report_issues = check_threat_mitigation_report('quarantine', threat_id=threat_id)
            assert not mitigation_report_issues, ', '.join(mitigation_report_issues)

    # sneezingpanda2006.exe is run from rpyc won't be detected after upgrade, so we're skipping this test
    if not upgrade:
        with STEP('Checking whitelist'):
            whitelist_test(agent_machine.os_handle)

    with STEP('Checking valid application is seen in the management'):
        # The current Linux agent doesn't send any applications
        if os_handle.platform != 'linux2':
            with STEP('Open application'):
                app_name = run_application(os_handle)

            app_data = is_application_seen_in_management(app_name=app_name, agent_id=g.agent_id)
            assert app_data, 'application {} was not found in the management'.format(app_name)


def full_sanity_test(agent_machine, upgrade=False):
    """
    Calls sanity test, to run all the functionality.
    Then checks agent crash dumps, agent statistics and lost events
    :param agent_machine:
    :param upgrade: True / False, relevant only for windows agent
    if the agent is after upgrade, its params are not patched so we need to run a different threat
    :return:
    """
    with STEP('Checking agent functionality'):
        sanity_test(agent_machine, upgrade=upgrade)

    with STEP('Uninstalling agent'):
        offline_uninstall_with_key_test(agent_machine)

    assert not g.issues, 'issues found after the test: {0}'.format([x for x in g.issues])


def test_qa_sanity(agent_machine):
    full_sanity_test(agent_machine)



