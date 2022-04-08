from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement, TopLevelPage
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.page_types.drop_down_select import DropDownSelect
from tests.QA.functionality.management.ui_alhambra.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_alhambra.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_alhambra.utils.actions import find_element
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class UpdatesTab(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//mgmt-updates[@*]")
        super(UpdatesTab, self).__init__(driver, locator)

    @property
    def platform(self):
        text_box_element = TextBox(XPathLocator("//md-select[contains(@placeholder, 'platform')]"), self)
        return DropDownSelect(self.driver, 'cdk-overlay-', text_box_element)

    @property
    def choose_file_button(self):
        return BaseElement(XPathLocator("//*[contains(@class, 'upload-button')]"), self)

    @property
    def upload_button(self):
        return Button(XPathLocator("//span[contains(text(), 'UPLOAD FILE')]"), self)

    @property
    def discard_button(self):
        return Button(XPathLocator("//*[contains(text(), 'discard changes')]"), self)

    @property
    def get_progress_percentage(self):
        elem = TextElement(XPathLocator("//*[contains(text(), '%') and ancestor::mgmt-ui-progress-bar[@*]]"), self)
        return elem.get_text().partition('%')[0]

    @property
    def deploy_button(self):
        return Button(XPathLocator("//*[contains(text(), 'DEPLOY')]"), self)

    @property
    def upload_finished_msg(self):
        return TextElement(XPathLocator("//*[contains(@class, deploy-text)]"), self)

    @property
    def version_number(self):
        return TextBox(XPathLocator("//input[contains(@class, 'version')]"), self)

    def choose_file(self, path_to_file):
        elem = self.driver.find_element_by_xpath("//input[@* and ancestor::*[contains(@class, 'upload-button')]]")
        elem.send_keys(path_to_file)

    def is_error_msg_appears(self):
        return BaseElement(XPathLocator("//*[contains(@class, 'file-upload-error')]"), self).is_in_dom()

    def is_file_choosen_correctly(self):
        elem = BaseElement(XPathLocator("//*[contains(@class, 'row selected-file')]"), self)
        return 'error' in find_element(elem).get_attribute('class')
