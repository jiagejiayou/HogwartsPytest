import time

import yaml
from hamcrest import *
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApp:
    def setup(self):
        caps = {}
        caps['deviceName'] = '192.168.112.101:5555'
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        caps['noReset'] = 'true'
        caps['dontStopAppOnReset'] = 'true'
        caps['unicodeKeyBoard']='true'
        caps['resetKeyBoard']='true'
        caps['skipDeviceInitialization '] = 'true'
        self.driver = webdriver.Remote('http://192.168.2.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()
        self.driver.quit()

    @pytest.mark.parametrize("searchkey,type,expect_price",[
        ('alibaba','BABA',250),
        ('xiaomi','01810',18)
    ])
    def test_search(self,searchkey,type,expect_price):
        """
        1.打开雪球
        2.点击搜索输入框
        3.向输入框里面输入搜索词，如“阿里巴巴”
        4.点击第一个搜索结果里
        5.判断股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        price_el = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(price_el.text)
        print(f"当前的价格{current_price}")
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))