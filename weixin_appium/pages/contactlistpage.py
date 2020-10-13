from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.addmemberpage import AddMemberPage
from weixin_appium.pages.base import BasePage
from weixin_appium.pages.personinfo import PersonInfo


class ContactListPage(BasePage):

    text = "添加成员"
    search_loc = (MobileBy.ID,"com.tencent.wework:id/hxw")
    search_item_loc =(MobileBy.ID,"com.tencent.wework:id/ghu")
    search_result = (MobileBy.ID,"com.tencent.wework:id/e2a")
    def add_contact(self):
        """
        进入添加成员页面
        :return:
        """
        self.find_scroll(self.text).click()
        return AddMemberPage(self.driver)

    def search_contact(self,name):
        self.find_click(self.search_loc)
        self.find_sendkeys(self.search_item_loc,name)
        self.webdriver_wait(self.search_result,10)
        self.find_click(self.search_result)
        return PersonInfo(self.driver)