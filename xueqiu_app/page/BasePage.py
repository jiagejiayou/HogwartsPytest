from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find(self, by, locator = None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, locator)