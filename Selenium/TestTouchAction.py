from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from time import sleep

class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        pass
    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID,'kw')
        ele.send_keys("selenium测试")
        ele_search = self.driver.find_element(By.ID,'su')
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele,0,10000).perform()
        sleep(3)