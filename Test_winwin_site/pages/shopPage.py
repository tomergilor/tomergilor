from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class ShopPage():
    def __init__(self, driver):
        self.driver = driver

        # elements:
        self.laptop_dell_button = '_2BULo chromexPathFinder'
        self.page_info = 'comp-kfr4ai8w3'
        self.privacy_title = '//span[contains(text(), "TestAuto Privacy Policy")]'
        self.dell_laptop_item = '//div[contains(@class, "_3RqKm")]'

    # def click_laptop_dell_btn(self, driver):
    #     driver.find_element_by_id(self.laptop_dell_button).click()

    def click_laptop_dell_item(self, driver):
        driver.find_element_by_xpath(self.dell_laptop_item).click()
