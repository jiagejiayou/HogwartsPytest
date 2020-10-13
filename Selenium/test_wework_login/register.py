from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    '''
    注册po
    '''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        '''
        输入内容
        点击下拉框
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys("我是来测试的")
        self.driver.find_element(By.CSS_SELECTOR, "#manager_name").send_keys("admin")
        self.driver.find_element(By.XPATH, '//*[@id="iagree"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="submit_btn"]').click()
        return True
