from selenium import webdriver
import time


browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")
time.sleep(10)
browser.close()