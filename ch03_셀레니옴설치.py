from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


browser = webdriver.Remote("http://172.17.0.2:4444/wd/hub", DesiredCapabilities.CHROME)
browser.get("http://naver.com")
print(browser.title,"안되나?")
browser.close()