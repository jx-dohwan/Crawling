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
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[name=query]")
search.send_keys("아이폰 케이스\n") # 엔터 치는거 안되는데? 왜지? 일단 오타는 없는데

time.sleep(5)

# button = find(wait,"a.co_srh_btn")
# button.click()
# time.sleep(3)

chrome.close()
