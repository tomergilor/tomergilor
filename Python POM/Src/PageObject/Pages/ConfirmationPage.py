__author__ = 'Aditya Roy'


from selenium.webdriver.common.by import By



class Confirmation(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        from Src.PageObject.Locators import Locator
        self.thankYou = driver.find_element(By.XPATH, Locator.thank_you)
        self.UserID = driver.find_element(By.XPATH, Locator.post_user)
