import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,locator):
        logging.info(f'find:{locator}')
        return self.driver.find_element(*locator)

    def find_click(self,locator):
        logging.info(f'find_click:{locator}')
        return self.find(locator).click()

    def find_sendkeys(self,locator,text):
        logging.info(f'find_sendkeys:{text}')
        return self.find(locator).send_keys(text)

    def find_scroll(self,text):
        logging.info(f'find_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def webdriver_wait(self,locator,timeout=10):
        logging.info(f'webdriver_wait:{locator}, timeout:{timeout}')
        ele = WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(*locator))
        return ele

    def back(self, num=1):
        logging.info(f'back:{num}')
        for i in range(num):
            self.driver.back()