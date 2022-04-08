import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.yahoo.com/')


driver.find_element_by_id('uh-search-box').send_keys('software testing')
driver.maximize_window()
#driver.implicitly_wait(20)
driver.find_element_by_id("uh-search-button").click()
#driver.find_element_by_id("yschsp").clear()
driver.minimize_window()
driver.maximize_window()
driver.title.replace('ynet')
driver.back()

# Wait for 5 seconds
time.sleep(5)

driver.quit()
