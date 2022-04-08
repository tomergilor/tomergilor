import random
import string
import time
import slash

from datetime import datetime
from pip.compat import total_seconds
from selenium.webdriver.common.keys import Keys
from slash import g
from slash_step import STEP
from tests.QA.functionality.management.ui_alhambra.pages.main_page import MainPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page import SettingsPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.policies import PoliciesTab
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.policies.policy_confirmation_window import \
    PolicyConfirmationWindow
from tests.QA.functionality.management.ui_alhambra.tests.ui_utils import login_to_mgmt
from tests.QA.functionality.management.ui_alhambra.utils.services import Services

from Scripts import Config
from Scripts import log
from Scripts.OSHandle import OSHandle


def get_time_diff(date_str, timestamp):
    time_diff = diff_between_comps()
    x = datetime.utcfromtimestamp(timestamp)
    y = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
    return abs(total_seconds(y - x) - time_diff)


def diff_between_comps():
    browser_os_handle = OSHandle(Config.selenium_node)
    browser_now = browser_os_handle.modules.datetime.datetime.now()
    exec_now = datetime.utcnow()
    browser_time = time.mktime(browser_now.timetuple())
    exec_time = time.mktime(exec_now.timetuple())
    return browser_time - exec_time


# @slash.requires((get_mgmt_version().lower() >= 'a'))  ToDo: Implement
@slash.tag('no_checks_after_test')
def test_policy_sanity_general_test(mgmt_ui_machine):

    with STEP('Go to policies'):
        driver = g.driver
        login_to_mgmt(driver=driver)

        with STEP('Go to Settings'):
            MainPage(driver).left_side_tabs.settings_tab.click()

        with STEP('Go to policies'):
            if not SettingsPage(driver).settings_tabs_panel.policies_tab.is_selected():
                SettingsPage(driver).settings_tabs_panel.policies_tab.click()

    with STEP('Buttons'):
        policies_tab = PoliciesTab(driver)
        with STEP('Check Duplicate button appears'):
            assert policies_tab.toolbar_buttons.duplicate_btn.is_enabled()

        with STEP('Check Delete button appears'):
            assert policies_tab.toolbar_buttons.delete_btn.is_enabled()

        with STEP('Check "new policy" button appears'):
            assert policies_tab.list_sidebar.new_policy_btn.is_enabled()

    with STEP('Lists'):
        with STEP('Validate "all policies" title appears'):
            assert policies_tab.list_sidebar.all_policies.is_enabled()
        with STEP('Validate "Default" policy appears'):
            assert policies_tab.list_sidebar.policy_by_name('Default').is_enabled()

    with STEP('Add/delete/edit/duplicate policies'):
        suffix = ''.join([random.choice(string.lowercase) for i in xrange(6)])
        new_policy_name = 'test_{}'.format(suffix)
        with STEP('Create new policy with "{}" name'.format(new_policy_name)):
            with STEP('Validate discard button not in DOM'):
                assert not policies_tab.policy_form.discard_button.is_in_dom()
            with STEP('Click "new policy" button'):
                policies_tab.list_sidebar.new_policy_btn.click()
            with STEP('Validate discard button is enabled'):
                assert policies_tab.policy_form.discard_button.is_enabled()
            with STEP('Enter policy name "{}"'.format(new_policy_name)):
                policies_tab.policy_form.policy_summary.policy_name_edit_btn.click()
                policies_tab.policy_form.policy_summary.policy_name.enter_text(new_policy_name)
            with STEP('Click save button'):
                policies_tab.policy_form.save_button.click()
                time.sleep(2)
            with STEP('Validate {} policy appears in DOM'.format(new_policy_name)):
                assert policies_tab.list_sidebar.policy_by_name(new_policy_name).is_in_dom()
            with STEP('Enter policy name "{}"'.format(new_policy_name + ' 2')):
                policies_tab.policy_form.policy_summary.policy_name_edit_btn.click()
                policies_tab.policy_form.policy_summary.policy_name.enter_text(new_policy_name + ' 2')
            with STEP('Click "Discard" button'):
                policies_tab.policy_form.discard_button.click()
            with STEP('Validate discard button not in DOM'):
                assert not policies_tab.policy_form.discard_button.is_in_dom()

        with STEP('Edit created policy'):
            new_off_days_value = '20'
            with STEP('Change "days offline" value to {}'.format(new_off_days_value)):
                policies_tab.policy_form.more_options.days_offline.enter_text(new_off_days_value)
            with STEP('Click Save button'):
                policies_tab.policy_form.save_button.click()
            with STEP('Validate confirmation windows appears'):
                PolicyConfirmationWindow(driver).is_displayed()
            with STEP('Click yes in confirmation window'):
                PolicyConfirmationWindow(driver).yes_btn.click()
            with STEP('Validate Policy updated message appears'):
                assert policies_tab.is_policy_updated_message_appears(), 'There is no policy updated message'
            with STEP('Validate "Days offline" value changed to {}'.format(new_off_days_value)):
                assert policies_tab.policy_form.more_options.days_offline.get_text() == new_off_days_value, ''

        with STEP('Delete created policy'):
            with STEP('Validate created policy is selected'):
                assert policies_tab.list_sidebar.get_selected_policy_name() == new_policy_name
            with STEP('Click Delete button'):
                policies_tab.toolbar_buttons.delete_btn.click()
            with STEP('Validate confirmation windows appears'):
                PolicyConfirmationWindow(driver).is_displayed()
            with STEP('Click yes in confirmation window'):
                PolicyConfirmationWindow(driver).ok_btn.click()
            with STEP('Validate Policy deleted message appears'):
                assert policies_tab.is_policy_updated_message_appears()
            with STEP('Validate "{}" policy not in DOM'.format(new_policy_name)):
                time.sleep(3)
                assert not policies_tab.list_sidebar.policy_by_name(new_policy_name).is_in_dom()

        with STEP('Duplicate default policy'):
            with STEP('Select default policy'):
                policies_tab.list_sidebar.policy_by_name("Default").click()
                assert policies_tab.list_sidebar.get_selected_policy_name() == 'Default'
            with STEP('Click duplicate button'):
                policies_tab.toolbar_buttons.duplicate_btn.click()
            with STEP('Enter policy name "{}"'.format(new_policy_name)):
                policies_tab.policy_form.policy_summary.policy_name_edit_btn.click()
                policies_tab.policy_form.policy_summary.policy_name.enter_text(new_policy_name)
            with STEP('Click Save button'):
                policies_tab.policy_form.save_button.click()
            with STEP('Validate created policy in DOM'):
                assert policies_tab.list_sidebar.policy_by_name(new_policy_name).is_in_dom()

    with STEP('Long name'):
        log.notice("There is no way to check it with selenium")
        pass

    with STEP('Empty name'):
        with STEP('Click "new policy"'):
            policies_tab.list_sidebar.new_policy_btn.click()
        with STEP('Clear name'):
            policies_tab.policy_form.policy_summary.policy_name_edit_btn.click()
            policies_tab.policy_form.policy_summary.policy_name.enter_text("a")
            policies_tab.policy_form.policy_summary.policy_name.enter_text(Keys.ARROW_LEFT, clear_before=False)
            policies_tab.policy_form.policy_summary.policy_name.enter_text(Keys.DELETE, clear_before=False)
        with STEP('Validate invalid name message appears'):
            assert not policies_tab.policy_form.policy_summary.is_policy_name_valid()
        with STEP('Press discard button'):
            policies_tab.policy_form.policy_summary.policy_name.enter_text("a")
            policies_tab.policy_form.discard_button.click()

    with STEP('Scrolling '):

        with STEP('Get time before creating policies'):
            timestamp = time.time()

        prefix = ''.join([random.choice(string.lowercase) for i in xrange(10)])
        with STEP("Creating 20 policies with {} prefix".format(prefix)):
            name = None
            for i in range(1, 21):
                name = prefix + str(i)
                with STEP('Creating policy with name {name}'.format(name=name)):
                    g.manager.create_policy(name=name)

        with STEP("Refresh page"):
            driver.refresh()

        with STEP("Click More items"):
            with STEP('Validate policy {} not displayed'.format(name)):
                assert not policies_tab.list_sidebar.policy_by_name(name).is_displayed(), "Policy {} displayed".format(name)
            with STEP('Press "more items"'):
                policies_tab.list_sidebar.more_items.click()
            with STEP('Validate policy displayed'.format(name)):
                assert policies_tab.list_sidebar.policy_by_name(name).is_displayed(), "Policy {} not displayed".format(name)

        with STEP("Check scrolling"):
            # ToDo: Add check that last policy not on screen  (https://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport/7557433#7557433)
            Services(driver).scroll_to_view(policies_tab.list_sidebar.policy_by_name(name))
            # ToDo: Add check that last policy on screen

    with STEP('Policy information'):
        with STEP('Select default policy'):
            policies_tab.list_sidebar.policy_by_name("Default").click()
        with STEP('Validate policy name == "Default"'):
            policies_tab.policy_form.policy_summary.policy_name_edit_btn.click()
            assert policies_tab.policy_form.policy_summary.policy_name.get_text() == 'Default'  #ToDo: add assertion messages
        with STEP('Validate group == "Default group"'):
            assert policies_tab.policy_form.policy_summary.groups.get_text() == 'Default group'
        with STEP('Validate creator = "System"'):
            assert policies_tab.policy_form.policy_summary.creator.get_text() == 'System'
        with STEP('Validate source == Default'):
            assert policies_tab.policy_form.policy_summary.source.get_text() == 'Default'

        with STEP('Select {} policy'.format(prefix + '1')):
            policies_tab.list_sidebar.policy_by_name(prefix + '1').click()
            appear_time = policies_tab.policy_form.policy_summary.date_time.get_text()

        with STEP('Validate time in browser in format "%m/%d/%y %H:%M:%S" and '
                  'diff between policy creation time (appears in browser) and '
                  'time taken before policy creation is less then 30 seconds'):
            assert get_time_diff(appear_time, timestamp) < 30

    driver.quit()