import selenium
from selenium import webdriver
def test_open_url():
    driver = webdriver.Chrome()
    driver.get("https:testerhome.com/")

