import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestXiaocx:
    def setup(self):
        des_caps={
            'platformName': 'android',
            'platformVersion': '10.0',
            'appPackage':'com.tencent.mm',
            'appActivity':'.ui.LauncherUI',
            'automationName':'Appium',
            'noReset':True,
            'deviceName':'88Y5T19C26009612',
            'noReset': True,
            'chromeOptions': {'androidProcess':'com.tencent.mm:appbrand0'},
            # 'adbPort': 5038
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def swipeDown(self, t=800, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.1 # 起始y坐标
        y2 = l['height'] * 0.5  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
    def test_search(self):
        """
        1.下滑，显示小程序
        2.选取有道小程序
        3.选择搜索框
        4.输入搜索单词
        5.选取第一个结果
        :return:
        """
        self.swipeDown()

        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@text='下厨房+']").click()
        self.driver.find_element(MobileBy.ID,'com.tencent.mm:id/h87').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("视频菜谱").'
                                                        'instance(0));').click()


