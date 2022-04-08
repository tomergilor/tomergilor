from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.email_recipients_box import \
    EmailRecipients
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.sms_recipients_box import \
    SmsRecipients
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class RecipientsContentData(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'content-data')]")
        super(RecipientsContentData, self).__init__(locator, parent)

    @property
    def sms_recipients(self):
        return SmsRecipients(self)

    @property
    def email_recipients(self):
        return EmailRecipients(self)

