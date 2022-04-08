from time import sleep, time

import slash
from slash import g
from slash_step import STEP

from Scripts.Issue import report_issue
from tests import platforms
from tests.QA.common_functions.agent import is_strings_in_agent_log
from tests.QA.common_functions.common import get_os_family_from_platform, ActivitiesWrap
from tests.QA.common_functions.management import change_management_options, validate_created_asset_at_mgmt_and_agent, \
    wait_for_asset, get_default_policy_id, change_rebootless_settings


def file_type_exclusion_changes_test(agent_machine, list_id, list_name):
    change_rebootless_settings()
    os_handle = agent_machine.os_handle
    agent_machine.machine.bringup_os(return_os_handle=True, reboot=True)
    folder_to_exclude = os_handle.TEMP_DIR_PATH
    platform = get_os_family_from_platform(os_handle)

    with STEP('File Type (Windows only)'):

        with STEP("Add a new exclusion (File) with temp folder for created list"):
            file_type = 'exe'
            exclusion = g.manager.create_file_type_exclusion(file_type, description=file_type,
                                                             exclusion_list_name=list_name, os_family=platform)
            file_type_id = exclusion[0].get('id')
            with STEP("Validate asset added to mgmt"):
                exclusions = g.manager.get_file_type_exclusion_list(exclusion_list_name=list_name)
                assert exclusions[list_id][0].get('id') == file_type_id, "Created asset doesn't appears in mgmt"

            with STEP('Validate created asset in mgmt and agent'):
                wait_for_asset()
                validate_created_asset_at_mgmt_and_agent(os_handle, file_type)

    with STEP('Exclusion - File path'):

        with STEP('Upload and run threat NOT from exclusion folder'):
            timestamp = time()
            sleep(3)
            init_threats = len(g.manager.get_threats(agent=g.agent_id))
            os_handle.create_and_execute_threat(threat_type='default')

        with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
            if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'ExtensionExcluded',
                                                       os_handle.threat_files.get('default')], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP("Verify mgmt didn't get threat"):
            threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id)
            assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                folder_to_exclude)

        with STEP('Verify the "threat" has not been added to the activity'):
            error_msg = 'There is activity log saying that mgmt got threat'
            assert not ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                   timestamp), error_msg

    with STEP('Delete exclusion'):
        assert g.manager.delete_all_file_type_exclusions(), 'There are not deleted file_type exclusions'


@slash.tag('no_checks_after_test')
@slash.requires(platforms(['windows']))
def test_file_type_exclusion_changes(agent_machine):
    list_name = 'test_list'
    list_id = None
    change_management_options(auto_mitigation_action='mitigation.quarantineThreat', mitigation_mode='protect',
                              mitigation_mode_suspicious='detect', agent_notification=True)

    with STEP('Create new exclusion list and connect it to default policy'):
        default_policy_id = g.manager.get_policies()[0]['id']
        g.manager.create_exclusion_list(name=list_name, policies=[default_policy_id])

        with STEP('Validate exclusion list created in mgmt'):
            exclusion_lists = g.manager.get_list_of_exclusion_lists()
            is_list_created = False
            for exclusion_list in exclusion_lists:
                if exclusion_list.get('name') == list_name:
                    is_list_created = True
                    list_id = exclusion_list.get('id')
            assert is_list_created, "List {} doesn't appears in mgmt".format(list_name)

    with STEP('Update policy with created Exclusion_list'):
        g.manager.update_policy(get_default_policy_id(), exclusion_list_id=list_id)

    with STEP('Running test with created exclusion_list {}'.format(list_id)):
        file_type_exclusion_changes_test(agent_machine, list_id, list_name)

    with STEP('Delete created exlusion list'):
        g.manager.delete_exclusion_list(list_id)
        with STEP('Validate exclusion list was deleted'):
            is_found = False
            excl_lists = g.manager.get_list_of_exclusion_lists()
            for exc_list in excl_lists:
                if exc_list['id'] == list_id:
                    is_found = True
            assert not is_found, 'Exclusion list was not deleted from mgmt'
        wait_for_asset()

    with STEP('Running test with global exclusion list'):
        list_id = g.manager.get_list_of_exclusion_lists()[0].get('id')
        file_type_exclusion_changes_test(agent_machine, list_id, 'Global')
