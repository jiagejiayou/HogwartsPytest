from selenium.webdriver.common.by import By
from Selenium.test_wework_index.basepage import Base


class AddMember(Base):

    def add_member(self):
        # self._driver.find_element(By.ID,'username').send_keys("ceshiren")
        # self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("baba")
        # self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("13589632456")
        # self._driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        self.find(By.ID, 'username').send_keys("ceshiren2")
        self.find(By.ID, 'memberAdd_acctid').send_keys("baba")
        self.find(By.ID, 'memberAdd_phone').send_keys("13589632456")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

