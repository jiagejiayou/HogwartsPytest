import os

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps={}
caps['deviceName']='emulator-5554'
caps['platformName'] = 'Android'
caps['platformVersion'] = '6.0'
        # caps['udid'] = os.getenv('udid',None)
caps['appPackage'] = 'com.xueqiu.android'
caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
caps['noReset'] = 'true'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
driver.implicitly_wait(10)
driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("apple")
driver.quit()


