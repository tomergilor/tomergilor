from time import sleep, time

import slash
from slash import g
from slash_step import STEP

from Scripts.Issue import report_issue
from tests.QA.common_functions.agent import is_asset_file_in_agent, is_hash_in_agent_asset_file, is_strings_in_agent_log
from tests.QA.common_functions.common import get_os_family_from_platform, ActivitiesWrap
from tests.QA.common_functions.management import get_latest_asset_file_path, is_hash_in_mgmt_asset_file, \
    change_management_options, validate_created_asset_at_mgmt_and_agent, \
    get_default_policy_id, change_rebootless_settings


def is_app_in_applications(filename):
    apps = g.manager.get_agent_applications(g.agent_id)
    for app in apps:
        if app.get('name') in filename:
            return True
    return False


def path_exclusion_changes_test(agent_machine, list_id):
    os_handle = agent_machine.os_handle
    change_rebootless_settings()
    agent_machine.machine.bringup_os(return_os_handle=True, reboot=True)
    folder_to_exclude = os_handle.TEMP_DIR_PATH
    platform = get_os_family_from_platform(os_handle)

    with STEP('Exclusion - Folder (path)'):

        with STEP("Add a new exclusion (Path) with temp folder for created list"):
            exclusion = g.manager.create_new_path_exclusion(os_family=platform, exclude_path=folder_to_exclude,
                                                            lists=[list_id])
            folder_id = exclusion[0].get('id')
            with STEP("Validate asset added to mgmt"):
                exclusions = g.manager.get_path_exclusions_list(list_id)
                assert exclusions[0].get('id') == folder_id, "Created asset doesn't appears in mgmt"
            validate_created_asset_at_mgmt_and_agent(os_handle, folder_to_exclude)

    with STEP('Run threats'):

        with STEP('Upload and run threat from exclusion folder'):
            threat_name = os_handle.threat_file('default')
            init_threats = len(g.manager.get_threats(agent=g.agent_id, display_name=threat_name))
            timestamp = time()
            sleep(3)
            os_handle.create_and_execute_threat(threat_type='default', dir=folder_to_exclude)
            sleep(30)

        with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
            if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                       os_handle.threat_files.get('default')], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP("Verify mgmt didn't get threat"):
            threat_detected = g.manager.expect_threat(init_threats=init_threats,
                                                      agent=g.agent_id,
                                                      display_name=threat_name)
            assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(folder_to_exclude)

        with STEP('Verify the "threat" has not been added to the activity'):
            assert not ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                   timestamp), 'There no activity log saying that an agent was automatically decommissioned'

    with STEP('Exclusion - Folder path with sub-folder'):
        exclusion_type = 'subfolders'
        with STEP('Update created exclusion with "include subfolder"'):
            g.manager.update_exclusions(list_id, folder_id, exclusion_type=exclusion_type)

        with STEP('Validate exclusion_type of the exclusion'):
            exclusion = g.manager.get_exclusions(list_id, folder_id)
            assert exclusion.get('exclusion_type') == exclusion_type

        with STEP('Add 2 sub folders (nested folders)'):
            path_to_fisrt_dir = os_handle.os.path.join(folder_to_exclude, '1')
            os_handle.os.makedirs(path_to_fisrt_dir)

            with STEP('Validate folder 1 created'):
                assert os_handle.os.path.isdir(path_to_fisrt_dir), "folder 1 wasn't created"

            path_to_second_dir = os_handle.os.path.join(path_to_fisrt_dir, '2')
            os_handle.os.makedirs(path_to_second_dir)

            with STEP('Validate folder 2 created'):
                assert os_handle.os.path.isdir(path_to_second_dir), "folder 2 wasn't created"

        with STEP('Wait for asset'):
            sleep(180)  # wait_for_asset(timeout=60)

        with STEP('Upload and run threat for first folder'):
            with STEP('Upload and run threat from exclusion folder'):
                init_threats = len(g.manager.get_threats(agent=g.agent_id, display_name=threat_name))
                timestamp = time()
                sleep(3)
                os_handle.create_and_execute_threat(threat_type='default', dir=path_to_fisrt_dir)
                sleep(30)

            with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
                if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                           os_handle.threat_files.get('default')], timestamp):
                    report_issue(g.issues, 'there is no searched string in agent log', False)

            with STEP("Verify mgmt didn't get threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats,
                                                          agent=g.agent_id,
                                                          display_name=threat_name)
                assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                    folder_to_exclude)

            with STEP('Verify the "threat" has not been added to the activity'):
                assert not ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                       timestamp), 'There is activity log saying that mgmt got threat'

        with STEP('Upload and run threat for second folder'):
            with STEP('Upload and run threat from exclusion folder'):
                init_threats = len(g.manager.get_threats(agent=g.agent_id, display_name=threat_name))
                timestamp = time()
                sleep(3)
                os_handle.create_and_execute_threat(threat_type='default', dir=path_to_second_dir)
                sleep(30)

            with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
                if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                           os_handle.threat_files.get('default')], timestamp):
                    report_issue(g.issues, 'there is no searched string in agent log', False)

            with STEP("Verify mgmt didn't get threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats,
                                                          agent=g.agent_id,
                                                          display_name=threat_name)
                assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                    folder_to_exclude)

            with STEP('Verify the "threat" has not been added to the activity'):
                assert not ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                       timestamp), 'There is activity log saying that mgmt got threat'

    # with STEP('Inject'):
    #     with STEP('Change the Mgmt to support mode'):
    #         change_settings_ini_key_and_restart_services(g.manager.os_handle, 'api', 'support_mode', 'True')
    #
    #     with STEP('Add a new exclusion (Path) with temp folder'):
    #         with STEP("Add a new exclusion (Path) with temp folder for created list"):
    #             g.manager.update_exclusions(list_id, folder_id, inject=False)
    #         validate_created_asset_at_mgmt_and_agent(os_handle, folder_to_exclude)
    #
    #         with STEP('Verify agent got the new list with the correct exclusions'):
    #             asset_id = get_latest_asset_file_path(g.manager.os_handle)
    #             expected_str = '"inject": false'
    #             assert is_hash_in_mgmt_asset_file(g.manager.os_handle, expected_str,
    #                                               asset_id), '{} doesnt appears in latest asset file on mgmt'.format(expected_str)
    #             err_msg = 'String {str} doesnt appears in latest asset file {asset} on agent'. \
    #                 format(str=expected_str, asset=asset_id)
    #             assert is_hash_in_agent_asset_file(os_handle, expected_str, asset_id), err_msg

    with STEP('Remove folder exclusion'):

        with STEP('Delete exclusion'):
            g.manager.delete_path_exclusions(id__in=folder_id)
            sleep(30)

        with STEP("Validate exclusion deleted from mgmt"):
            exclusions = g.manager.get_path_exclusions_list(list_id)
            assert len(exclusions) == 0, "Created exclusion still appears in mgmt"

        with STEP("Validate deleted exclusion in asset file on mgmt"):
            asset_id = get_latest_asset_file_path(g.manager.os_handle)
            assert not is_hash_in_mgmt_asset_file(g.manager.os_handle, folder_to_exclude,
                                              asset_id), 'Added exclusion still appears in latest asset file on mgmt'

        with STEP('Verify agent got the new list with the correct exclusions'):
            sleep(180) # wait_for_asset(timeout=60)
            if not is_asset_file_in_agent(os_handle, asset_id):
                report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
            else:
                err_msg = 'Added exclusion {excl} still appears in latest asset file {asset} on agent'. \
                    format(excl=folder_id, asset=asset_id)
                if is_hash_in_agent_asset_file(os_handle, folder_to_exclude, asset_id):
                    report_issue(g.issues, err_msg, False)

        with STEP('Run threat from excluded folder'):

            with STEP('Upload and run threat from exclusion folder'):
                init_threats = len(g.manager.get_threats(agent=g.agent_id, display_name=threat_name))
                timestamp = time()
                sleep(3)
                os_handle.create_and_execute_threat(threat_type='default', dir=folder_to_exclude)
                sleep(30)

            with STEP('Validate agent detected threat'):
                pass

            with STEP("Verify mgmt got threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats,
                                                          agent=g.agent_id,
                                                          display_name=threat_name)
                assert threat_detected, "Threat not detected in mgmt"

            with STEP('Verify the "threat" has been added to the activity'):
                assert ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                   timestamp), 'There is NO activity log saying that mgmt got threat'

        with STEP('Run threat from nested folder'):

            with STEP('Upload and run threat from exclusion folder'):
                init_threats = len(g.manager.get_threats(agent=g.agent_id, display_name=threat_name))
                timestamp = time()
                sleep(3)
                os_handle.create_and_execute_threat(threat_type='default', dir=path_to_fisrt_dir)
                sleep(30)

            with STEP('Validate agent detected threat'):
                pass

            with STEP("Verify mgmt got threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats,
                                                          agent=g.agent_id,
                                                          display_name=threat_name)
                assert threat_detected, "Threat not detected in mgmt"

            with STEP('Verify the "threat" has been added to the activity'):
                assert ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                   timestamp), 'There is NO activity log saying that mgmt got threat'

    with STEP('Exclusion - File path'):
        file_name = os_handle.threat_files.get('default')
        path_to_file_to_exclude = os_handle.os.path.join(folder_to_exclude, file_name)
        with STEP("Add a new exclusion (Path) with temp folder for created list"):
            exclusion = g.manager.create_new_path_exclusion(os_family=platform, exclude_path=path_to_file_to_exclude,
                                                            is_file=True, lists=[list_id], exclusion_type='file')
            folder_id = exclusion[0].get('id')
            with STEP("Validate asset added to mgmt"):
                exclusions = g.manager.get_path_exclusions_list(list_id)
                assert exclusions[0].get('id') == folder_id, "Created asset doesn't appears in mgmt"
        validate_created_asset_at_mgmt_and_agent(os_handle, folder_to_exclude)

    with STEP('Run threats'):

        with STEP('Upload and run threat from exclusion folder'):
            init_threats = len(g.manager.get_threats(agent=g.agent_id, display_name=threat_name))
            timestamp = time()
            sleep(3)
            os_handle.create_and_execute_threat(threat_type='default', dir=folder_to_exclude)
            sleep(30)

        with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
            if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                       os_handle.threat_files.get('default')], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP("Verify mgmt didn't get threat"):
            threat_detected = g.manager.expect_threat(init_threats=init_threats,
                                                      agent=g.agent_id,
                                                      display_name=threat_name)
            assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                folder_to_exclude)

        with STEP('Verify the "threat" has not been added to the activity'):
            assert not ActivitiesWrap.check_activity_in_management('THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS',
                                                                   timestamp), 'There is activity log saying that mgmt got threat'

    with STEP('Remove file path exclusion'):
        with STEP('Delete exclusion'):
            g.manager.delete_path_exclusions(id__in=folder_id)
            sleep(30)

        with STEP("Validate exclusion deleted from mgmt"):
            exclusions = g.manager.get_path_exclusions_list(list_id)
            assert len(exclusions) == 0, "Created exclusion still appears in mgmt"

        with STEP("Validate deleted exclusion in asset file on mgmt"):
            asset_id = get_latest_asset_file_path(g.manager.os_handle)
            assert not is_hash_in_mgmt_asset_file(g.manager.os_handle, folder_to_exclude,
                                                  asset_id), 'Added exclusion still appears in latest asset file on mgmt'

        with STEP('Verify agent got the new list with the correct exclusions'):
            sleep(180)  # wait_for_asset(timeout=60)
            if not is_asset_file_in_agent(os_handle, asset_id):
                report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
            else:
                err_msg = 'Added exclusion {excl} still appears in latest asset file {asset} on agent'. \
                    format(excl=folder_id, asset=asset_id)
                if is_hash_in_agent_asset_file(os_handle, folder_to_exclude, asset_id):
                    report_issue(g.issues, err_msg, False)

    with STEP('Removing created dirs'):
        os_handle.modules.shutil.rmtree(path_to_fisrt_dir)


@slash.tag('no_checks_after_test')
def test_path_exclusion_changes(agent_machine):
    list_id = None

    with STEP('Preparations'):
        change_management_options(auto_mitigation_action='mitigation.quarantineThreat', mitigation_mode='protect',
                                  mitigation_mode_suspicious='detect', agent_notification=True)
        list_name = 'test_list'
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
        path_exclusion_changes_test(agent_machine, list_id)

    with STEP('Delete created exlusion list'):
        g.manager.delete_exclusion_list(list_id)
        with STEP('Validate exclusion list was deleted'):
            is_found = False
            excl_lists = g.manager.get_list_of_exclusion_lists()
            for exc_list in excl_lists:
                if exc_list['id'] == list_id:
                    is_found = True
            assert not is_found, 'Exclusion list was not deleted from mgmt'
            sleep(180)  # wait_for_asset(timeout=60)

    with STEP('Running test with global exclusion list'):
        list_id = g.manager.get_list_of_exclusion_lists()[0].get('id')
        path_exclusion_changes_test(agent_machine, list_id)
