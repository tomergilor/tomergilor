import abc

from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.utils.actions import find_elements
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class BaseRecipients(BaseElement):
    __metaclass__ = abc.ABCMeta

    def __init__(self, locator, parent):
        super(BaseRecipients, self).__init__(locator, parent)

    def get_existing_items_list(self):
        chip_item = BaseElement(XPathLocator("//*[contains(@class, 'chip-item')]"), self)
        elements = find_elements(chip_item)
        items = list()
        for element in elements:
            current_num = element.text.partition('\n')[0]
            items.append(current_num)
        return items

    def is_element_present(self, text):
        elem = BaseElement(XPathLocator("//*[contains(@class, 'chip-item') and contains(text(), '{}')]".format(text)),
                           self)
        return elem.is_in_dom()

    def delete_number(self, number):
        chip_item = BaseElement(
            XPathLocator("//*[contains(@class, 'chip-item') and contains(text(), '{}')]".format(number)), self)
        chip_close = BaseElement(XPathLocator("//span[contains(@class, 'chip-close')]"), chip_item)
        chip_close.click()
