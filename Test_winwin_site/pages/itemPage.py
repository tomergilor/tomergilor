from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep


class ItemPage():
    def __init__(self, driver):
        self.driver = driver

        # elements:
        self.laptop_dell_price = '//span[contains(text(), "850.00 ₪")]'
        self.item_quantity = '//div[contains(@class , "_2uERl")]'
        self.add_to_cart_btn = '//div[contains(@class, "_3j0qu fggS- cell")]'
        self.row_up = '//span[contains(@data-hook, "number-input-spinner-up-arrow")]'
        self.go_to_cart_page_btn = '//cart-popup[@id="widget-view-cart-button"]'

    def verify_item_price(self, driver, price):
        item_val = driver.find_element_by_xpath(self.laptop_dell_price)
        assert str(item_val.text) == str(price)

    def choose_two_items(self, driver):
        driver.find_element_by_xpath(self.row_up).click()

    def add_item_to_cart(self, driver):
        driver.find_element_by_xpath(self.add_to_cart_btn).click()

    def click_open_cart_page(self, driver):
        # driver.switch_to.frame(self.iframe)
        driver.find_element_by_xpath(self.go_to_cart_page_btn).click()
        sleep(2)


# driver.switch_to.frame("Dialogue Window")
# Using the <iframe> WebElement identified through name attribute as follows:
#
# driver.switch_to.frame(driver.find_element_by_name('Dialogue Window'))