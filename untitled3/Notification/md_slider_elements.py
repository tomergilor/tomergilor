from selenium.webdriver import ActionChains

from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.utils.actions import find_element
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class MdSlider(BaseElement):
    _values = {'0': 'None', '1': 'Critical', '2': 'Advisory', '3': 'Information'}

    def __init__(self, parent):
        locator = XPathLocator("//md-slider[@*]")
        super(MdSlider, self).__init__(locator, parent)

    def _set_level(self, level):
        slider = find_element(self)
        width = slider.size.get('width')
        move = ActionChains(self.driver)
        move.move_to_element_with_offset(slider, ((width * level) / 100), 0).click()
        move.perform()

    def set_none_level(self):
        self._set_level(5)

    def set_critical_level(self):
        self._set_level(33)

    def set_advisory_level(self):
        self._set_level(66)

    def set_information_level(self):
        self._set_level(95)

    def get_current_level(self):
        value = find_element(self).get_attribute('aria-valuenow')
        return self._values[value]
