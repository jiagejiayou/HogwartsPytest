import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps={#真机
            'platformName': 'android',
            'platformVersion': '10.0',
            'browserName':'chrome',
            'noReset':True,
            'deviceName':'88Y5T19C26009612',
            'dontStopAppOnReset': True
        }
        caps = {#genimotion
            'platformName': 'android',
            'platformVersion': '6.0',
            'browserName': 'Browser',#自带的浏览器
            'noReset': True,
            'deviceName': '192.168.112.101:5555',
            'dontStopAppOnReset': True
            # 'chromedriverExecutableDir': 'E:\PythonStd\HogwartsPytest\chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

        # self.driver.quit()
    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        locator = (By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
        time.sleep(5)


