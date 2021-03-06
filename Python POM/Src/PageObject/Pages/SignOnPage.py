__author__ = 'Aditya Roy'

__author__ = 'Aditya Roy'

from selenium.webdriver.common.by import By


class SignOn(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        from Src.PageObject.Locators import Locator
        self.userName = driver.find_element(By.XPATH, Locator.signOn_userName)
        self.password = driver.find_element(By.XPATH, Locator.signOn_password)
        self.login = driver.find_element(By.XPATH, Locator.signOn_login)
        self.welcomeText = driver.find_element(By.XPATH, Locator.signOn_txt)
        self.registrationLink = driver.find_element(By.XPATH,Locator.signOn_registerLink)



