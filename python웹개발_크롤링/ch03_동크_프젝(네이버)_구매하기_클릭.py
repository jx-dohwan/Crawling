from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # 새로 추가
import time
import os
import pyperclip

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 5)
chrome.get("https://shopping.naver.com")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_login_button"))).click() # 보이냐?
input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input#pw")))

# pip3 install pyperclip
pyperclip.copy("jx7789")
input_id.send_keys(Keys.CONTROL,"v")

pyperclip.copy("rh74!@EH06")
input_pw.send_keys(Keys.CONTROL,"v")
input_pw.send_keys("\n")


short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a#gnb_logout_button")))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("아이폰 케이스")
time.sleep(1) # 엔터가 안먹힐 수도 있기 때문에 설정한 것이다. 
search.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__]"))) # 앞에둬서 로딩이 될때까지 기다리게 한다.


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[class^=basicList_link__]"))).click()

time.sleep(2)

chrome.switch_to.window(chrome.window_handles[1])
# 스위치 해서 밖에서 찾는게 아니라 클릭되고 2번째[1] 탭에서 찾을 수 있도록 한다.
print(chrome.title)


chrome.quit()