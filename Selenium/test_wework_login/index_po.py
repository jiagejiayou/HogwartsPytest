
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Selenium.test_wework_login.login import Login
from Selenium.test_wework_login.register import Register


class Index:
    '''
    首页面po
    '''
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
    def goto_register(self):
        '''

        点击立即注册
        进入到立即注册的po
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

    def goto_login(self):
        '''
        点击立即登录
        进入到立即登录的po
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self.driver)
