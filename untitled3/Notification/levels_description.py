from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class LevelsContentDescription(BaseElement):
    def __init__(self, parent):
        xpath = "//*[contains(@class, 'content-description') and descendant::*[contains(@class, 'container')]]"
        locator = XPathLocator(xpath)
        super(LevelsContentDescription, self).__init__(locator, parent)

