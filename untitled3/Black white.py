---------------------------------------------------------------------------------------------------------------------
Black White:
-------------

INIT:

from tests.QA.functionality.management.ui.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui.pages.p_main.black_white_page.list import BlackWhiteList
from tests.QA.functionality.management.ui.pages.p_main.black_white_page.options_items import BlackWhiteFilters
from tests.QA.functionality.management.ui.utils.locator import ClassNameLocator


class BlackWhite(BaseElement):
    def __init__(self, parent):
        locator = ClassNameLocator("bw-container")
        super(BlackWhite, self).__init__(locator, parent)

   def options_items(self):
        return BlackWhiteFilters(self)

   def blackwhite_list(self):
        return BlackWhiteList(self)

   def search(self):
        return Search(self)
----------------------------------------------------------------------------------------------------------------
BASE FILTER:

from tests.QA.functionality.management.ui.page_types.button import Button
from tests.QA.functionality.management.ui.utils.actions import hover, find_elements, find_element
from tests.QA.functionality.management.ui.utils.locator import XPathLocator

from tests.QA.functionality.management.ui.page_types.base_page import BaseElement


class BaseFilter(BaseElement):
    def __init__(self, type, parent):
        locator = XPathLocator("//*[contains(@class, 'mgmt-')]".format(type))
        super(BaseFilter, self).__init__(locator, parent)

   @property
    def content(self):
        return BaseElement(XPathLocator("//*[contains(@class, 'cdk-overlay-')]"), self)

   def hover_mouse_over(self):
        hover(self)

   def get_options_count(self):
        elem = BaseElement(XPathLocator("//div[contains(@class, 'item ng-binding ng-scope')]"), self.content)
        return len(find_elements(elem))

   @property
    def clear_btn(self):
        return Button(XPathLocator("//div[contains(@class, 'item clear-filter')]"), self.content)

   def get_option(self, option):
        return BaseElement(XPathLocator("//*[contains(@class, 'item') and contains(text(), '{}')]".format(option)), self.content)

   def select_option(self, option):
        self.get_option(option).click()

   def select_all(self):
        self.get_option('All').click()

   def is_option_selected(self, option):
        elem = self.get_option(option)
        return 'selected' in find_element(elem).get_attribute('class')
------------------------------------------------------------------------------------------------------------------
list:

from tests.QA.functionality.management.ui.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui.pages.p_main.black_white_page.hash_row_element import HashRow
from tests.QA.functionality.management.ui.utils.actions import find_elements
from tests.QA.functionality.management.ui.utils.locator import IdLocator


class BlackWhiteList(BaseElement):
    def __init__(self, parent):
        locator = ClassNaeLocator("scrollable-content")
        super(BlackWhiteList, self).__init__(locator, parent)

   @property
    def hash_row_element(self):
        return HashRow(self)

   def get_hash_rows_list(self):
        find_elements(self.hash_row)
-----------------------------------------------------------------------------------------------------
Options items:

from tests.QA.functionality.management.ui.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui.pages.p_main.black_white_page.base_filter import BaseFilter
from tests.QA.functionality.management.ui.utils.locator import XPathLocator


class BlackWhiteFilters(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[@class='header']")
        super(BlackWhiteFilters, self).__init__(locator, parent)

   @property
    def OS_filter(self):
        return BaseFilter('administrative ', self)

   @property
    def blackwhite_filter(self):
        return BaseFilter('bnw ', self)

   @property
    def search(self):
        return BaseFilter('search', self)
----------------------------------------------------------------------------------------------------------
