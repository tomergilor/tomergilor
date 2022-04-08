from time import sleep

import slash
from slash import g
from slash_step import STEP
from tests.QA.functionality.management.ui_alhambra.pages.login_page import LoginPage
from tests.QA.functionality.management.ui_alhambra.pages.main_page import MainPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page import SettingsPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.policies import PoliciesTab
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.policies.policy_confirmation_window import \
    PolicyConfirmationWindow
from tests.QA.functionality.management.ui_alhambra.tests.ui_utils import login_to_mgmt

from Scripts.Issue import report_issue
from Utils.Timeout import Timeout
from tests.QA.common_functions.agent import is_engine_status_on
from tests.QA.common_functions.management import wait_for_asset, get_mgmt_policy_specific_field, change_ioc_settings, \
    change_settings_ini_key_and_restart_services



@slash.tag('no_checks_after_test')
def test_policy_sanity_engines(agent_ui_machine):
    os_handle = agent_ui_machine.os_handle
    with STEP('Go to policies'):
        driver = g.driver
        login_to_mgmt(driver=driver)

        with STEP('Go to Settings'):
            MainPage(driver).left_side_tabs.settings_tab.click()

        with STEP('Go to policies'):
            if not SettingsPage(driver).settings_tabs_panel.policies_tab.is_selected():
                SettingsPage(driver).settings_tabs_panel.policies_tab.click()

        with STEP('Validate hidden engine'):
            assert not PoliciesTab(driver).policy_form.engines.intrusion_detection.is_in_dom()

    with STEP('Add "?advanced"'):
        change_settings_ini_key_and_restart_services(g.manager.os_handle, 'api', 'support_mode', 'True')
        driver.get(driver.current_url + '?advanced=true')

    with STEP('Validate unhidden engine'):
        assert PoliciesTab(driver).policy_form.engines.intrusion_detection.is_in_dom()
        assert PoliciesTab(driver).policy_form.engines.intrusion_detection.is_enabled()
        assert not PoliciesTab(driver).policy_form.engines.intrusion_detection.is_on()

    with STEP("Edit 'Advanced'"):
        policies_tab = PoliciesTab(driver)
        engns = policies_tab.policy_form.engines

        with STEP('Validate reputation ON and disabled'):
            assert engns.reputation.is_on()
            assert not engns.reputation.is_enabled()

        engines = {'dfi': engns.dfi,
                   'dfi_suspicious': engns.dfi_suspicious,
                   'dbt_executables': engns.dbt_executables,
                   'potentially_unwanted_applications': engns.potentially_unwanted_applications,
                   'documents_scripts': engns.documents_scripts,
                   'exploits': engns.exploits,
                   'lateral_movements': engns.lateral_movements
                   }

        for key, value in engines.items():
            with STEP('Validate {} is ON'.format(key)):
                assert value.is_on()
            with STEP('Set {} off'.format(key)):
                value.set_off()
            with STEP('Click OK button on confirmation windows for {}'.format(key)):
                PolicyConfirmationWindow(driver).yes_btn.click()
            with STEP('Validate {} is OFF'.format(key)):
                assert not value.is_on()
        with STEP('Click Save button'):
            policies_tab.policy_form.save_button.click()

        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

        with STEP("Validate changes has been saved"):
            for key, value in engines.items():
                with STEP('Validate {} is OFF'.format(key)):
                    assert not value.is_on()

    # with STEP('Validate Settings wheel does not appear'):
    #     assert not policies_tab.policy_form.engines.settings_btn.is_in_dom()

    with STEP('Set ioc=True in settings.ini and restart services'):
        change_ioc_settings()

    time_to_wait = 60
    with STEP('Refreshing page every 5 seconds due {} seconds. Expect to see login page'.format(time_to_wait)):
        timeout = Timeout(time_to_wait)
        is_loaded = False
        while not is_loaded and not timeout.is_expired():
            sleep(5)
            driver.refresh()
            if LoginPage(driver).is_displayed():
                is_loaded = True
        assert is_loaded, 'Login page still not displayed with refresh after {} seconds'.format(time_to_wait)

    login_to_mgmt(driver=driver)

    with STEP('Go to Settings'):
        MainPage(driver).left_side_tabs.settings_tab.click()

    with STEP('Go to policies'):
        if not SettingsPage(driver).settings_tabs_panel.policies_tab.is_selected():
            SettingsPage(driver).settings_tabs_panel.policies_tab.click()

    with STEP('Add "?advanced"'):
        driver.get(driver.current_url + '?advanced=true')

    with STEP('Properties'):
        with STEP('Click settings button'):
            policies_tab.policy_form.engines.settings_btn.click()
        with STEP('Validate monitoring window is displayed'):
            assert policies_tab.policy_form.engines.monitoring_box.is_displayed()
        with STEP('Uncheck on write checkbox'):
            policies_tab.policy_form.engines.monitoring_box.on_write.uncheck()
        with STEP('Validate Confirmation Window displayed'):
            assert PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click OK button'):
            PolicyConfirmationWindow(driver).ok_btn.click()
        with STEP('Validate dfi disabled'):
            assert not engns.dfi.is_enabled()
        with STEP('Validate dfi OFF'):
            assert not engns.dfi.is_on()
        with STEP('Validate dfi-suspicious disabled'):
            assert not engns.dfi_suspicious.is_enabled()
        with STEP('Validate dfi-suspicious OFF'):
            assert not engns.dfi.is_on()
        with STEP('Click Settings button'):
            policies_tab.policy_form.engines.settings_btn.click()
        with STEP('Validate monitoring window is displayed'):
            assert policies_tab.policy_form.engines.monitoring_box.is_displayed()
        with STEP('Uncheck on execute checkbox'):
            policies_tab.policy_form.engines.monitoring_box.on_execute.uncheck()
        with STEP('Validate Confirmation Window displayed'):
            assert PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click OK button'):
            PolicyConfirmationWindow(driver).ok_btn.click()
        with STEP('Validate dbt disabled'):
            assert not engns.dbt_executables.is_enabled()
        with STEP('Validate documents scripts disabled'):
            assert not engns.documents_scripts.is_enabled()
        with STEP('Validate lateral movements disabled'):
            assert not engns.lateral_movements.is_enabled()
        with STEP('Validate pup disabled'):
            assert not engns.potentially_unwanted_applications.is_enabled()
        with STEP('Validate exploit disabled'):
            assert not engns.exploits.is_enabled()
        with STEP('Validate intrusion detection disabled'):
            assert not engns.intrusion_detection.is_enabled()

        with STEP('Click Save button'):
            policies_tab.policy_form.save_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

    with STEP('Agent side'):
        wait_for_asset()
        # assert is_agent_got_policy_changes(os_handle, 'configure', {"monitorBehavioralEvents ": "??????"})

        eng = 'reputation'
        if not is_engine_status_on(os_handle, eng):
            report_issue(g.issues, 'Agent status of {} is OFF, when expected to be ON'.format(eng), False)
        for engine in ['preExecution', 'preExecutionSuspicious', 'executables', 'dataFiles',
                       'exploits', 'penetration', 'fileLess', 'lateralMovement']:
            if is_engine_status_on(os_handle, engine):
                report_issue(g.issues, 'Agent status of {} is ON, when expected to be OFF'.format(engine), False)

    with STEP('Validate in mgmt by Rest call'):
        assert not get_mgmt_policy_specific_field('monitor_on_execute')
        assert not get_mgmt_policy_specific_field('monitor_on_write')

    with STEP('Turn engines on'):
        with STEP('Click settings button'):
            policies_tab.policy_form.engines.settings_btn.click()
        with STEP('Validate monitoring window enabled'):
            assert policies_tab.policy_form.engines.monitoring_box.is_enabled()
        with STEP('Check on execute checkbox'):
            policies_tab.policy_form.engines.monitoring_box.on_execute.check()

        engines = {'dbt_executables': engns.dbt_executables,
                   'potentially_unwanted_applications': engns.potentially_unwanted_applications,
                   'documents_scripts': engns.documents_scripts,
                   'exploits': engns.exploits,
                   'lateral_movements': engns.lateral_movements,
                   'Intrusion Detection': engns.intrusion_detection
                   }
        for key, value in engines.items():
            with STEP('Validate {} is OFF'.format(key)):
                assert not value.is_on()
            with STEP('Set {} ON'.format(key)):
                value.set_on()
            with STEP('Validate {} is ON'.format(key)):
                assert value.is_on()

        with STEP('Click Save button'):
            policies_tab.policy_form.save_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

        with STEP('Wait for asset to arrive'):
            wait_for_asset()

        # assert is_agent_got_policy_changes(os_handle, 'configure', {"monitorBehavioralEvents ": "??????"})

        for engine in ['preExecution', 'preExecutionSuspicious']:
            if is_engine_status_on(os_handle, engine):
                report_issue(g.issues, 'Agent status of {} is ON, when expected to be OFF'.format(engine), False)

        for engine in ['reputation', 'executables', 'dataFiles', 'exploits',
                       'penetration', 'fileLess', 'lateralMovement']:
            if not is_engine_status_on(os_handle, engine):
                report_issue(g.issues, 'Agent status of {} is OFF, when expected to be ON'.format(engine), False)

    with STEP('Turn all engines on'):
        with STEP('Click settings button'):
            policies_tab.policy_form.engines.settings_btn.click()
        with STEP('Validate monitoring window enabled'):
            assert policies_tab.policy_form.engines.monitoring_box.is_enabled()
        with STEP('Check on write checkbox'):
            policies_tab.policy_form.engines.monitoring_box.on_write.check()

        engines = {'dfi': engns.dfi,
                   'dfi suspicious': engns.dfi_suspicious}
        for key, value in engines.items():
            with STEP('Validate {} is OFF'.format(key)):
                assert not value.is_on()
            with STEP('Set {} ON'.format(key)):
                value.set_on()
            with STEP('Validate {} is ON'.format(key)):
                assert value.is_on()

        with STEP('Click Save button'):
            policies_tab.policy_form.save_button.click()
        with STEP('Validate confirmation windows appears'):
            PolicyConfirmationWindow(driver).is_displayed()
        with STEP('Click yes in confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate Policy updated message appears'):
            assert policies_tab.is_policy_updated_message_appears()

        with STEP('Wait for asset to arrive'):
            wait_for_asset()

        # assert is_agent_got_policy_changes(os_handle, 'configure', {"monitorBehavioralEvents ": "??????"})

        for engine in ['preExecution', 'preExecutionSuspicious', 'reputation', 'executables',
                       'dataFiles', 'exploits', 'penetration', 'fileLess', 'lateralMovement']:
            if not is_engine_status_on(os_handle, engine):
                report_issue(g.issues, 'Agent status of {} is OFF, when expected to be ON'.format(engine), False)

    with STEP('Discard changes'):
        with STEP('Validate dfi engine ON'):
            assert engns.dfi.is_on()
        with STEP('Set dfi engine OFF'):
            engns.dfi.set_off()
        with STEP('Click yes button on confirmation window'):
            PolicyConfirmationWindow(driver).yes_btn.click()
        with STEP('Validate dfi OFF'):
            assert not engns.dfi.is_on()
        with STEP('Click discard button'):
            policies_tab.policy_form.discard_button.click()
        with STEP('Validate dfi ON'):
            assert engns.dfi.is_on()
