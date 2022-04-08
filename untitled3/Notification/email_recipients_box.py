from tests.QA.functionality.management.ui_alhambra.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.base_recipients import \
    BaseRecipients
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class EmailRecipients(BaseRecipients):
    def __init__(self, parent):
        xpath = "//*[@class='row' and descendant::input[contains(@placeholder, 'Enter email addresses')]]"
        locator = XPathLocator(xpath)
        super(EmailRecipients, self).__init__(locator, parent)

    @property
    def mail_input_textbox(self):
        return TextBox(XPathLocator("//input[contains(@placeholder, 'Enter email addresses')]"), self)
