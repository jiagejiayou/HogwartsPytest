import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

with open("../datas/add_contact.yaml") as f:
    datas = yaml.safe_load(f)
class TestDada:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "88Y5T19C26009612"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'    # 跳过设备初始化
        caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        caps['settings[waitForIdleTimeout]'] = 0

        # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    """
    打卡
    """
    def test_daka(self):
        """
        1.打开【企业微信】应用
        2. 等待直到进入到主页
        3. 点击下方的导航栏中的【工作台】，进入到工作台
        4. 在页面上查找【打卡】标签，点击打卡。进入到打卡页面
        5. 验证【你已在打卡范围】文本存在
        6. 点击‘更新打卡’（如果有），然后点击【打卡】（上班打卡或下班打卡）
        7. 如果有弹框，点击【确认打卡】，验证打卡成功
        :return:
        """
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hiy").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        result = self.driver.find_element(MobileBy.ID,
                                          'com.tencent.wework:id/os').text
        assert '打卡成功' in result

    """
    添加联系人
    """
    @pytest.mark.parametrize("name,gender,phone",datas
                             )

    def test_add(self,name,gender,phone):
        """
        1. 点击【通讯录】
        2. 点击【添加成员】
        3. 点击【手动输入添加】
        4. 填写内容，点击【保存】
        5. 验证toast【添加成功】
        6. 返回通讯录
        :return:
        """
        # name = '阿尔法'
        # gender = '男'
        # phone = '15378946321'
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cm5").click()

        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b3c").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/..//*[@text='男']").click()
        if gender=='男':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fiv").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gkt").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        re= self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        assert '添加成功' in re
        self.driver.back()

    """删除联系人"""
    def test_delete(self):
        """
        1.进入【通讯录】页面
        2.点击要删除的成员，进入个人信息页面
        3. 点击右上方
        4. 点击【编辑成员】
        5. 在编辑成员页面点击【删除成员】
        6. 在弹框中选择【确定】
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("zhang h").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hxm").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()

    def test_search(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hxw").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ghu").send_keys("Ailsa")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/e2a").click()
        time.sleep(5)

