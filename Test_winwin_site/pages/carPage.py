from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class CarPage():
    def __init__(self, driver):
        self.driver = driver

        # elements:
        self.manufacturer_dbx = 'ctl00_topNav_ctl00_ddlManuf'
        self.model_dbx = 'ctl00_topNav_ctl00_ddlModel'
        self.from_year_dbx = 'ctl00_topNav_ctl00_ddlYearFrom'
        self.to_year_dbx = 'ctl00_topNav_ctl00_ddlYearTo'
        self.gears_dbx = 'ctl00_topNav_ctl00_ddlGear'
        self.area_dbx = 'ctl00_topNav_ctl00_ddlDistr'
        self.price_min_txb = 'ctl00_topNav_ctl00_txtPriceFrom'
        self.price_max_txb = 'ctl00_topNav_ctl00_txtPriceTo'
        self.free_text_txb = 'FreeText'
        self.no_thanks_btn = '//div[contains(@class , "UserAgentFieldName NoThanks")]'
        self.no_thanks = "לא תודה"
        self.find_btn = 'searchBtnDiv'
        self.results_txb = '//span[contains(text(), " מודעות  ")]'

    def choose_car_manufacturer_name(self, driver, car_manu):
        elem = driver.find_element_by_id(self.manufacturer_dbx)
        Select(elem).select_by_visible_text(car_manu)

    def choose_car_model_name(self, driver, car_model):
        elem = driver.find_element_by_id(self.model_dbx)
        Select(elem).select_by_visible_text(car_model)

    def choose_from_year(self, driver, from_year):
        elem = driver.find_element_by_id(self.from_year_dbx)
        Select(elem).select_by_visible_text(from_year)

    def choose_to_year(self, driver, car_model):
        elem = driver.find_element_by_id(self.to_year_dbx)
        Select(elem).select_by_visible_text(car_model)

    def choose_gear_option(self, driver, car_model):
        elem = driver.find_element_by_id(self.gears_dbx)
        Select(elem).select_by_visible_text(car_model)

    def choose_area_of_search(self, driver, area_of_search):
        elem = driver.find_element_by_id(self.area_dbx)
        Select(elem).select_by_visible_text(area_of_search)

    def choose_min_price(self, driver, min_price):
        elem = driver.find_element_by_id(self.price_min_txb)
        elem.send_keys(min_price)

    def choose_max_price(self, driver, max_price):
        elem = driver.find_element_by_id(self.price_max_txb)
        elem.send_keys(max_price)

    def enter_free_text(self, driver, free_text):
        elem = driver.find_element_by_id(self.free_text_txb)
        elem.send_keys(free_text)

    def click_on_search_btn(self, driver):
        driver.find_element_by_id(self.find_btn).click()
        time.sleep(3)
        nothanks = driver.find_element_by_xpath(self.no_thanks_btn)
        if self.no_thanks in driver.page_source:        # if there is a popup, click on no thanks
            nothanks.click()

    def get_number_of_results(self, driver):
        res = driver.find_element_by_xpath(self.results_txb)
        res_text = res.text
        for num in res_text:
            if num.isdigit():
                num_res = num
                print("The results number is: " + num)




        # def insert_name(self, driver, user_name):
    #    driver.find_element_by_id(self.name_tbx).send_keys(user_name)

    # def verify_text_get_in_touch_exists(self, driver):
    #     driver.find_element_by_xpath(self.get_in_touch_text)
    #
    # def verify_text_thanks_for_submit_appears(self, driver):
    #     driver.find_element_by_xpath(self.thanks_for_submit)
    #     try:
    #         assert 'Thanks for submitting!' in driver.page_source
    #         print("Sent successfully !")
    #     except AssertionError:
    #         print("The message was not sent !")
    #

