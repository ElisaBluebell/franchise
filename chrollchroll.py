from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
import json

driver = webdriver.Chrome()
driver.implicitly_wait(300)
driver.get('https://nid.naver.com/nidlogin.login')
search_box1 = driver.find_element("name", "id")
search_box1.send_keys('id')
search_box2 = driver.find_element("name", "pw")
search_box2.send_keys('%pw')
search_box1.submit()

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

a = input()
