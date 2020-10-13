from appium import webdriver

from weixin_appium.pages.base import BasePage
from weixin_appium.pages.mainpage import MainPage


class App(BasePage):
# class App:
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "88Y5T19C26009612"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            caps['dontStopAppOnReset'] = 'true'  # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 0

            # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
           self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch()

    def stop(self):
        self.driver.quit()


    def goto_main(self):
        '''进入首页'''
        return MainPage(self.driver)
