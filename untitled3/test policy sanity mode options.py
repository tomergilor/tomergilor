import slash
from slash import g
from slash_step import STEP
from tests.QA.functionality.management.ui_alhambra.pages.main_page import MainPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page import SettingsPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.policies import PoliciesTab
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.policies.policy_confirmation_window import \
    PolicyConfirmationWindow
from tests.QA.functionality.management.ui_alhambra.tests.ui_utils import login_to_mgmt

from Scripts.Issue import report_issue
from tests.QA.common_functions.agent import is_agent_got_policy_changes
from tests.QA.common_functions.management import wait_for_asset, change_settings_ini_key_and_restart_services


@slash.tag('no_checks_after_test')
def test_policy_sanity_mode_options(agent_ui_machine):

    with STEP('Policy mode options'):
        with STEP('Go to policies'):
            driver = g.driver
            login_to_mgmt(driver=driver)

            with STEP('Go to Settings'):
                MainPage(driver).left_side_tabs.settings_tab.click()

            with STEP('Go to policies'):
                if not SettingsPage(driver).settings_tabs_panel.policies_tab.is_selected():
                    SettingsPage(driver).settings_tabs_panel.policies_tab.click()

            with STEP('Validate default values'):  # with STEP(''):
                policies_tab = PoliciesTab(driver)
                with STEP('Validate detect checkbox of threats not selected'):
                    assert not policies_tab.policy_form.policy_mode_options.threats.is_detect_selected()
                with STEP('Validate protect checkbox of suspicious is enabled'):
                    assert policies_tab.policy_form.policy_mode_options.suspicious.protect_checkbox.is_enabled()
                with STEP('Validate detect checkbox of suspicious is selected'):
                    assert policies_tab.policy_form.policy_mode_options.suspicious.detect_checkbox.is_checked()
                with STEP('Validate agent notifications checkbox is selected'):
                    assert policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.is_checked()

    with STEP('Edit Policy mode options'):
        policies_tab.policy_form.policy_mode_options.threats.detect_checkbox.check()
        assert not policies_tab.policy_form.policy_mode_options.suspicious.protect_checkbox.is_enabled()
        assert policies_tab.policy_form.policy_mode_options.suspicious.is_detect_selected()

        policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.uncheck()
        assert not policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.is_checked()
        policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.check()
        assert policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.is_checked()

        policies_tab.policy_form.policy_mode_options.threats.protect_checkbox.check()
        policies_tab.policy_form.policy_mode_options.suspicious.protect_checkbox.check()

        policies_tab.policy_form.save_button.click()

        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

        with STEP("Validate changes has been saved"):
            assert policies_tab.policy_form.policy_mode_options.threats.protect_checkbox.is_checked()
            assert policies_tab.policy_form.policy_mode_options.suspicious.protect_checkbox.is_checked()

    with STEP('Adding advanced=true to url'):
        change_settings_ini_key_and_restart_services(g.manager.os_handle, 'api', 'support_mode', 'True')
        driver.get(driver.current_url + '?advanced=true')

        with STEP('Verify there are additional protect levels - Remidiate and Rollback.'):
            assert policies_tab.policy_form.protect_level_options.is_displayed()
            assert policies_tab.policy_form.protect_level_options.kill_and_quarantine.is_displayed()
            assert policies_tab.policy_form.protect_level_options.remediate.is_displayed()
            assert policies_tab.policy_form.protect_level_options.rollback.is_displayed()

    with STEP("Edit 'Advanced'"):
        policies_tab.policy_form.protect_level_options.rollback.check()
        policies_tab.policy_form.save_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

        with STEP('Validate changes has been saved'):
            assert policies_tab.policy_form.protect_level_options.rollback.is_checked()

    with STEP('Agent side'):
        os_handle = agent_ui_machine.os_handle
        with STEP('Wait for asset'):
            wait_for_asset()

        if not is_agent_got_policy_changes(os_handle, 'configure', {"OnValidate ": "PromotetoMitigate"}):
            report_issue(g.issues, 'Agent did not got policy changes for OnValidate', False)
        if not is_agent_got_policy_changes(os_handle, 'status', {"Mitigation policy": "rollbackThreat"}):
            report_issue(g.issues, 'Agent did not got policy changes for Mitigation policy', False)

    with STEP("Set all off"):
        policies_tab.policy_form.policy_mode_options.threats.detect_checkbox.check()
        policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.uncheck()

        policies_tab.policy_form.save_button.click()

        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

        assert policies_tab.policy_form.policy_mode_options.threats.is_detect_selected()
        assert policies_tab.policy_form.policy_mode_options.suspicious.is_detect_selected()
        assert not policies_tab.policy_form.policy_mode_options.agent_notification_on_suspicious.is_checked()

    with STEP('Agent side'):
        with STEP('Wait for asset'):
            wait_for_asset()

        if not is_agent_got_policy_changes(os_handle, 'configure', {"OnValidate ": "reportToMgmt"}):
            report_issue(g.issues, 'Agent did not got policy changes for OnValidate', False)
        if not is_agent_got_policy_changes(os_handle, 'status', {"Mitigation policy": "none"}):
            report_issue(g.issues, 'Agent did not got policy changes for Mitigation policy', False)

    with STEP('Set threats - protect and level rollback'):
        policies_tab.policy_form.policy_mode_options.threats.protect_checkbox.check()
        assert policies_tab.policy_form.protect_level_options.is_in_dom()
        policies_tab.policy_form.protect_level_options.rollback.check()
        policies_tab.policy_form.save_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

    with STEP('Discard changes'):
        policies_tab.policy_form.protect_level_options.remediate.click()
        assert policies_tab.policy_form.protect_level_options.remediate.is_checked()
        assert not policies_tab.policy_form.protect_level_options.rollback.is_checked()
        policies_tab.policy_form.policy_mode_options.suspicious.protect_checkbox.check()
        assert policies_tab.policy_form.policy_mode_options.suspicious.protect_checkbox.is_checked()

        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).ok_btn.click()

        policies_tab.policy_form.discard_button.click()

        assert policies_tab.policy_form.protect_level_options.rollback.is_checked()
        assert policies_tab.policy_form.protect_level_options.remediate.is_checked()
        assert policies_tab.policy_form.policy_mode_options.suspicious.detect_checkbox.is_checked()
        assert policies_tab.policy_form.policy_mode_options.suspicious.detect_checkbox.is_checked()

    driver.quit()
