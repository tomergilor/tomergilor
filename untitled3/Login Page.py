from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement, TopLevelPage
from tests.QA.functionality.management.ui_alhambra.page_types.check_box import CheckBox
from tests.QA.functionality.management.ui_alhambra.page_types.dis_button import DisButton
from tests.QA.functionality.management.ui_alhambra.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_alhambra.utils.locator import ClassNameLocator, NameLocator, XPathLocator


class LoginPage(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//div[contains(@class, 'loginFormWrapper')]")
        super(LoginPage, self).__init__(driver, locator)

    @property
    def username(self):
        return TextBox(NameLocator('username'), self)

    @property
    def password(self):
        return TextBox(NameLocator('password'), self)

    @property
    def agreement(self):
        xpath = "//div[contains(@class, 'checkbox') and contains(@class, 'enabled') and ancestor::ui-checkbox[contains(@ng-model, 'eulaChecked')]]"
        return CheckBox(XPathLocator(xpath), self)

    @property
    def login_btn(self):
        wrapper = BaseElement(ClassNameLocator('submitBTN'), self)
        return DisButton(XPathLocator("//button[contains(@class, 'main-button')]"), wrapper)

    def login_with_sso_btn(self):
        pass

