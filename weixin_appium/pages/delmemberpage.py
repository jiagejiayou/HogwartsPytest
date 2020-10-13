from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage


class DelMemberPage(BasePage):
    del_button = '删除成员'
    confirm_loc = (MobileBy.XPATH,"//*[@text='确定']")
    def del_member(self):
        self.find_scroll(self.del_button).click()
        self.webdriver_wait(self.confirm_loc,10)
        self.find_click(self.confirm_loc)
        from weixin_appium.pages.contactlistpage import ContactListPage
        return ContactListPage(self.driver)
