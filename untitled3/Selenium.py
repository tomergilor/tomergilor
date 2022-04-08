"""

# ############ Login to Mgmt  ###########
#
# from selenium import webdriver
# import time
#
# #creating object of firefox
# driver = webdriver.Firefox()

#open the URL (MGMT)
driver.get('https://davidg-mgmt.sentinelone.local')
time.sleep(3)
driver.find_element_by_id('username').send_keys('mgmt')
time.sleep(3)
driver.find_element_by_name("password").send_keys('12345678')
time.sleep(1)
driver.find_element_by_xpath("//div[@id='content-wrapper']/div/div[2]/div[3]/div/div/form/div[3]/div/ui-checkbox/div/div").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
#------------------------------------------------------------------------------------------------------------------------

##### Test cases #####

import unittest
from selenium import webdriver
import time

class Test(unittest.TestCase):

    def setUp(self):
        print "Before test execution"
        self.driver = webdriver.Firefox()
        self.driver.get("https://davidg-mgmt.sentinelone.local")

    def tearDown(self):
        print "After test case execution"
        self.driver.quit()

    def testName(self):
        print "Test case execution"
        time.sleep(3)
        self.driver.find_element_by_id('username').send_keys('mgmt')

if __name__== "__main__":
    unittest.main()

"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class Test(unittest.TestCase):

    def setUp(self):
        print "Before test execution"
        self.driver = webdriver.Firefox()
        self.driver.get("http://shop.thetestingworld.com/")
        self.driver.maximize_window()


    def tearDown(self):
        print "After test case execution"
        self.driver.quit()


    def testName(self):
        print "Test case execution"
        time.sleep(2)               # wait 2 sec.
        self.driver.find_element_by_name('search').send_keys('iphone')          # Input value
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(@class, 'btn') and ancestor::*[@id='search' and descendant::*[]]]").click()   # click on search button
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Add to Cart']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='Checkout']").click()  #Click on button
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@value='guest']").click()    # Click on Radio button
        self.driver.implicitly_wait(5)                                          # wait 5 sec. to the element
        self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        time.sleep(2)
        sel = Select(self.driver.find_element_by_id("input-payment-country"))
        time.sleep(2)
        sel.select_by_visible_text("India")                                 # Select from drop down list
        time.sleep(3)


if __name__== "__main__":
    unittest.main()
