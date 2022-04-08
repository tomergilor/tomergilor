import random
import string
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

from Scripts import log
from Scripts.Issue import report_issue
from Utils.Timeout import Timeout
from tests.QA.common_functions.agent import is_asset_file_in_agent
from tests.QA.common_functions.management import get_latest_asset_file_path, change_ioc_settings, \
    change_settings_ini_key_and_restart_services


WAITING_TIME = 5


def save_and_validate(driver, policies_tab):
    with STEP('Click Save button'):
        policies_tab.policy_form.save_button.click()
    with STEP('Validate confirmation windows appears'):
        PolicyConfirmationWindow(driver).is_displayed()
    with STEP('Click yes in confirmation window'):
        PolicyConfirmationWindow(driver).yes_btn.click()
    with STEP('Validate Policy updated message appears'):
        if not policies_tab.is_policy_updated_message_appears():
            report_issue(g.issues, 'There is no policy updated message', False)


@slash.tag('no_checks_after_test')
def test_policy_sanity_more_options(agent_ui_machine):
    os_handle = agent_ui_machine.os_handle
    with STEP('Go to policies'):
        driver = g.driver
        login_to_mgmt(driver=driver)

        with STEP('Go to Settings'):
            MainPage(driver).left_side_tabs.settings_tab.click()

        with STEP('Go to policies'):
            if not SettingsPage(driver).settings_tabs_panel.policies_tab.is_selected():
                SettingsPage(driver).settings_tabs_panel.policies_tab.click()

        with STEP('Validate hidden fields'):
            policies_tab = PoliciesTab(driver)
            assert not policies_tab.policy_form.deep_visibility.is_in_dom()

    with STEP('Validate deep visibility ON\OFF option'):
        with STEP('Validate deep visibility on/off option NOT displayed'):
            assert not policies_tab.policy_form.more_options.agent_configuration.deep_visibility.is_displayed()

        with STEP('Set ioc=True in settings.ini and restart services'):
            change_ioc_settings()

        with STEP('Refreshing page'):
            time_to_wait = 60
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

        with STEP('Validate deep visibility on/off option IS displayed'):
            assert policies_tab.policy_form.more_options.agent_configuration.deep_visibility.is_displayed()

    with STEP('Add "?advanced"'):
        change_settings_ini_key_and_restart_services(g.manager.os_handle, 'api', 'support_mode', 'True')
        driver.get(driver.current_url + '?advanced=true')
        with STEP('Validate unhidden checkboxes'):
            deep_vis = policies_tab.policy_form.deep_visibility
            assert deep_vis.is_displayed()
            checkboxes = {"dns": deep_vis.dns_checkbox,
                          "ip": deep_vis.ip_checkbox,
                          "file": deep_vis.file_checkbox,
                          "headers": deep_vis.headers_checkbox,
                          "url": deep_vis.url_checkbox,
                          "process": deep_vis.process_checkbox}

            for key, value in checkboxes.items():
                with STEP('Checking {} element in DOM'.format(key)):
                    assert value.is_in_dom(), "{} checkbox not in DOM".format(key)
                with STEP('Checking {} checkbox selected'.format(key)):
                    assert value.is_on(), "{} checkbox is not checked".format(key)

    with STEP('More options - Containment'):
        assert not policies_tab.policy_form.more_options.disconnect_from_network.is_on()
        policies_tab.policy_form.more_options.disconnect_from_network.set_on()
        assert policies_tab.policy_form.more_options.disconnect_from_network.is_on()
        save_and_validate(driver, policies_tab)
        assert policies_tab.policy_form.more_options.disconnect_from_network.is_on()
        with STEP('Validate by rest API'):
            sleep(WAITING_TIME)
            default_policy_id = g.manager.get_policies()[0]['id']
            policy = g.manager.get_specific_policy(default_policy_id)
            key = 'network_quarantine_on'
            assert policy.get(key) is True, 'Wrong value for {}'.format(key)

    with STEP('Decommission'):
        assert policies_tab.policy_form.more_options.auto_decommission.is_on()
        assert policies_tab.policy_form.more_options.days_offline.get_text() == '21'
        policies_tab.policy_form.more_options.auto_decommission.set_off()
        assert not policies_tab.policy_form.more_options.auto_decommission.is_on()
        policies_tab.policy_form.more_options.days_offline.enter_text('1')
        assert policies_tab.policy_form.more_options.days_offline.get_text() == '1'
        save_and_validate(driver, policies_tab)
        assert not policies_tab.policy_form.more_options.auto_decommission.is_on()
        assert policies_tab.policy_form.more_options.days_offline.get_text() == '1'

        with STEP('Validate by rest API'):
            sleep(WAITING_TIME)
            policy = g.manager.get_specific_policy(default_policy_id)
            assert policy.get('auto_decommission_on') is False
            assert policy.get('auto_decommission_days') is 1

    with STEP('Exclusions'):
        policy_name = ''.join([random.choice(string.lowercase) for i in xrange(10)])
        policy_id = g.manager.create_policy(name=policy_name)['id']
        exclusion_list_name = ''.join([random.choice(string.lowercase) for i in xrange(10)])
        g.manager.create_exclusion_list(name=exclusion_list_name, policies=[policy_id])
        sleep(WAITING_TIME)
        driver.refresh()
        exclusion_list_selector = policies_tab.policy_form.more_options.exclusions.exclusion_list_selector
        assert not exclusion_list_selector.get_selected_value()
        exclusion_list_selector.select_by_text(exclusion_list_name)
        assert exclusion_list_selector.get_selected_value() == exclusion_list_name
        save_and_validate(driver, policies_tab)
        assert exclusion_list_selector.get_selected_value() == exclusion_list_name
        with STEP('Validate by rest API'):
            sleep(WAITING_TIME)
            policy = g.manager.get_specific_policy(default_policy_id)
            excl_list_id = g.manager.get_list_of_exclusion_lists_ids_by_name(exclusion_list_name)[0]
            key = 'exclusion_list_id'
            assert policy.get(key) == excl_list_id, 'Exclusion list was not updated with {}'.format(exclusion_list_name)

    with STEP('Validate agent got asset'):
        sleep(120)  # wait_for_asset()
        asset_id = get_latest_asset_file_path(g.manager.os_handle)
        if not is_asset_file_in_agent(os_handle, asset_id):
            report_issue(g.issues, 'Asset file {} not found in agent'.format(asset_id), False)

    with STEP('Monitoring'):
        log.notice('Currently removed')
        pass

    with STEP("Edit 'Advanced'"):
        for key, value in checkboxes.items():
            value.set_off()
        save_and_validate(driver, policies_tab)
        for key, value in checkboxes.items():
            assert not value.is_on(), "{} checkbox is checked when it shouldn't' to be".format(key)

        with STEP('Validate by rest API'):
            sleep(WAITING_TIME)
            policy = g.manager.get_specific_policy(default_policy_id)
            wrong_params = list()
            for key, value in policy['ioc_attributes'].items():
                if value:
                    wrong_params.append(key)
            assert not wrong_params, 'Wrong params are: {}'.format(wrong_params)

    with STEP('Agent Configuration'):
        agent_conf = policies_tab.policy_form.more_options.agent_configuration
        checkboxes = {'agent ui': agent_conf.agent_ui,
                      'anti tamper': agent_conf.anti_tamper,
                      'deep visibility': agent_conf.deep_visibility,
                      'logging': agent_conf.logging,
                      'snapshots': agent_conf.snapshots,
                      'full disk scan on install': agent_conf.full_disk_scan_on_install}
        for key, value in checkboxes.items():
            with STEP('Validate {} is ON'.format(key)):
                assert value.is_on()
            with STEP('Set {} off'.format(key)):
                value.set_off()
            with STEP('Validate {} is OFF'.format(key)):
                assert not value.is_on()
        save_and_validate(driver, policies_tab)

        with STEP('Validate by rest API'):
            sleep(WAITING_TIME)
            policy = g.manager.get_specific_policy(default_policy_id)
            wrong_params = list()
            for item in ['scan_new_agents', 'agent_ui_on', 'anti_tampering_on',
                         'snapshots_on', 'agent_logging_on', 'ioc']:
                if policy.get(item) is not False:
                    wrong_params.append(item)
            assert not wrong_params, 'Wrong params are: {}'.format(wrong_params)

        # with STEP('Agent side'):
        #     wait_for_asset()
        #     assert is_agent_got_policy_changes(os_handle, 'configure', {'logging': 'false'})
        # assert is_agent_got_policy_changes(os_handle, 'status', {'Self-Protection': 'On'})
        #     process_name = 'AgentUI.exe'
        #     process = os_handle.find_process_by_name(process_name)
        #     assert not process, "{} is running when it shouldn't".format(process_name)

    with STEP('Edit more options'):
        with STEP('Click clear button (clear exclusion)'):
            policies_tab.policy_form.more_options.exclusions.clear_button.click()
        with STEP('Validate no exclusion selected'):
            assert not policies_tab.policy_form.more_options.exclusions.exclusion_list_selector.get_selected_value()
        with STEP(''):
            policies_tab.policy_form.discard_button.click()

    with STEP('Tooltips'):
        tooltips = {"full disk scan on install": agent_conf.full_disk_scan_tooltip,
                    "agent ui": agent_conf.agent_ui_tooltip,
                    "anti tamper": agent_conf.anti_tamper_tooltip,
                    "snapshots": agent_conf.snapshots_tooltip,
                    "logging": agent_conf.logging_tooltip,
                    "deep visibility": agent_conf.deep_visibility_tooltip}
        for key, value in tooltips.items():
            with STEP("Validate {} tooltip".format(key)):
                assert value.is_displayed(), "{} tooltip element not on page".format(key)
                value.hover_mouse_over()
                assert value.is_tooltip_displayed(), "{} tooltip not displayed when mouse on it".format(key)

    with STEP('Discard changes'):
        with STEP('Validate deep visibility is OFF'):
            assert not policies_tab.policy_form.more_options.agent_configuration.deep_visibility.is_on()
        with STEP('Set deep visibility ON'):
            policies_tab.policy_form.more_options.agent_configuration.deep_visibility.set_on()
        with STEP('Validate deep visibility is ON'):
            assert policies_tab.policy_form.more_options.agent_configuration.deep_visibility.is_on()
        with STEP('Click discard changes button'):
            policies_tab.policy_form.discard_button.click()
        with STEP('Validate deep visibility is OFF'):
            assert not policies_tab.policy_form.more_options.agent_configuration.deep_visibility.is_on()
