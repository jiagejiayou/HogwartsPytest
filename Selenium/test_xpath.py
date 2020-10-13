#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


class Testxpath:
    def setup(self):
        self.driver=webdriver.Chrome()
        # self.driver.get("https://www.baidu.com/")
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_open(self):
        self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID,'su').click()
    def test_ActionChains(self):
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        sleep(3)
        action.perform()
    def test_move_to_elem(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID,'s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")

        acton = ActionChains(self.driver)
        # acton.drag_and_drop(drag_element,drop_element).perform()
        acton.click_and_hold(drag_element).release(drop_element)
        sleep(3)
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

































        