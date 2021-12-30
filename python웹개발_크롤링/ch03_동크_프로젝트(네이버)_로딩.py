from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") # 여러창
#options.add_argument("headless") # 굳이 창 안보이게

chrome = webdriver.Chrome("./chromedriver.exe", options=options)
chrome.get("https://shopping.naver.com")
WebDriverWait(chrome, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"input[name=query]")))
chrome.close()
