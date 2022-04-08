from tests.QA.functionality.management.ui_bigben.page_types.base_page import TopLevelPage, BaseElement
from tests.QA.functionality.management.ui_bigben.page_types.button import Button
from tests.QA.functionality.management.ui_bigben.page_types.check_box import CheckBox
from tests.QA.functionality.management.ui_bigben.page_types.drop_down_select import DropDownSelect
from tests.QA.functionality.management.ui_bigben.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_bigben.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_bigben.utils.locator import DataAidLocator
from abc import ABCMeta


class OsTypeSelector(DropDownSelect):  # ToDo
    def __init__(self, parent):
        locator = DataAidLocator("OsTypeSelector")  # ToDo
        super(OsTypeSelector, self).__init__(locator, parent)

class BrowserTypeSelector(DropDownSelect):  # ToDo
    def __init__(self, parent):
        locator = DataAidLocator("BrowserTypeSelector")  # ToDo
        super(BrowserTypeSelector, self).__init__(locator, parent)

class ExclusionTypeSelector(DropDownSelect):  # ToDo
    def __init__(self, parent):
        locator = DataAidLocator("ExclusionTypeSelector")  # ToDo
        super(ExclusionTypeSelector, self).__init__(locator, parent)


class NewExclusionDialog(TopLevelPage):
    __metaclass__ = ABCMeta

    def __init__(self, driver):
        locator = DataAidLocator("ExclusionLocatorArea")
        super(NewExclusionDialog, self).__init__(driver, locator)

    @property
    def header(self):
        return TextElement(DataAidLocator("NewExclusionHeader"), self)

    @property
    def os_type_selector(self):
        return OsTypeSelector(self)

    @property
    def exclusion_type_selector(self):
        return ExclusionTypeSelector(self)

    @property
    def description(self):
        return TextBox(DataAidLocator('DescriptionField'), self)

    @property
    def exclusion_scope(self):
        return BaseElement(DataAidLocator("SiteRadio"), self)

    @property
    def selected_groups(self):
        return BaseElement(DataAidLocator("GroupsRadio"), self)

    @property
    def save_btn(self):
        return Button(DataAidLocator("SaveButton"), self)

    @property
    def save_and_add_another_btn(self):
        return Button(DataAidLocator("SaveAndAddAnotherBtn"), self)

    @property
    def cancel_btn(self):
        return Button(DataAidLocator("CancelButton"), self)


class PathExclusion(NewExclusionDialog):
    def __init__(self, driver):
        super(PathExclusion, self).__init__(driver)

    @property
    def path(self):
        return TextBox(DataAidLocator("Exclusion_path"), self)

    @property
    def include_subfolders_checkbox(self):
        return CheckBox(DataAidLocator("IncludeSubFolderCheckbox"), self)

    @property
    def include_monitor_checkbox(self):
        return CheckBox(DataAidLocator("Monitor"), self)

    @property
    def exclusion_scope(self):
        return BaseElement(DataAidLocator("SiteCheckbox"), self)

    @property
    def selected_groups(self):
        return BaseElement(DataAidLocator("SelectedGroupCheckbox"), self)


class FileTypeExclusion(NewExclusionDialog):
    def __init__(self, driver):
        super(FileTypeExclusion, self).__init__(driver)

    @property
    def filetype(self):
        return TextBox(DataAidLocator("ExclusionFileType"), self)


class SignerIdentity(NewExclusionDialog):
    def __init__(self, driver):
        super(SignerIdentity, self).__init__(driver)

    @property
    def CertificateID(self):
        return TextBox(DataAidLocator("CertificateID"), self)


class BrowserExclusion(NewExclusionDialog):
    def __init__(self, driver):
        super(BrowserExclusion, self).__init__(driver)

    @property
    def browser_type(self):
        return TextBox(DataAidLocator("BrowserTypeDropdown"), self)

    @property
    def browser_type_selector(self):
        return BrowserTypeSelector(self)


class HashExclusion(NewExclusionDialog):
    def __init__(self, driver):
        super(HashExclusion, self).__init__(driver)

    @property
    def hash_exclusion(self):
        return TextBox(DataAidLocator("ExclusionWhiteHash"), self)
