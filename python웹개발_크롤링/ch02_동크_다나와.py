from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import time
import os

chrome = webdriver.Chrome("./chromedriver.exe")
wait = WebDriverWait(chrome, 10)

# 보이지 않더라도 존재하는 것을 가져온다.
def find_present(css):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))

# 여러개를 반환
def finds_present(css):
    find_present(css) # 기다림
    return chrome.find_elements_by_css_selector(css) # 여러개 반환

# 보이는 것을 가져온다.
def find_visible(css):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))

def finds_visible(css):
    find_visible(css)
    return chrome.find_elements_by_css_selector(css)   

category = {
    "cpu":"873",
    "메인보드":"875",
    "메모리":"874",
    "그래픽카드":"876",
    "ssd":"32617",
    "케이스":"879",
    "파워":"880",
}

category_css = {
    c: "dd.category_" + category[c]+" a" for c in category
}

chrome.get("http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti")  

# mainboard = find_visible("dd.category_" + category["메인보드"]+" a" )  

# mainboard.click()

find_visible(category_css["cpu"]).click()
time.sleep(1)

# cpu 제조사 불러오기
lists = finds_visible("ul.search_cate_list li")
for list in lists:
    print(list.text)

time.sleep(5)

chrome.quit() # quit와 close의 차이를 알아야 함
