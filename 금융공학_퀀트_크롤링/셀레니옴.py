from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://fastcampus.co.kr/"

driver = webdriver.Chrome("./chromedriver.exe")

driver.get(url)