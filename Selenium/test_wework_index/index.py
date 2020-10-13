from selenium.webdriver.common.by import By
from Selenium.test_wework_index.basepage import Base

from Selenium.test_wework_index.add_member import AddMember
from time import sleep

class Index(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):
        '''
        点击“添加成员”
        进入添加成员页面
        :return:
        '''
        def add_member_condition(x):
            elements_len = len(self.finds(By.ID,"username"))
            if elements_len<=0:
                self.find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
            return elements_len>0

        self.find(By.CSS_SELECTOR,'#menu_contacts').click()
        sleep(2)
        self.wait_for_condition(add_member_condition)
        self.find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        return AddMember(self._driver)


    def gogo_import_addresss(self):
        pass
    def goto_join_member(self):
        pass
