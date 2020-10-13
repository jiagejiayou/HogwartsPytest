import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
class TestForm:
    def setup(self):
        '''
        浏览器复用，即每次不用打开新的浏览器运行,在已有的浏览器上进行测试
        需要将chrome浏览器加入环境变量，启动debug模式，先关闭所有浏览器，然后
        通过cmd window: chrome --remote-debugging-port=9222打开浏览器
        '''
        options =Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        # self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
    def teardown(self):
        pass

    @pytest.mark.skip
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id('user_login').send_keys("1079608990@qq.ocm")
        self.driver.find_element_by_id('user_password').send_keys("xiaoniuer11...")
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(3)

    def test_wework(self):
        #浏览器当前已经登录企业微信，可以直接执行点击
        self.driver.find_element_by_id("menu_contacts").click()
