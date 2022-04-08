from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        # elements:
        self.car_page_btn = 'mainMenu_1'
        self.contact_us = 'comp-kfr46g9y7label'
        self.more_menu = 'comp-kfr46g9y__more__label'
        self.privacy_policy = 'comp-kfr46g9ymoreContainer'
        self.shop_menu = 'comp-kfr46g9y3'

    def choose_cars_page(self, driver):
        driver.find_element_by_id(self.car_page_btn).click()

    def click_contact_us(self, driver):
        driver.find_element_by_id(self.contact_us).click()

