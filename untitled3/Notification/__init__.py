from tests.QA.functionality.management.ui_alhambra.page_types.base_page import TopLevelPage
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.page_types.tab import TopTab
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.levels_page import LevelsTab
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.recipients_page import \
    RecipientsTab
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class NotificationsTab(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//mgmt-notifications[@*]")
        super(NotificationsTab, self).__init__(driver, locator)

    @property
    def levels_tab(self):
        return TopTab('LEVELS', self)

    @property
    def levels_tab_content(self):
        return LevelsTab(self)

    @property
    def recipients_tab(self):
        return TopTab('RECIPIENTS', self)

    @property
    def recipients_tab_content(self):
        return RecipientsTab(self)

    @property
    def save_button(self):
        return Button(XPathLocator("//span[contains(text(), 'Save')]"), self)

    @property
    def discard_button(self):
        return Button(XPathLocator("//*[contains(text(), 'discard changes')]"), self)