from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.level_row import LevelRow
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class NotificationLevelPanel(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'notification-level-panel')]")
        super(NotificationLevelPanel, self).__init__(locator, parent)

    @property
    def sms_level_row(self):
        return LevelRow('SMS', self)

    @property
    def email_level_row(self):
        return LevelRow('Email', self)

    @property
    def syslog_level_row(self):
        return LevelRow('Syslog', self)

