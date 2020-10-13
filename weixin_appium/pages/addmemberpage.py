from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage



class AddMemberPage(BasePage):

    add_button = (MobileBy.ID, "com.tencent.wework:id/cm5")
    toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_manual(self):
        from weixin_appium.pages.manualaddpage import ManualAddPage
        self.find_click(self.add_button)
        return ManualAddPage(self.driver)

    def get_toast(self):
        ele = self.webdriver_wait(self.toast_ele)
        result = ele.text
        return result

