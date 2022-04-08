from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.advanced_level import \
    AdvancedPanel
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.levels_description import \
    LevelsContentDescription
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.notification_level import \
    NotificationLevelPanel
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class LevelsTab(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-notifications-levels[@*]")
        super(LevelsTab, self).__init__(locator, parent)

    @property
    def notification_level_panel(self):
        return NotificationLevelPanel(self)

    @property
    def advanced_panel(self):
        return AdvancedPanel(self)

    @property
    def content_description(self):
        return LevelsContentDescription(self)

    @property
    def save_button(self):
        return Button(XPathLocator("//span[contains(text(), 'Save')]"), self)

    @property
    def discard_button(self):
        return Button(XPathLocator("//*[contains(text(), 'discard changes')]"), self)

    @property
    def reset_button(self):
        return Button(XPathLocator("//*[contains(text(), 'reset')]"), self)

    def collapse_advanced(self):
        if self.is_advanced_expanded():
            elem = BaseElement(XPathLocator("//*[contains(@class, 'advanced-panel-title')]"), self)
            elem.click()

    def expand_advanced(self):
        if not self.is_advanced_expanded():
            elem = BaseElement(XPathLocator("//*[contains(@class, 'advanced-panel-title')]"), self)
            elem.click()

    def is_advanced_expanded(self):
        elem = BaseElement(XPathLocator("//*[contains(@class, 'advanced-panel-title active')]"), self)
        return elem.is_in_dom()
