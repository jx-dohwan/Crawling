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
short_wati = WebDriverWait(chrome, 3)
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

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_logout_button")))

chrome.close