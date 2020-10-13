from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage
from weixin_appium.pages.editinfo import EditInfo


class PersonInfo(BasePage):
    person_edit_loc = (MobileBy.ID,"com.tencent.wework:id/hxm")
    def goto_edit_page(self):
        self.find_click(self.person_edit_loc)
        return EditInfo(self.driver)