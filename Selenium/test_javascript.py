import pytest

from Selenium.base import Base
from time import sleep
class TestJS(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("selenium")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/strong/span[2]").click()
        sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(code)
            # print(self.driver.execute_script("return document.title;eturn JSON.stringify(performance.timing"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)