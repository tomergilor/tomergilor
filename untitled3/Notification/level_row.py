from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.notifications_page.md_slider_element import \
    MdSlider
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class LevelRow(BaseElement):
    def __init__(self, label, parent):
        locator = XPathLocator(
            "//*[@class='row' and descendant::*[contains(@class, 'notification-label') and contains(text(), '{}')]]".format(
                label))
        super(LevelRow, self).__init__(locator, parent)

    @property
    def slider(self):
        return MdSlider(self)

