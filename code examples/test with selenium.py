from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = "tomer"
pwd = "password"
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()


"""
Explanation of the code

Code line 1: From selenium module import webdriver
Code line 2: From selenium module import Keys
Code line 3: User is a blank variable which will be we used to store values of username.
Code line 4: pwd is also a blank (here it is empty, but the user can provide values in it) variable. This will be used to store values of the password.
Code line 5: In this line, we are initializing "FireFox" by making an object of it.
Code line 6: The "driver.get method" will explore to a page given by the URL.WebDriver will hold up until the page has completely been loaded (that is, the "onload" occasion has let go), before returning control to your test or script.
Code line 7: "Asserts" keyword is used to verify the conditions. In this line, we are confirming whether the title is correct or not. For that, we will compare the title with the string which is given.
Code line 8: In this line, we are finding the element of the textbox where the "email" has to be written.
Code line 9: Now we are sending the values to the email section
Code line 10: Same for the password
Code line 11: Sending values to the password section
Code line 12: Elem.send_keys(Keys.RETURN) is used to press enter after the values are inserted
Code line 13: Close
OUTPUT

The values of the username "guru99" and password entered.
"""

# ______________________________________________________________________________________________________________________________________

