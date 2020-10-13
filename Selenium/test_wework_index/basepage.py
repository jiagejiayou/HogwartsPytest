from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _driver = None
    _base_url =""
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver=driver

        if self._base_url != "":j
            self._driver.get(self._base_url)
    def find(self, by, locator):
        return self._driver.find_element(by,locator)
    def finds(self, by, locator):
        return self._driver.find_elements(by,locator)
    def wait_for_click(self, locator):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
    def wait_for_condition(self, condition):
        WebDriverWait