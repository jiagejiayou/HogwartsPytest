from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage


class OutdakaPage(BasePage):
    daka_loc = (MobileBy.XPATH,"//*[contains(@text,'次外出')]")
    verify_loc = (MobileBy.ID,'com.tencent.wework:id/os')
    def out_daka(self):
        self.find_click(self.daka_loc)
        return self
    def is_success(self):
        re = self.find(self.verify_loc).text
        return re