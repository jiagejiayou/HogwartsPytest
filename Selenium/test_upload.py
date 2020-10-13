from Selenium.base import Base
from time import sleep

class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("E:\PythonStd\HogwartsPytest\Selenium\home-pc_sucai.jpeg")
        sleep(3)