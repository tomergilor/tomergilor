import random
import string
from time import sleep, time

import slash
from slash import g
from slash_step import STEP

from Scripts.Issue import report_issue
from tests.QA.common_functions.agent import is_asset_file_in_agent, is_hash_in_agent_asset_file, is_strings_in_agent_log
from tests.QA.common_functions.common import get_os_family_from_platform, ActivitiesWrap
from tests.QA.common_functions.management import get_latest_asset_file_path, is_hash_in_mgmt_asset_file, \
    validate_created_asset_at_mgmt_and_agent, change_settings_ini_key_and_restart_services, change_rebootless_settings
from tests.QA.functionality.management.ui_bahamas.pages.main_page import MainPage
from tests.QA.functionality.management.ui_bahamas.pages.p_main.dashboard_page import Dashboard
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page import SettingsPage
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page import ExclusionsTab
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.edit_exclusion_page import \
    EditExclusionDialog
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.edit_list import \
    EditListDialog
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.new_exclusion_page import \
    NewExclusionDialog
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.policies import PoliciesTab
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.policies.policy_confirmation_window import \
    PolicyConfirmationWindow
from tests.QA.functionality.management.ui_bahamas.tests.ui_utils import login_to_mgmt, switch_to_default_iframe, \
    switch_to_dashboard_iframe

WAITING_TIME = 5


def is_app_in_applications(filename):
    apps = g.manager.get_agent_applications(g.agent_id)
    for app in apps:
        if app.get('name') in filename:
            return True
    return False


