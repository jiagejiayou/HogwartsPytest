from  time import sleep
from Selenium.base import Base

class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text('登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)#所有窗口
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('12qttwet3')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('18628359755')
        sleep(3)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('12qttwet3')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('1234566')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()

        sleep(3)

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)