from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class RecipientsContentDescription(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'content-description')]")
        super(RecipientsContentDescription, self).__init__(locator, parent)

