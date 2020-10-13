from weixin_appium.pages.base import BasePage
from weixin_appium.pages.dakapage import DaKaPage


class WorkBenchPage(BasePage):
    text = "打卡"
    def goto_daka(self):
        self.find_scroll(self.text).click()
        return DaKaPage(self.driver)
