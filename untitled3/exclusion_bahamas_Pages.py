## __init__
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import TopLevelPage
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.about import ExclusionAboutBox
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.exclusion_grid_element import \
    ExclusionGrid
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.exclusion_header_element import \
    ExclusionHeader
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.exclusion_type_box_element import \
    ExclusionTypeBox
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.exclusions_left_side_bar import \
    LeftSideBar
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class ExclusionsTab(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//mgmt-exclusion[@*]")
        super(ExclusionsTab, self).__init__(driver, locator)

    @property
    def left_sidebar(self):
        return LeftSideBar(self)

    @property
    def header(self):
        return ExclusionHeader(self)

    @property
    def type_box(self):
        return ExclusionTypeBox(self)

    @property
    def about_box(self):
        return ExclusionAboutBox(self)

    @property
    def exclusion_grid(self):
        return ExclusionGrid(self)

## About:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.policies_box_element import \
    PoliciesBox
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class ExclusionAboutBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[@* and descendant::*[contains(@class, 'about-exclusion-list-box')]]")
        super(ExclusionAboutBox, self).__init__(locator, parent)

    @property
    def title(self):
        return TextElement(XPathLocator("//h4[@*]"), self)

    @property
    def list_name(self):
        return TextElement(XPathLocator(
            "//span[@class='value' and ancestor::li[@* and descendant::span[contains(text(), 'List name')]]]"), self)

    @property
    def edit_name_button(self):
        return BaseElement(XPathLocator("//a[@* and descendant::i[contains(@class, 'mgmt-edit')]]"), self)

    @property
    def created_at(self):
        return TextElement(XPathLocator(
            "//span[@class='value' and ancestor::li[@* and descendant::span[contains(text(), 'Created at')]]]"), self)

    @property
    def creator(self):
        return TextElement(XPathLocator("//mgmt-user[@*]"), self)

    @property
    def policies_box(self):
        return PoliciesBox(self)

## Edit exclusion page:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement, TopLevelPage
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.page_types.md_check_box import MdCheckBox
from tests.QA.functionality.management.ui_bahamas.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.new_exclusion_page import \
    OSDropDownSelector
from tests.QA.functionality.management.ui_bahamas.utils.actions import NoSuchElementException
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class EditExclusionDialog(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//md-dialog-container[@*]")
        super(EditExclusionDialog, self).__init__(driver, locator)

    @property
    def os_selector(self):
        text_box_element = TextBox(XPathLocator("//md-select[@placeholder='OS']"), self)
        return OSDropDownSelector(self.driver, text_box_element)

    @property
    def path(self):
        return TextBox(XPathLocator("//input[contains(@placeholder, 'Path')]"), self)

    @property
    def include_subfolders_checkbox(self):
        locator = XPathLocator("//*[@formcontrolname='includeSubfolders']")
        return MdCheckBox(partial_id=None, parent=self, locator=locator)

    @property
    def inject_checkbox(self):
        locator = XPathLocator("//*[@formcontrolname='inject']")
        return MdCheckBox(partial_id=None, parent=self, locator=locator)

    @property
    def description(self):
        return TextBox(XPathLocator("//input[contains(@placeholder, 'Description')]"), self)

    @property
    def cansel_btn(self):
        return Button(XPathLocator("//span[contains(text(), 'Cancel')]"), self)

    @property
    def save_btn(self):
        return Button(XPathLocator("//span[(text()='Save')]"), self)

    @property
    def as_change_btn(self):
        return Button(XPathLocator("//a[(text()='Change')]"), self)

    def is_as_file(self):
        if BaseElement(XPathLocator("//span[(text()='As Folder')]"), self).is_in_dom():
            return False
        elif BaseElement(XPathLocator("//span[(text()='As File')]"), self).is_in_dom():
            return True
        else:
            raise NoSuchElementException()

## Edit List:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement, TopLevelPage
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_bahamas.utils.actions import find_element
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class EditListDialog(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//md-dialog-container[@*]")
        super(EditListDialog, self).__init__(driver, locator)

    @property
    def list_name(self):
        return TextBox(XPathLocator("//input[contains(@placeholder, 'Name')]"), self)

    @property
    def save_button(self):
        return Button(XPathLocator("//span[contains(text(), 'Save')]"), self)

    @property
    def cancel_button(self):
        return Button(XPathLocator("//*[contains(text(), 'Cancel')]"), self)

    def select_by_name(self, name):
        if not self.is_selected(name):
            self._get_row_by_policy_name(name).click()

    def unselect_by_name(self, name):
        if self.is_selected(name):
            self._get_row_by_policy_name(name).click()

    def _get_row_by_policy_name(self, name):
        return BaseElement(XPathLocator("//label[@* and ancestor::md-checkbox[contains(*, '{}')]]".format(name)), self)

    def is_selected(self, name):
        element = BaseElement(XPathLocator("//md-checkbox[contains(*, '{}')]".format(name)), self)
        element_class_name = find_element(element).get_attribute('class')
        if 'mat-checkbox-checked' in element_class_name:
            return True
        else:
            return False

## exclusion grid element:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.page_types.drop_down_select import DropDownSelect
from tests.QA.functionality.management.ui_bahamas.page_types.md_check_box import MdCheckBox
from tests.QA.functionality.management.ui_bahamas.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_bahamas.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.grid_element import Grid
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class ExclusionGrid(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[@* and descendant::*[contains(@class, 'header')]]")
        super(ExclusionGrid, self).__init__(locator, parent)

    @property
    def type_selector(self):
        text_box_element = TextBox(XPathLocator("//md-select[contains(@placeholder, 'Select Exclusion Type')]"), self)
        return ExclusionDropDownSelect(self.driver, text_box_element)

    @property
    def include_global_checkbox(self):
        return MdCheckBox('827', self)

    @property
    def results_count(self):
        return TextElement(XPathLocator("//*[contains(@class, 'resultsCount')]"), self)

    @property
    def grid(self):
        return Grid(self)


class ExclusionDropDownSelect(DropDownSelect):
    def __init__(self, driver, text_box_element):
        locator = XPathLocator("//div[contains(@id, 'cdk-overlay-') and descendant::*[@class='mgmt-path']]")
        super(ExclusionDropDownSelect, self).__init__(driver, None, text_box_element, locator)

    def select_by_text(self, text):
        values = {'Path': 'mgmt-path', 'Signer Identity': 'mgmt-signer-identity',
                  'File Type': 'mgmt-filetype', 'Browser': 'mgmt-browser'}
        self.open()
        locator = XPathLocator("//md-option[@* and descendant::i[contains(@class, '{}')]]".format(values[text]))
        elem = BaseElement(locator, self)
        try:
            elem.click()
        except:
            raise Exception("Can't click on element {xpath} with text {text}".format(xpath=elem.locator.get_xpath(),
                                                                                     text=text))

## Exclusion header element:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class ExclusionHeader(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-exclusion-header[@*]")
        super(ExclusionHeader, self).__init__(locator, parent)

    @property
    def name(self):
        return TextElement(XPathLocator("//h3[@*]"), self)

    @property
    def new_exclusion_btn(self):
        return Button(XPathLocator("//button[@* and descendant::i[contains(@class, 'mgmt-new-exclusion')]]"), self)

    @property
    def delete_exclusion_btn(self):
        return Button(XPathLocator("//button[@* and descendant::i[contains(@class, 'mgmt-delete')]]"), self)

## exclusion type box element
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator, ClassNameLocator


class TypeBox(BaseElement):
    def __init__(self, name, parent):
        locator = XPathLocator("//*[contains(@class, 'type-box') and contains(@href, '{}')]".format(name))
        super(TypeBox, self).__init__(locator, parent)

    @property
    def icon(self):
        xpath = "//i[contains(@class, 'mgmt-path') and ancestor::*[contains(@class, 'icon-box')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def name(self):
        return TextElement(ClassNameLocator("name"), self)

    @property
    def total(self):
        return TextElement(XPathLocator("//*[@class='num' and ancestor::*[@class='total']]"), self)

    @property
    def open_button(self):
        return Button(XPathLocator("//button[@*]"), self)


class ExclusionTypeBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[@* and descendant::*[contains(@class, 'select-exclusion-type-box')]]")
        super(ExclusionTypeBox, self).__init__(locator, parent)

    @property
    def path_type(self):
        return TypeBox('path', self)

    @property
    def signer_identity_type(self):
        return TypeBox('certificate', self)

    @property
    def file_type(self):
        return TypeBox('file', self)

    @property
    def browser_type(self):
        return TypeBox('browser', self)

    @property
    def title(self):
        return TextElement(XPathLocator("//h4[@*]"), self)

## Exclusion left side bar:
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.utils.actions import find_element
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator, ClassNameLocator

from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement


class LeftSideBar(BaseElement):
    def __init__(self, parent):
        locator = ClassNameLocator('list-sidebar')
        super(LeftSideBar, self).__init__(locator, parent)

    def get_list_by_name(self, name):
        return BaseElement(XPathLocator("//*[contains(text(), '{}')]".format(name)), self)

    @property
    def new_list_btn(self):
        return Button(XPathLocator("//a[contains(@class, 'link-btn') and contains(text(), 'New List')]"), self)

    @property
    def all_policies(self):
        return BaseElement(XPathLocator("//*[@class='title' and contains(text(), 'Lists')]"), self)

    def get_selected_list_name(self):
        side_list = BaseElement(ClassNameLocator("side-list"), self)
        active_elem = BaseElement(XPathLocator("//div[contains(@class, 'item-wrapper active')]"), side_list)
        text_containing_elem = BaseElement(ClassNameLocator("ellipsis"), active_elem)
        return str(find_element(text_containing_elem).text)

## Frid element:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.page_types.md_check_box import MdCheckBox
from tests.QA.functionality.management.ui_bahamas.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class Grid(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//md-table[contains(@role, 'grid')]")
        super(Grid, self).__init__(locator, parent)

    def get_row_by_text(self, text):
        return GridRow(text, self)

    @property
    def select_all_checkbox(self):
        wrapper = BaseElement(XPathLocator("//md-header-row[@*]"), self)
        return MdCheckBox('', wrapper)

    def click_row_by_text(self, text):
        self.get_row_by_text(text).click()


class GridRow(BaseElement):
    def __init__(self, text, parent):
        locator = XPathLocator("//md-row[@* and descendant::*[contains(normalize-space(), '{}')]]".format(text))
        super(GridRow, self).__init__(locator, parent)

    @property
    def checkbox(self):
        return MdCheckBox('', self)

    def select(self):
        self.checkbox.check()

    def unselect(self):
        self.checkbox.uncheck()

    def is_selected(self):
        return self.checkbox.is_checked()

    def get_path_value(self):
        self._get_column_value('path')

    def get_type_value(self):
        self._get_column_value('type')

    def get_subfolders_value(self):
        self._get_column_value('subfolders')

    def get_last_update_value(self):
        self._get_column_value('dateUpdated')

    def get_user_value(self):
        self._get_column_value('user')

    def _get_column_value(self, column_name):
        elem = TextElement(XPathLocator("//md-cell[contains(@class, '{}')]".format(column_name)), self)
        return elem.get_text()


## new exclusion page:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.page_types.drop_down_select import DropDownSelect
from tests.QA.functionality.management.ui_bahamas.page_types.md_check_box import MdCheckBox
from tests.QA.functionality.management.ui_bahamas.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.edit_list import EditListDialog
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.exclusions_page.exclusion_grid_element import \
    ExclusionDropDownSelect
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class NewExclusionDialog(EditListDialog):
    def __init__(self, driver):
        super(NewExclusionDialog, self).__init__(driver)

    @property
    def type_selector(self):
        text_box_element = TextBox(XPathLocator("//md-select[contains(@placeholder, 'Select Exclusion Type')]"), self)
        return ExclusionDropDownSelect(self.driver, text_box_element)

    @property
    def os_selector(self):
        text_box_element = TextBox(XPathLocator("//md-select[@placeholder='OS']"), self)
        return OSDropDownSelector(self.driver, text_box_element)

    @property
    def path(self):
        return TextBox(XPathLocator("//input[contains(@placeholder, 'Path')]"), self)

    @property
    def include_subfolders_checkbox(self):
        return MdCheckBox('74', self)

    @property
    def description(self):
        return TextBox(XPathLocator("//input[contains(@placeholder, 'Description')]"), self)

    @property
    def save_and_add_another_btn(self):
        return Button(XPathLocator("//span[contains(text(), 'Save and Add Another')]"), self)


class OSDropDownSelector(DropDownSelect):
    def __init__(self, driver, text_box_element):
        locator = XPathLocator("//div[contains(@id, 'cdk-overlay-') and descendant::*[@class='mgmt-windows']]")
        super(OSDropDownSelector, self).__init__(driver, None, text_box_element, locator)

    def select_by_text(self, text):
        values = {'Windows': 'mgmt-windows', 'OS X': 'mgmt-mac', 'Linux': 'mgmt-linux',
                  'windows': 'mgmt-windows', 'osx': 'mgmt-mac', 'linux': 'mgmt-linux'}
        self.open()
        locator = XPathLocator("//md-option[@* and descendant::i[contains(@class, '{}')]]".format(values[text]))
        elem = BaseElement(locator, self)
        try:
            elem.click()
        except:
            raise Exception("Can't click on element {xpath} with text {text}".format(xpath=elem.locator.get_xpath(),
                                                                                     text=text))

## policies box element:
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_bahamas.utils.actions import find_elements
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class PoliciesBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//div[@* and descendant::*[contains(@class, 'delete_wrapper')]]")
        super(PoliciesBox, self).__init__(locator, parent)

    @property
    def delete_list_button(self):
        return BaseElement(XPathLocator("//a[@* and descendant::i[contains(@class, 'mgmt-delete')]]"), self)

    @property
    def add_remove_policies_btn(self):
        return BaseElement(XPathLocator("//a[@* and ancestor::*[contains(@class, 'add_wrapper')]]"), self)

    @property
    def list_box(self):
        return ListBox(self)


class ListBullet(BaseElement):
    def __init__(self, policy_name, parent):
        locator = XPathLocator("//*[contains(@class, 'list-bullet') and contains(text(), '{}')]".format(policy_name))
        super(ListBullet, self).__init__(locator, parent)

    @property
    def view_policy_btn(self):
        return BaseElement(XPathLocator("//a[contains(@class, 'tool-btn')]"), self)


class ListBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'list-box')]")
        super(ListBox, self).__init__(locator, parent)

    def get_policy_by_name(self, policy_name):
        return ListBullet(policy_name, self)

    def is_policy_in_list(self, exact_policy_name):
        return self.get_policy_by_name(exact_policy_name).is_in_dom()

    def get_all_policy_names_in_list(self):
        bullet = ListBullet('', self)
        elements = find_elements(bullet)
        names = list()
        for element in elements:
            current = element.text.partition('\n')[0]
            names.append(current)
        return names

________________________________________________________________________________________

Configuration_page:

__ini__
from tests.QA.functionality.management.ui_bahamas.page_types.base_page import TopLevelPage
from tests.QA.functionality.management.ui_bahamas.page_types.button import Button
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.configuration_page.configuration_data_section import \
    ConfigurationDataSection
from tests.QA.functionality.management.ui_bahamas.pages.p_main.settings_page.configuration_page.configuration_description_section import \
    ConfigurationDescriptionSection
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator


class ConfigurationTab(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//mgmt-configuration[@* and descendant::mgmt-content-with-description[@*]]")
        super(ConfigurationTab, self).__init__(driver, locator)

    @property
    def configuration_data(self):
        return ConfigurationDataSection(self)

    @property
    def configuration_description(self):
        return ConfigurationDescriptionSection(self)

    @property
    def save_button(self):
        return Button(XPathLocator("//span[contains(text(), 'Save')]"), self)

    @property
    def discard_button(self):
        return Button(XPathLocator("//*[contains(text(), 'discard changes')]"), self)

##Configuration data section:
from tests.QA.functionality.management.ui_bahamas.page_types.md_switch import MdSwitch
from tests.QA.functionality.management.ui_bahamas.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_bahamas.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator

from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement


class ConfigurationDataSection(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'content-data')]")
        super(ConfigurationDataSection, self).__init__(locator, parent)

    @property
    def cloud_connectivity(self):
        xpath = "//div[contains(@class, 'stretched' ) and descendant::label[contains(text(), 'Cloud connectivity')]]"
        wrapper = BaseElement(XPathLocator(xpath), self)
        return TextElement(XPathLocator("//div[@*]"), wrapper)

    @property
    def stay_signed_in_days(self):
        return TextBox(XPathLocator("//input[@type='number' and contains(@formcontrolname, 'signedInDuration')]"), self)

    @property
    def two_factor_auth(self):
        return MdSwitch('md-slide-toggle-17', self)

    @property
    def management_url(self):
        return TextBox(XPathLocator("//input[@type='text' and contains(@formcontrolname, 'accessibleUrl')]"), self)

## configuraion description section:
from tests.QA.functionality.management.ui_bahamas.utils.locator import XPathLocator

from tests.QA.functionality.management.ui_bahamas.page_types.base_page import BaseElement


class ConfigurationDescriptionSection(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'content-description')]")
        super(ConfigurationDescriptionSection, self).__init__(locator, parent)