def path_exclusion_changes_test(os_handle, list_id, list_name):
    folder_to_exclude = '{}\\'.format(os_handle.TEMP_DIR_PATH)
    platform = get_os_family_from_platform(os_handle)

    with STEP('Exclusion - Folder (path)'):
        driver = g.driver
        with STEP('Go to Settings'):
            MainPage(driver).left_side_tabs.settings_tab.click()
        with STEP('Go to exclusions tab'):
            SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
            exclusions_tab = ExclusionsTab(driver)
        with STEP('Click Path Type Open button'):
            exclusions_tab.type_box.path_type.open_button.click()
        with STEP('Click "new exclusion" button'):
            exclusions_tab.header.new_exclusion_btn.click()
            dialog = NewExclusionDialog(driver)
        with STEP('Select "Path" from type selector'):
            dialog.type_selector.select_by_text('Path')
        with STEP('Select {} OS'.format(platform)):
            dialog.os_selector.select_by_text(platform)
        with STEP('Enter {} folder into path textbox'.format(folder_to_exclude)):
            dialog.path.enter_text(folder_to_exclude)
        with STEP('Unselect Global'):
            dialog.unselect_by_name('Global')
        with STEP('Select {} list'.format(list_name)):
            dialog.select_by_name(list_name)
        with STEP('Set description = "{}"'.format(folder_to_exclude)):
            dialog.description.enter_text(folder_to_exclude)
        with STEP('Click Save button'):
            dialog.save_button.click()
        with STEP('Waiting {} seconds'.format(WAITING_TIME)):
            sleep(WAITING_TIME)

        exclusions = g.manager.get_path_exclusions_list(list_id)
        folder_id = exclusions[0].get('id')

    activity_type = 'THREAT_MITIGATION_REPORT_QUARANTINE_SUCCESS'
    with STEP('Run threats'):
        with STEP('Upload and run threat from exclusion folder'):
            timestamp = time()
            sleep(3)
            init_threats = len(g.manager.get_threats(agent=g.agent_id, resolved=False))
            os_handle.create_and_execute_threat(threat_type='default', dir=folder_to_exclude)

        with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
            if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                       os_handle.threat_files.get('default')], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP("Verify mgmt didn't get threat"):
            threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id, resolved=False)
            assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                folder_to_exclude)

            dashboard = Dashboard(driver)
            with STEP('Click on dashboard tab'):
                MainPage(driver).left_side_tabs.dashboard_tab.click()
                with STEP('Switch to dashboard iframe'):
                    switch_to_dashboard_iframe(driver)
                summary = dashboard.threats.summary
            with STEP('Validating threats count in dashboard'):
                assert (summary.active.get_count() + summary.mitigated.get_count() +
                        summary.blocked.get_count() + summary.suspicious.get_count()) == init_threats
                with STEP('Switch to default iframe'):
                    switch_to_default_iframe(driver)  # back from iframe

        with STEP('Verify the "threat" has not been added to the activity'):
            err_msg = 'There no activity log saying that an agent was automatically decommissioned'
            assert not ActivitiesWrap.check_activity_in_management(activity_type, timestamp), err_msg

    with STEP('Exclusion - Folder path with sub-folder'):
        exclusion_type = 'subfolders'
        with STEP('Update created exclusion with "include subfolder"'):
            with STEP('Click on Settings tab'):
                MainPage(driver).left_side_tabs.settings_tab.click()
            with STEP('Click on exclusions tab'):
                SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
            with STEP('Click on {} list'.format(list_name)):
                exclusions_tab.left_sidebar.get_list_by_name(list_name).click()
            with STEP('Click Path Type Open button'):
                exclusions_tab.type_box.path_type.open_button.click()
            with STEP('Click on row with text {}'.format(folder_to_exclude)):
                exclusions_tab.exclusion_grid.grid.click_row_by_text(folder_to_exclude)
                edit_dialog = EditExclusionDialog(driver)
            with STEP('Select "include subfolders" checkbox'):
                edit_dialog.include_subfolders_checkbox.check()
            with STEP('Click save button'):
                edit_dialog.save_btn.click()
            with STEP('Waiting {} seconds'.format(WAITING_TIME)):
                sleep(WAITING_TIME)

        with STEP('Validate exclusion_type of the exclusion'):
            exclusion = g.manager.get_exclusions(list_id, folder_id)
            assert exclusion.get('exclusion_type') == exclusion_type

        with STEP('Add 2 sub folders (nested folders)'):
            path_to_first_dir = os_handle.os.path.join(folder_to_exclude, '1')
            os_handle.os.makedirs(path_to_first_dir)

            with STEP('Validate folder 1 created'):
                assert os_handle.os.path.isdir(path_to_first_dir), "folder 1 wasn't created"

            path_to_second_dir = os_handle.os.path.join(path_to_first_dir, '2')
            os_handle.os.makedirs(path_to_second_dir)

            with STEP('Validate folder 2 created'):
                assert os_handle.os.path.isdir(path_to_second_dir), "folder 2 wasn't created"

        with STEP('Wait for asset'):
            sleep(180)  # wait_for_asset(timeout=60)

        with STEP('Upload and run threat for first folder'):
            with STEP('Upload and run threat from exclusion folder'):
                timestamp = time()
                sleep(3)
                init_threats = len(g.manager.get_threats(agent=g.agent_id, resolved=False))
                os_handle.create_and_execute_threat(threat_type='default', dir=path_to_first_dir)
                sleep(WAITING_TIME)

            with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
                if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                           os_handle.threat_files.get('default')], timestamp):
                    report_issue(g.issues, 'there is no searched string in agent log', False)

            with STEP("Verify mgmt didn't get threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id, resolved=False)
                assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                    folder_to_exclude)
                with STEP('Click on dashboard tab'):
                    MainPage(driver).left_side_tabs.dashboard_tab.click()
                    with STEP('Switch to dashboard iframe'):
                        switch_to_dashboard_iframe(driver)
                with STEP('Validating threats count in dashboard'):
                    assert (summary.active.get_count() + summary.mitigated.get_count() +
                            summary.blocked.get_count() + summary.suspicious.get_count()) == init_threats
                    with STEP('Switch to default iframe'):
                        switch_to_default_iframe(driver)  # back from iframe

            with STEP('Verify the "threat" has not been added to the activity'):
                err_msg = 'There is activity log saying that mgmt got threat'
                assert not ActivitiesWrap.check_activity_in_management(activity_type, timestamp), err_msg

        with STEP('Upload and run threat for second folder'):
            with STEP('Upload and run threat from exclusion folder'):
                timestamp = time()
                sleep(3)
                init_threats = len(g.manager.get_threats(agent=g.agent_id, resolved=False))
                os_handle.create_and_execute_threat(threat_type='default', dir=path_to_second_dir)
                sleep(WAITING_TIME)

            with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
                if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                           os_handle.threat_files.get('default')], timestamp):
                    report_issue(g.issues, 'there is no searched string in agent log', False)

            with STEP("Verify mgmt didn't get threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id, resolved=False)
                assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                    folder_to_exclude)
                with STEP('Click on dashboard tab'):
                    MainPage(driver).left_side_tabs.dashboard_tab.click()
                with STEP('Switch to dashboard iframe'):
                    switch_to_dashboard_iframe(driver)
                with STEP('Validating threats count in dashboard'):
                    assert (summary.active.get_count() + summary.mitigated.get_count() +
                            summary.blocked.get_count() + summary.suspicious.get_count()) == init_threats
                    with STEP('Switch to default iframe'):
                        switch_to_default_iframe(driver)  # back from iframe

            with STEP('Verify the "threat" has not been added to the activity'):
                err_msg = 'There is activity log saying that mgmt got threat'
                assert not ActivitiesWrap.check_activity_in_management(activity_type, timestamp), err_msg

    with STEP('Inject'):
        with STEP('Change the Mgmt to support mode'):
            change_settings_ini_key_and_restart_services(g.manager.os_handle, 'api', 'support_mode', 'True')

        with STEP('Add "?advanced" to url'):
            change_settings_ini_key_and_restart_services(g.manager.os_handle, 'api', 'support_mode', 'True')
            driver.get(driver.current_url + '?advanced=true')

        with STEP('Add a new exclusion (Path) with temp folder'):
            with STEP('Click on Settings tab'):
                MainPage(driver).left_side_tabs.settings_tab.click()
            with STEP('Click on exclusions tab'):
                SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
            with STEP('Click on {} list'.format(list_name)):
                exclusions_tab.left_sidebar.get_list_by_name(list_name).click()
            with STEP('Click Path Type Open button'):
                exclusions_tab.type_box.path_type.open_button.click()
            with STEP('Click on row with text {}'.format(folder_to_exclude)):
                exclusions_tab.exclusion_grid.grid.click_row_by_text(folder_to_exclude)
                edit_dialog = EditExclusionDialog(driver)
            with STEP('UnSelect "inject" checkbox'):
                edit_dialog.inject_checkbox.uncheck()
            with STEP('Click save button'):
                edit_dialog.save_btn.click()
            with STEP('Waiting {} seconds'.format(WAITING_TIME)):
                sleep(WAITING_TIME)

            validate_created_asset_at_mgmt_and_agent(os_handle, folder_to_exclude)

            with STEP('Verify agent got the new list with the correct exclusions'):
                asset_id = get_latest_asset_file_path(g.manager.os_handle)
                expected_str = '"inject": false'
                assert is_hash_in_mgmt_asset_file(
                    g.manager.os_handle, expected_str,
                    asset_id), '{} doesnt appears in latest asset file on mgmt'.format(expected_str)
                err_msg = 'String {str} doesnt appears in latest asset file {asset} on agent'. \
                    format(str=expected_str, asset=asset_id)
                assert is_hash_in_agent_asset_file(os_handle, expected_str, asset_id), err_msg

    with STEP('Remove folder exclusion'):

        with STEP('Delete exclusion'):
            with STEP('Click on Settings tab'):
                MainPage(driver).left_side_tabs.settings_tab.click()
            with STEP('Click on exclusions tab'):
                SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
            with STEP('Click on {} list'.format(list_name)):
                exclusions_tab.left_sidebar.get_list_by_name(list_name).click()
            with STEP('Click Path Type Open button'):
                exclusions_tab.type_box.path_type.open_button.click()
            with STEP('Select checkbox on row with text "{}"'.format(folder_to_exclude)):
                exclusions_tab.exclusion_grid.grid.get_row_by_text(folder_to_exclude).checkbox.check()
            with STEP('Click on "delete exclusion" button'):
                exclusions_tab.header.delete_exclusion_btn.click()
            with STEP('Validate confirmation windows appears'):
                PolicyConfirmationWindow(driver).is_displayed()
            with STEP('Click yes in confirmation window'):
                PolicyConfirmationWindow(driver).yes_btn.click()
            with STEP('Waiting {} seconds'.format(WAITING_TIME)):
                sleep(WAITING_TIME)

        with STEP("Validate exclusion deleted from mgmt"):
            exclusions = g.manager.get_path_exclusions_list(list_id)
            assert len(exclusions) == 0, "Created exclusion still appears in mgmt"
            assert not exclusions_tab.exclusion_grid.grid.get_row_by_text(folder_to_exclude).is_in_dom()

        with STEP("Validate deleted exclusion in asset file on mgmt"):
            asset_id = get_latest_asset_file_path(g.manager.os_handle)
            assert not is_hash_in_mgmt_asset_file(g.manager.os_handle, folder_to_exclude,
                                                  asset_id), 'Exclusion still appears in latest asset file on mgmt'

        with STEP('Verify agent got the new list with the correct exclusions'):
            sleep(180)  # wait_for_asset(timeout=60)
            if not is_asset_file_in_agent(os_handle, asset_id):
                report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)
            else:
                err_msg = 'Added exclusion {excl} still appears in latest asset file {asset} on agent'.format(
                    excl=folder_id, asset=asset_id)
                if is_hash_in_agent_asset_file(os_handle, folder_to_exclude, asset_id):
                    report_issue(g.issues, err_msg, False)

        with STEP('Run threat from excluded folder'):

            with STEP('Upload and run threat from exclusion folder'):
                init_threats = len(g.manager.get_threats(agent=g.agent_id, resolved=False))
                timestamp = time()
                sleep(3)
                os_handle.create_and_execute_threat(threat_type='default', dir=folder_to_exclude)

            with STEP('Validate agent detected threat and the threat of FolderExcluded type'):
                pass
            with STEP("Verify mgmt got threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id, resolved=False)
                assert threat_detected, "Threat not detected in mgmt"
                with STEP('Click on dashboard tab'):
                    MainPage(driver).left_side_tabs.dashboard_tab.click()
                    with STEP('Switch to dashboard iframe'):
                        switch_to_dashboard_iframe(driver)
                with STEP('Validating threats count in dashboard'):
                    assert (summary.active.get_count() + summary.mitigated.get_count() +
                            summary.blocked.get_count() + summary.suspicious.get_count()) > init_threats
                    with STEP('Switch to default iframe'):
                        switch_to_default_iframe(driver)  # back from iframe

            with STEP('Verify the "threat" has been added to the activity'):
                err_msg = 'There is NO activity log saying that mgmt got threat'
                assert ActivitiesWrap.check_activity_in_management(activity_type, timestamp), err_msg

        with STEP('Run threat from nested folder'):

            with STEP('Upload and run threat from exclusion folder'):
                init_threats = len(g.manager.get_threats(agent=g.agent_id, resolved=False))
                timestamp = time()
                sleep(3)
                os_handle.create_and_execute_threat(threat_type='default', dir=path_to_first_dir)

            with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
                pass

            with STEP("Verify mgmt got threat"):
                threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id, resolved=False)
                assert threat_detected, "Threat not detected in mgmt"
                with STEP('Click on dashboard tab'):
                    MainPage(driver).left_side_tabs.dashboard_tab.click()
                    with STEP('Switch to dashboard iframe'):
                        switch_to_dashboard_iframe(driver)
                with STEP('Validating threats count in dashboard'):
                    assert (summary.active.get_count() + summary.mitigated.get_count() +
                            summary.blocked.get_count() + summary.suspicious.get_count()) > init_threats
                    with STEP('Switch to default iframe'):
                        switch_to_default_iframe(driver)  # back from iframe

            with STEP('Verify the "threat" has been added to the activity'):
                err_msg = 'There is NO activity log saying that mgmt got threat'
                assert ActivitiesWrap.check_activity_in_management(activity_type, timestamp), err_msg

    with STEP('Exclusion - File path'):
        file_name = os_handle.threat_files.get('default')
        path_to_file_to_exclude = os_handle.os.path.join(folder_to_exclude, file_name)
        with STEP("Add a new exclusion (Path) with temp folder for created list"):
            with STEP('Click on Settings tab'):
                MainPage(driver).left_side_tabs.settings_tab.click()
            with STEP('Click on exclusions tab'):
                SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
                exclusions_tab = ExclusionsTab(driver)
            with STEP('Click on {} list'.format(list_name)):
                exclusions_tab.left_sidebar.get_list_by_name(list_name).click()
            with STEP('Select path type'):
                exclusions_tab.type_box.path_type.click()
            with STEP('Click "new exclusion" button'):
                exclusions_tab.header.new_exclusion_btn.click()
                new_excl_dialog = NewExclusionDialog(driver)
            with STEP('Select {} OS'.format(platform)):
                new_excl_dialog.os_selector.select_by_text(platform)
            with STEP('Enter text "{}" into path textbox'.format(path_to_file_to_exclude)):
                new_excl_dialog.path.enter_text(path_to_file_to_exclude)
            with STEP('Enter text "{}" into description textbox'.format(path_to_file_to_exclude)):
                new_excl_dialog.description.enter_text(path_to_file_to_exclude)
            with STEP('Click Save button'):
                new_excl_dialog.save_button.click()
            with STEP('Waiting {} seconds'.format(WAITING_TIME)):
                sleep(WAITING_TIME)

            exclusions = g.manager.get_path_exclusions_list(list_id)
            folder_id = exclusions[0].get('id')

        validate_created_asset_at_mgmt_and_agent(os_handle, folder_to_exclude)

    with STEP('Run threats'):

        with STEP('Upload and run threat from exclusion folder'):
            timestamp = time()
            sleep(3)
            init_threats = len(g.manager.get_threats(agent=g.agent_id, resolved=False))
            os_handle.create_and_execute_threat(threat_type='default', dir=folder_to_exclude)

        with STEP('Validate agent detected threat but the threat of FolderExcluded type'):
            if not is_strings_in_agent_log(os_handle, ['InternalMalwareDetected', 'FolderExcluded',
                                                       os_handle.threat_files.get('default')], timestamp):
                report_issue(g.issues, 'there is no searched string in agent log', False)

        with STEP("Verify mgmt didn't get threat"):
            threat_detected = g.manager.expect_threat(init_threats=init_threats, agent=g.agent_id, resolved=False)
            assert not threat_detected, "Threat still detected, although it ran from exclusion folder {}".format(
                folder_to_exclude)
            with STEP('Click on dashboard tab'):
                MainPage(driver).left_side_tabs.dashboard_tab.click()
                with STEP('Switch to dashboard iframe'):
                    switch_to_dashboard_iframe(driver)
            with STEP('Validating threats count in dashboard'):
                assert (summary.active.get_count() + summary.mitigated.get_count() +
                        summary.blocked.get_count() + summary.suspicious.get_count()) == init_threats
                with STEP('Switch to default iframe'):
                    switch_to_default_iframe(driver)  # back from iframe

        with STEP('Verify the "threat" has not been added to the activity'):
            err_msg = 'There is activity log saying that mgmt got threat'
            assert not ActivitiesWrap.check_activity_in_management(activity_type, timestamp), err_msg

    with STEP('Remove file path exclusion'):
        with STEP('Delete exclusion'):
            with STEP('Click on Settings tab'):
                MainPage(driver).left_side_tabs.settings_tab.click()
            with STEP('Click on exclusions tab'):
                SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
            with STEP('Click on {} list'.format(list_name)):
                exclusions_tab.left_sidebar.get_list_by_name(list_name).click()
            with STEP('Click Path Type Open button'):
                exclusions_tab.type_box.path_type.open_button.click()
            with STEP('Select checkbox for row with text "{}"'.format(path_to_file_to_exclude)):
                exclusions_tab.exclusion_grid.grid.get_row_by_text(path_to_file_to_exclude).checkbox.check()
            with STEP('Click "delete exclusion" button'):
                exclusions_tab.header.delete_exclusion_btn.click()
            with STEP('Validate confirmation windows appears'):
                PolicyConfirmationWindow(driver).is_displayed()
            with STEP('Click yes in confirmation window'):
                PolicyConfirmationWindow(driver).yes_btn.click()

            sleep(30)

        with STEP("Validate exclusion deleted from mgmt"):
            exclusions = g.manager.get_path_exclusions_list(list_id)
            assert len(exclusions) == 0, "Created exclusion still appears in mgmt"

        with STEP("Validate deleted exclusion in asset file on mgmt"):
            asset_id = get_latest_asset_file_path(g.manager.os_handle)
            assert not is_hash_in_mgmt_asset_file(g.manager.os_handle, folder_to_exclude,
                                                  asset_id), 'Exclusion still appears in latest asset file on mgmt'

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
        os_handle.modules.shutil.rmtree(path_to_first_dir)


