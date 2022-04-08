import os
from time import sleep, time

import slash
from psutil import NoSuchProcess
from slash import g
from slash_step import STEP

from Scripts import Config
from Scripts import log
from Scripts.Issue import report_issue
from Utils.Timeout import Timeout
from tests.QA.common_functions.agent import is_asset_file_in_agent, is_hash_in_agent_asset_file, is_strings_in_agent_log
from tests.QA.common_functions.common import get_os_family_from_platform, ActivitiesWrap
from tests.QA.common_functions.management import wait_for_asset, get_latest_asset_file_path, \
    is_hash_in_mgmt_asset_file, change_management_options, change_rebootless_settings

BLACK_HASH = '54f638fa6bdecedaf62770abb015fde6c2e0d6bc'  # hash of npp.exe
WHITE_HASH = '6aa1f51802ea8884cb7c55c23c2444ab27068c63'  # Hash of sneezingpanda2006.exe


@slash.tag('no_checks_after_test')
def test_hashes_changes(agent_machine):
    change_rebootless_settings()
    agent_machine.machine.bringup_os(return_os_handle=True, reboot=True)

    mitigation_statuses = {0: 'mitigated', 1: 'active', 2: 'blocked', 3: 'suspicious'}
    os_handle = agent_machine.os_handle
    platform = get_os_family_from_platform(os_handle)

    with STEP('Prepare step: Set mgmt configuration'):
        change_management_options(auto_mitigation_action='mitigation.none', mitigation_mode='detect',
                                  mitigation_mode_suspicious='detect')

    with STEP('Add black\white hashes'):

        with STEP('Add white hash to mgmt'):
            with STEP('Add white hash {} to mgmt'.format(WHITE_HASH)):
                g.manager.add_hash(WHITE_HASH, platform, is_black=False)
            with STEP('Validate hash added to mgmt'):
                sleep(30)
                hashes_list = g.manager.get_hashes(is_black='false')
                is_hash_found = False
                for hash in hashes_list:
                    if hash.get('id') == WHITE_HASH:
                        is_hash_found = True
                assert is_hash_found, 'Hash {} not found on mgmt'.format(WHITE_HASH)
                asset_id = get_latest_asset_file_path(g.manager.os_handle)
                assert is_hash_in_mgmt_asset_file(g.manager.os_handle, WHITE_HASH, asset_id), 'hash {hash} not found in mgmt asset file {asset}'. \
                    format(hash=WHITE_HASH, asset=asset_id)

            with STEP('Validate agent got asset'):
                wait_for_asset()
                if not is_asset_file_in_agent(os_handle, asset_id):
                    report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
                else:
                    if not is_hash_in_agent_asset_file(os_handle, WHITE_HASH, asset_id):
                        report_issue(g.issues, 'Hash {hsh} not found in agent asset file {asst}'.format(hsh=WHITE_HASH, asst=asset_id), False)

        with STEP('Add black hash to mgmt'):
            with STEP('Add black hash {} to mgmt'.format(BLACK_HASH)):
                g.manager.add_hash(BLACK_HASH, platform, is_black=True)
            with STEP('Validate hash added to mgmt'):
                sleep(30)
                hashes_list = g.manager.get_hashes(is_black='true')
                is_hash_found = False
                for hash in hashes_list:
                    if hash.get('id') == BLACK_HASH:
                        is_hash_found = True
                assert is_hash_found, 'Hash {} not found on mgmt'.format(BLACK_HASH)
                asset_id = get_latest_asset_file_path(g.manager.os_handle)
                assert is_hash_in_mgmt_asset_file(g.manager.os_handle, BLACK_HASH, asset_id), 'hash {hash} not found in mgmt asset file {asset}'. \
                    format(hash=BLACK_HASH, asset=asset_id)

            with STEP('Validate agent got asset'):
                wait_for_asset()
                if not is_asset_file_in_agent(os_handle, asset_id):
                    report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
                else:
                    if not is_hash_in_agent_asset_file(os_handle, BLACK_HASH, asset_id):
                        report_issue(g.issues, 'Hash {hsh} not found in agent asset file {asst}'.format(hsh=BLACK_HASH, asst=asset_id), False)

    with STEP('Run black file'):

        with STEP('Run file'):
            timestamp = time()
            sleep(3)
            log.debug("timestamp is {}".format(timestamp))
            filename = 'npp.exe'
            local_path = os.path.join(Config.automation_root_dir, 'tests', 'windows', 'assets', filename)
            remote_file_path = os_handle.os.path.join(os_handle.TEMP_DIR_PATH, filename)
            os_handle.upload_local_file(local_path, remote_file_path)
            try:
                os_handle.run(remote_file_path, timeout=20)
            except:
                log.error('fail to run file. Trying to continue test')

        with STEP('Validate file blocked in agent'):
            if not is_strings_in_agent_log(os_handle, ['Blocked process', 'npp.exe'], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP('Validate "threat" has been added to the MGMT as "Blocked"'):
            sleep(30)
            threats = g.manager.get_threats(content_hash=BLACK_HASH, resolved=False)
            assert len(threats) >= 1, "Threat was not arrived to mgmt"
            threat = g.manager.get_threats(content_hash=BLACK_HASH, mitigation_status=2, resolved=False)
            assert len(threat) >= 1, "Threat was not arrived as Blocked to mgmt"

        with STEP('Validate threat in activity page'):
            assert ActivitiesWrap.check_activity_in_management('NEW_THREAT_PREEMPTIVE_BLOCK',
                                                               timestamp), 'There no activity log saying that threat was blocked'

        with STEP('resolve threats'):
            g.manager.resolve_threats(agent_id=g.agent_id)

    with STEP('Run White threat file'):

        with STEP('Set protect mode'):
            change_management_options(auto_mitigation_action='mitigation.quarantineThreat', mitigation_mode='protect',
                                      mitigation_mode_suspicious='detect', agent_notification=True)
            wait_for_asset()

        with STEP('Run file'):
            init_threats = len(g.manager.get_threats(content_hash=WHITE_HASH, resolved=False))
            timestamp = time()
            sleep(3)
            try:
                os_handle.create_and_execute_threat(threat_type='default')
                remote_path = os.path.join(os_handle.TEMP_DIR_PATH, os_handle.threat_files.get('default'))
                os_handle.os.startfile(remote_path)
            except:
                log.error('fail on threat execution. Trying to continue test')

        with STEP('Validate file running'):
            process_name = os_handle.threat_files.get('default')
            with STEP('Checking {} process is running'.format(process_name)):
                timeout = Timeout(10)
                process = False
                while not process and not timeout.is_expired():
                    sleep(3)
                    process = os_handle.find_process_by_name(process_name)
                if not process:
                    raise Exception("{} is not running when it should".format(process_name))

        with STEP('Validate SilentWhitelist in agent log'):
            if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'SilentWhitelist', process_name], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP('Kill running process of {}'.format(process_name)):
            try:
                os_handle.modules.psutil.Process(process[0]).terminate()
            except NoSuchProcess:
                log.error("Can't kill {} process. Trying to continue test".format(process_name))

            with STEP('Validate "threat" has NOT been added to the MGMT'):
                sleep(30)
                threats = g.manager.get_threats(content_hash=WHITE_HASH, resolved=False)
                assert len(threats) == init_threats, "Threat has been added to mgmt"

            with STEP('Validate threat NOT in activity page'):
                assert not ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                       timestamp), 'There is activity log saying that threat was mitigated'

    with STEP('Delete Black hash'):
        with STEP('Remove blask hash'):
            g.manager.remove_hash(BLACK_HASH)

        with STEP('Validate hash deleted from mgmt'):
            sleep(30)
            hashes_list = g.manager.get_hashes(is_black='true')
            is_hash_found = False
            for hash in hashes_list:
                if hash.get('id') == BLACK_HASH:
                    is_hash_found = True
            assert not is_hash_found, 'Hash {} still appears on mgmt'.format(BLACK_HASH)
            asset_id = get_latest_asset_file_path(g.manager.os_handle)
            assert not is_hash_in_mgmt_asset_file(g.manager.os_handle,
                                              BLACK_HASH, asset_id), 'Deleted hash appears in latest asset file on mgmt'
        with STEP('Validate agent got asset'):
            wait_for_asset()
            if not is_asset_file_in_agent(os_handle, asset_id):
                report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
            else:
                if is_hash_in_agent_asset_file(os_handle, BLACK_HASH, asset_id):
                    report_issue(g.issues,'Deleted hash {hash} appears in latest asset file {asset} on agent'.format(hsh=BLACK_HASH, asst=asset_id), False)


        with STEP('Run file'):
            try:
                os_handle.run(remote_file_path, timeout=20)
            except:
                log.error('fail to run file. Trying to continue test')

        with STEP('Validate file running'):
            process_name = 'npp.exe'
            with STEP('Checking {} process is running'.format(process_name)):
                timeout = Timeout(10)
                process = False
                while not process and not timeout.is_expired():
                    sleep(3)
                    process = os_handle.find_process_by_name(process_name)
                if not process:
                    raise Exception("{} is not running when it should".format(process_name))

        with STEP('Kill running process of {}'.format(process_name)):
            os_handle.modules.psutil.Process(process[0]).terminate()

    with STEP('Delete White hash'):

        with STEP('Remove white hash'):
            g.manager.remove_hash(WHITE_HASH)

        with STEP('Validate hash deleted from mgmt'):
            sleep(30)
            hashes_list = g.manager.get_hashes(is_black='false')
            is_hash_found = False
            for hash in hashes_list:
                if hash.get('id') == WHITE_HASH:
                    is_hash_found = True
            assert not is_hash_found, 'Hash {} still appears on mgmt'.format(WHITE_HASH)
            asset_id = get_latest_asset_file_path(g.manager.os_handle)
            assert not is_hash_in_mgmt_asset_file(g.manager.os_handle,
                                                  WHITE_HASH, asset_id), 'Deleted hash still appears in latest asset file on mgmt'
        with STEP('Validate agent got asset'):
            wait_for_asset()
            if not is_asset_file_in_agent(os_handle, asset_id):
                report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
            else:
                if is_hash_in_agent_asset_file(os_handle, WHITE_HASH, asset_id):
                    report_issue(g.issues, 'Deleted hash appears in latest asset file on agent'.format(hsh=WHITE_HASH, asst=asset_id), False)

        with STEP('Run specific threat'):
            timestamp = time()
            sleep(3)
            try:
                os_handle.create_and_execute_threat(threat_type='default')
            except:
                log.error('fail on threat execution. Trying to continue test')

        with STEP('Validate threat detected in agent'):
            if not is_strings_in_agent_log(os_handle, ['Mitigator::quarantineThreat',
                                                       os_handle.threat_files.get('default')], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP('Validate threat in mitigated state in mgmt'):
            sleep(30)
            threat = g.manager.get_threats(content_hash=WHITE_HASH, resolved=False)
            assert len(threat) == 1, "Threat was not arrived to mgmt"
            specific_threat = g.manager.get_specific_threat(threat[0].get('id'))
            mitigation_status = specific_threat.get('mitigation_status')
            assert mitigation_status == 0, 'Threat arrived to mgmt as {arrived} instead of {expected}'.format(
                arrived=mitigation_statuses.get(mitigation_status), expected=mitigation_statuses.get(0))

        with STEP('Verify the "threat" has been added to the activity'):
            assert ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                               timestamp), 'There no activity log saying that threat was mitigated'

        with STEP('Resolve threats'):
            g.manager.resolve_threats(agent_id=g.agent_id)

        with STEP('Validate no unresolved threats'):
            assert not g.manager.get_threats(resolved=False), 'Not all threats were resolved'
