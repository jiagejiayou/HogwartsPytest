from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage
from weixin_appium.pages.delmemberpage import DelMemberPage


class EditInfo(BasePage):
    edit_mem_loc = (MobileBy.XPATH,"//*[@text='编辑成员']")
    def edit_member(self):
        self.find_click(self.edit_mem_loc)
        return DelMemberPage(self.driver)