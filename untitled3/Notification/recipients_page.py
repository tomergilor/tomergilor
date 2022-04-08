from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.recipients_data import \
    RecipientsContentData
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.recipients_description import \
    RecipientsContentDescription
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class RecipientsTab(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-notifications-recipients[@*]")
        super(RecipientsTab, self).__init__(locator, parent)

    @property
    def content_data(self):
        return RecipientsContentData(self)

    @property
    def content_description(self):
        return RecipientsContentDescription(self)

    @property
    def save_button(self):
        return Button(XPathLocator("//span[contains(text(), 'Save')]"), self)

    @property
    def discard_button(self):
        return Button(XPathLocator("//*[contains(text(), 'discard changes')]"), self)

