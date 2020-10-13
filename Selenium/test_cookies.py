import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCookie:
    def setup(self):

        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        # self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_wework(self):
        #可以不使用浏览器复用
        self.driver.get("https://work.weixin.qq.com/")
        # 先获取到cookies, 然后去掉有效期，将cookies存储到db数据库里
        # print(self.driver.get_cookies())
        # cookies = [{'domain': 'work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598453953'}, {'domain': 'work.weixin.qq.com', 'expiry': 1629989953, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598453953'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '5517264533550753'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598485488.494301, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2r5a4t'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'work.weixin.qq.com', 'expiry': 1629989952.494398, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': 'work.weixin.qq.com', 'expiry': 1601045952.993515, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]

        # # 创建或打开一个数据库，shelve是python自带的数据库
        db = shelve.open("cookies")
        # 进行存储
        # db["cookies"] = cookies
        # 读取cookies
        cookies = db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            #把字典加入到driver的cookie中
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        db.close()