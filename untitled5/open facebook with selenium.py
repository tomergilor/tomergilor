#######    Open Facebook site with selenium    ########

from selenium import webdriver

driver = webdriver.Firefox("C:\\Python27\\Lib\\site-packages\\selenium\\webdriver\\firefox")
driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("C:\\Users\\Tomer\\.PyCharmCE2017.2\\Exercises\\Selenium\\Screenshots\\Before_Facebook.png")
print (driver.title)
assert "Facebook" in driver.title

driver.find_element_by_id("email").send_keys("selenium werbdriver")
driver.find_element_by_name("pass").send_keys("python")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("C:\\Users\\Tomer\\.PyCharmCE2017.2\\Exercises\\Selenium\\Screenshots\\After_Facebook.png")
driver.quit()


