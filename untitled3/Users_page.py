Init:
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import TopLevelPage
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.content_data import Content
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.description_data import Description
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.side_bar import LeftSidebar
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.toolbar import ToolbarButtons
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class UsersTab(TopLevelPage):
    def __init__(self, driver):
        locator = XPathLocator("//mgmt-users[@*]")
        super(UsersTab, self).__init__(driver, locator)

    @property
    def toolbar_buttons(self):
        return ToolbarButtons(self)

    @property
    def left_sidebar(self):
        return LeftSidebar(self)

    @property
    def content(self):
        return Content(self)

    @property
    def description(self):
        return Description(self)

--------------------------------------------------------------------------------------------------------------------------
Content Data:

from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.password import PasswordBox
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.two_factor import TwoFactorBox
from tests.QA.functionality.management.ui_alhambra.pages.p_main.settings_page.users_page.user_details import UserDetailsBox
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class VerifyEmailBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[contains(@boxtitle, 'Verify Email')]")
        super(VerifyEmailBox, self).__init__(locator, parent)

    @property
    def verify_btn(self):
        return Button(XPathLocator("//*[contains(@class, 'pointer') and contains(text(), 'Verify')]"), self)


class ApiTokenBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[contains(@boxtitle, 'API Token')]")
        super(ApiTokenBox, self).__init__(locator, parent)

    @property
    def generate_btn(self):
        return Button(XPathLocator("//*[contains(@class, 'pointer') and contains(text(), 'Generate')]"), self)


class Content(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//*[contains(@class, 'content-data')]")
        super(Content, self).__init__(locator, parent)

    @property
    def user_details_box(self):
        return UserDetailsBox(self)

    @property
    def password_box(self):
        return PasswordBox(self)

    @property
    def two_factor_box(self):
        return TwoFactorBox(self)

    @property
    def veryfy_email(self):
        return VerifyEmailBox(self)

    @property
    def api_token(self):
        return ApiTokenBox(self)

-----------------------------------------------------------------------------------------------------------------------
Description data:

from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.utils.locator import ClassNameLocator


class Description(BaseElement):
    def __init__(self, driver):
        locator = ClassNameLocator("content-description")
        super(Description, self).__init__(driver, locator)

--------------------------------------------------------------------------------------------------------------------------
Password:
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class PasswordBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[@* and descendant::*[contains(@class, 'user-details')]]")
        super(PasswordBox, self).__init__(locator, parent)

    @property
    def change_btn(self):
        return Button(XPathLocator("//*[contains(@class, 'pointer') and contains(text(), 'Change')]"), self)

    @property
    def password(self):
        return TextBox(XPathLocator("//input[@formcontrolname='newPassword']"), self)

    @property
    def confirm_password(self):
        return TextBox(XPathLocator("//input[@formcontrolname='confirmPassword']"), self)

    @property
    def cancel_btn(self):
        return Button(XPathLocator("//*[contains(@class, 'cancel-passwords')]"), self)

    @property
    def password_min_lenth_error(self):
        xpath = "//*[@class='error' and descendant::*[contains(text(), 'Minimum length')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def password_invalid_error(self):
        xpath = "//*[@class='error' and descendant::*[contains(text(), 'Invalid username')]]"
        return BaseElement(XPathLocator(xpath), self)

    @property
    def password_match_error(self):
        xpath = "//*[@class='error' and descendant::*[contains(text(), 'Passwords do not match')]]"
        return BaseElement(XPathLocator(xpath), self)

---------------------------------------------------------------------------------------------------------------------
Side Bar:
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_alhambra.utils.actions import find_element
from tests.QA.functionality.management.ui_alhambra.utils.locator import ClassNameLocator, XPathLocator


class LeftSidebar(BaseElement):
    def __init__(self, parent):
        locator = ClassNameLocator("users-sidebar")
        super(LeftSidebar, self).__init__(locator, parent)

    @property
    def all_users_title(self):
        return TextElement(XPathLocator("//*[@class='title']"), self)

    def get_user_by_name(self, name):
        return BaseElement(XPathLocator("//*[contains(text(), '{}')]".format(name)), self)

    def get_selected_user_name(self):
        side_list = BaseElement(ClassNameLocator("side-list"), self)
        active_elem = BaseElement(XPathLocator("//div[contains(@class, 'item-wrapper active')]"), side_list)
        text_containing_elem = BaseElement(XPathLocator("//*[contains(@class, 'ellipsis')]"), active_elem)
        return str(find_element(text_containing_elem).text).replace(' ', '')

    def get_user_role(self, name):
        element = self.get_user_by_name(name)
        return TextElement(XPathLocator("//*[@class='right']"), element).get_text().replace(' ', '')

-----------------------------------------------------------------------------------------------------------------
toolbar:
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.button import Button
from tests.QA.functionality.management.ui_alhambra.utils.locator import ClassNameLocator, XPathLocator


class ToolbarButtons(BaseElement):
    def __init__(self, parent):
        locator = ClassNameLocator('top-headers-buttons')
        super(ToolbarButtons, self).__init__(locator, parent)

    @property
    def new_user_btn(self):
        return Button(XPathLocator("//*[contains(text(), 'New User')]"), self)

    @property
    def delete_btn(self):
        return Button(XPathLocator("//*[contains(text(), 'Delete')]"), self)

------------------------------------------------------------------------------------------------------------------
two factors:
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.md_switch import MdSwitch
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class TwoFactorBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[contains(@boxtitle, 'Two Factor Authentication')]")
        super(TwoFactorBox, self).__init__(locator, parent)

    @property
    def two_factor_slider(self):
        return MdSwitch(None, self, XPathLocator("//md-slide-toggle[@formcontrolname='twoFA']"))

---------------------------------------------------------------------------------------------------------------------
user details:
from tests.QA.functionality.management.ui_alhambra.page_types.base_page import BaseElement
from tests.QA.functionality.management.ui_alhambra.page_types.drop_down_select import DropDownSelect
from tests.QA.functionality.management.ui_alhambra.page_types.text_box import TextBox
from tests.QA.functionality.management.ui_alhambra.page_types.text_element import TextElement
from tests.QA.functionality.management.ui_alhambra.utils.locator import XPathLocator


class UserDetailsBox(BaseElement):
    def __init__(self, parent):
        locator = XPathLocator("//mgmt-ui-box[contains(@boxtitle, 'Password')]")
        super(UserDetailsBox, self).__init__(locator, parent)

    @property
    def username(self):
        return TextElement(XPathLocator("//*[contains(@class, 'username-title')]"), self)

    @property
    def full_name(self):
        return TextBox(XPathLocator("//input[@formcontrolname='fullName']"), self)

    @property
    def email(self):
        return TextBox(XPathLocator("//input[@formcontrolname='email']"), self)

    @property
    def role(self):
        text_box_element = TextBox(XPathLocator("//md-select[contains(@formcontrolname, 'role')]"), self)
        return DropDownSelect(self.driver, 'cdk-overlay-', text_box_element)

    @property
    def last_login(self):
        xpath = "//div[@* and ancestor::div[@class='form-item' and descendant::label[contains(text(), 'last login')]]]"
        return TextElement(XPathLocator(xpath), self)

-----------------------------------------------------------------------------------------------------------------------
