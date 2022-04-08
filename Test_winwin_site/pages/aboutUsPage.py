

class AboutUs():
    def __init__(self, driver):
        self.driver = driver

        # elements:
        self.moledet_song = ''
        self.nodedet_song = ''
        self.about_us_text = '//*[text() = "About Us"]'

    def verify_text_about_us_exists(self, driver):
        driver.find_element_by_xpath(self.about_us_text)
