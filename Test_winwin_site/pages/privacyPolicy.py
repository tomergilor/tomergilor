from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class PrivacyPolicyPage():
    def __init__(self, driver):
        self.driver = driver

        # elements:
        self.name_tbx = 'input_comp-kfr4aji02'
        self.page_info = 'comp-kfr4ai8w3'
        self.privacy_title = '//span[contains(text(), "TestAuto Privacy Policy")]'

    def verify_text_info_appears(self, driver):
        driver.find_element_by_xpath(self.privacy_title)
