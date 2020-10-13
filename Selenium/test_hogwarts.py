from selenium import webdriver
from time import sleep
class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        pass
    def teardown(self):
        self.driver.quit()
    def test_hogwarts(self):
        self.driver.get("http://www.testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        # sleep(5)
        self.driver.find_element_by_link_text("求职面试圈").click()

