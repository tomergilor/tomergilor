from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Test_winwin_site.pages.homePage import HomePage
from Test_winwin_site.pages.carPage import CarPage

driver = webdriver.Firefox()
url = "https://www.winwin.co.il/Homepage/Page.aspx"

home_page = HomePage(driver)
car_page = CarPage(driver)

user_name = 'Tomer'
user_mail = 'tomer@tomer.com'
subject = 'Hello'
manufacturer_name = 'יונדאי'
car_model = 'i30'
from_year = '2014'
to_year = '2014'
gear_type = 'אוטומטית'
area_to_search = 'רחובות – נס ציונה'
min_price = '30000'
max_price = '40000'
free_text = ''



# Open site homepage:
url = driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
sleep(1)

# click on cars page
home_page.choose_cars_page(driver)
driver.implicitly_wait(2)

# Fill search data
# select manufacturer car
car_page.choose_car_manufacturer_name(driver, manufacturer_name)

# select car model
car_page.choose_car_model_name(driver, car_model)

# select range of years
car_page.choose_from_year(driver, from_year)
car_page.choose_to_year(driver, to_year)

# select gear option
car_page.choose_gear_option(driver, gear_type)

# select area of search
car_page.choose_area_of_search(driver, area_to_search)

# select price range
car_page.choose_min_price(driver, min_price)
car_page.choose_max_price(driver, max_price)

# enter free text (optional)

# click to start search process
car_page.click_on_search_btn(driver)
sleep(3)
car_page.get_number_of_results(driver)



#
# # Scroll to page buttom and back up
# driver.execute_script("window.scrollTo(0, 1800)")
# sleep(2)
# driver.execute_script("window.scrollTo(1800, 0)")
# sleep(2)
#
# # Click on 'Contact us' page
# home_page.click_contact_us(driver)
# driver.implicitly_wait(3)
#
# # Verify 'Get in Touch' Text is existing
# contact_us_page.verify_text_get_in_touch_exists(driver)
# sleep(3)
#
# # Fill and send contact message details
# contact_us_page.insert_name(driver, user_name)
# contact_us_page.insert_email(driver, user_mail)
# contact_us_page.insert_subject(driver, subject)
# contact_us_page.insert_message(driver, message_txt)
# contact_us_page.click_on_submit_btn(driver)
# sleep(1)
# contact_us_page.verify_text_thanks_for_submit_appears(driver)
# sleep(2)
#
# # Click on privacy policy page from menu
# home_page.click_more_menu(driver)
# sleep(1)
# home_page.click_privacy_policy_menu(driver)
# sleep(2)
#
# # Verify privacy title page appears
# privacy_policy_page.verify_text_info_appears(driver)
# sleep(2)
#
# # Click shop menu button
# home_page.click_shop_menu(driver)
# sleep(3)
#
# # Choose and click the Dell laptop
# shop_page.click_laptop_dell_item(driver)
# sleep(2)
#
# # Verify the price is 850 NIS
# driver.execute_script("window.scrollTo(0, 1000)")
# sleep(2)
# item_page.verify_item_price(driver, item_price)
#
# # Add 2 items
# item_page.choose_two_items(driver)
# sleep(2)
#
# # Add to cart
# item_page.add_item_to_cart(driver)
# sleep(2)
#
# # Click ESC button
# webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# sleep(2)
#
# # Scroll up
# driver.execute_script("window.scrollTo(1800, 0)")
# sleep(2)

# Close driver:
driver.close()