@slash.tag('no_checks_after_test')
def test_ui_path_exclusion_changes(agent_ui_machine):
    change_rebootless_settings()
    agent_ui_machine.machine.bringup_os(return_os_handle=True, reboot=True)
    driver = g.driver
    login_to_mgmt(driver=driver)

    os_handle = agent_ui_machine.os_handle
    list_id = None

    with STEP('Go to Settings'):
        MainPage(driver).left_side_tabs.settings_tab.click()

    with STEP('Preparations'):
        policy_form = PoliciesTab(driver).policy_form
        with STEP('Select "Protect checkbox" for threats'):
            policy_form.policy_mode_options.threats.protect_checkbox.check()
        with STEP('Select "Detect checkbox" for suspicious'):
            policy_form.policy_mode_options.suspicious.detect_checkbox.check()
        with STEP('Select "Agent notifications on suspicious" checkbox'):
            policy_form.policy_mode_options.agent_notification_on_suspicious.check()

        if policy_form.save_button.is_in_dom():
            with STEP('Click save button'):
                policy_form.save_button.click()
            with STEP('Validate confirmation windows appears'):
                PolicyConfirmationWindow(driver).is_displayed()
            with STEP('Click yes in confirmation window'):
                PolicyConfirmationWindow(driver).yes_btn.click()

        suffix = ''.join([random.choice(string.lowercase) for i in xrange(10)])
        list_name = 'test_list_{}'.format(suffix)
        with STEP('Create new exclusion list and connect it to default policy'):
            with STEP('Click on exclusions tab'):
                SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
                exclusions_tab = ExclusionsTab(driver)
            with STEP('Click "new list" button'):
                exclusions_tab.left_sidebar.new_list_btn.click()
                new_list_dialog = EditListDialog(driver)
            with STEP('Enter list name="{}"'.format(list_name)):
                new_list_dialog.list_name.enter_text(list_name)
            with STEP('Select "Default"'):
                new_list_dialog.select_by_name('Default')
            with STEP('Click Save button'):
                new_list_dialog.save_button.click()

        with STEP('Validate exclusion list created in mgmt'):
            with STEP('Waiting {} seconds'.format(WAITING_TIME)):
                sleep(WAITING_TIME)
            exclusion_lists = g.manager.get_list_of_exclusion_lists()
            is_list_created = False
            for exclusion_list in exclusion_lists:
                if exclusion_list.get('name') == list_name:
                    is_list_created = True
                    list_id = exclusion_list.get('id')
            assert is_list_created, "List {} doesn't appears in mgmt".format(list_name)

    with STEP('Update policy with created Exclusion_list'):
        with STEP('Click on policies tab'):
            SettingsPage(driver).settings_tabs_panel.policies_tab.click()
        with STEP('Select {} exclusion list'.format(list_name)):
            policy_form.more_options.exclusions.exclusion_list_selector.select_by_text(list_name)
        with STEP('Click Save button'):
            policy_form.save_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()

    with STEP('Running test with created exclusion_list {}'.format(list_id)):
        path_exclusion_changes_test(os_handle, list_id, list_name)

    with STEP('Delete created exlusion list'):
        with STEP('Click on exclusions tab'):
            SettingsPage(driver).settings_tabs_panel.exclusions_tab.click()
        with STEP('Click on {} list'.format(list_name)):
            exclusions_tab.left_sidebar.get_list_by_name(list_name).click()
        with STEP('Click "delete list" button'):
            exclusions_tab.about_box.policies_box.delete_list_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Waiting {} seconds'.format(WAITING_TIME)):
            sleep(WAITING_TIME)

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
        path_exclusion_changes_test(os_handle, list_id, 'Global')


