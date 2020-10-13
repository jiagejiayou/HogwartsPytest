import time
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
        caps['skipADeviceInitialization '] = 'true'
        self.driver = webdriver.Remote('http://192.168.2.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        '''
        1.打开雪球
        2.点击搜索输入框
        3.向输入框里面输入“阿里巴巴”
        4.在搜索结果里面选择“阿里巴巴”，然后点击
        5.获取这只阿里巴巴的股价，并判断这只股票的价格>200
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price>200
    def test_attr(self):
        """
        打开雪球首页
        定位首页的搜索框
        判断搜索框是否可用，并查看name的属性值
        打印搜索框这个元素左上角坐标和宽高
        在搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        :return:
        """
        search_elem = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = search_elem.is_enabled()
        print(search_elem.text)
        print(search_elem.location)
        print(search_elem.size)
        if search_enabled==True:
            search_elem.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            search_re=alibaba.get_attribute("displayed")
            if search_re=='true':
                print("search success!")
            else:
                print("search fail")
    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()


    def test_scroll_find_element(self):
        """
        #通过滑动页面找到特定元素
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("奎星楼街").'
                                                        'instance(0));').click()
    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        """
        显示等待
        """
        locator = (MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # el = self.driver.find_element(*locator)
        el = WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        print(el.text)
        current_price = float(el.text)
        expect_price = 250
        # assert current_price>expect_price
        #hamcrest 断言
        assert_that(current_price,close_to(expect_price,expect_price*0.1))

if __name__ == '__main__':
    pytest.main()
