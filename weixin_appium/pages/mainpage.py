from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage
from weixin_appium.pages.contactlistpage import ContactListPage
from weixin_appium.pages.workbenchpage import WorkBenchPage


class MainPage(BasePage):

    contact_ele = (MobileBy.XPATH, "//*[@text='通讯录']")
    workbench_ele = (MobileBy.XPATH, "//*[@text='工作台']")

    def goto_contactlist(self):
        """
        进入通讯录页面
        :return:
        """
        self.find_click(self.contact_ele)
        return ContactListPage(self.driver)

    def goto_workbench(self):
        """
        进入工作台
        :return:
        """
        self.find_click(self.workbench_ele)
        return WorkBenchPage(self.driver)