from appium.webdriver.common.mobileby import MobileBy

from weixin_appium.pages.base import BasePage


class ManualAddPage(BasePage):

    name_loc = (MobileBy.ID,"com.tencent.wework:id/b3c")
    gender_loc = (MobileBy.XPATH,"//*[@text='性别']/..//*[@text='男']")
    male_loc = (MobileBy.XPATH, "//*[@text='男']")
    female_loc = (MobileBy.XPATH, "//*[@text='女']")
    phone_loc = (MobileBy.ID, "com.tencent.wework:id/fiv")
    save_loc = (MobileBy.XPATH, "//*[@text='保存']")

    def set_name(self, name):
        self.find_sendkeys(self.name_loc,name)
        return self

    def set_gender(self, gender):
        gender = self.find_click(self.gender_loc)
        if gender == '男':
            self.find_click(self.male_loc)
        else:
            self.find_click(self.female_loc)
        return self

    def set_phone(self, phone):
        self.find_sendkeys(self.phone_loc,phone)
        return self

    def click_save(self):
        self.find_click(self.save_loc)
        from weixin_appium.pages.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)
