from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage
from weixin_appium.pages.outdakapage import OutdakaPage


class DaKaPage(BasePage):
    waichudaka = (MobileBy.ID,"com.tencent.wework:id/hiy")
    def daka_task(self):
        self.find_click(self.waichudaka)
        return OutdakaPage(self.driver)