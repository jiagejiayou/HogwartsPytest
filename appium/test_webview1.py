import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            'noReset': True,
            'deviceName': '192.168.112.101:5555',
            'dontStopAppOnReset': True
            # 'chromedriverExecutableDir': 'E:\PythonStd\HogwartsPytest\chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        #进入交易页面，并切换context到webview
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.current_context)

        #点击A股开户
        print(self.driver.window_handles)

        self.driver.find_element_by_css_selector("li.trade_home_agu_3bZ").click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print(self.driver.current_window_handle)
        #输入手机号码，验证码，点击立即开户按钮
        time.sleep(10)
        phone_loc = (MobileBy.ID,'phone-number')
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(phone_loc))

        self.driver.find_element(*phone_loc).send_keys("18398609040")
        self.driver.find_element(MobileBy.ID,'code').send_keys("123465")
        self.driver.find_element_by_css_selector(".btn-submit").click()
        # time.sleep(5)

