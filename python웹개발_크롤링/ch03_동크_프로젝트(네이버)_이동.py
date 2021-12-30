from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") # 여러창
#options.add_argument("headless") # 굳이 창 안보이게

chrome = webdriver.Chrome("./chromedriver.exe", options=options)
chrome.get("https://naver.com")
chrome.get("https://shopping.naver.com")
chrome.back()
chrome.forward()
time.sleep(3)
chrome.close()
