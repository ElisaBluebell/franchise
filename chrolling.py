from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
import json
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(300)
# driver.get('https://map.naver.com/v5/search/%EC%A0%9C%EC%A3%BC%EB%8F%84%EC%B9%B4%ED%8E%98?c=10,0,0,0,dh')
# search_box1 = driver.find_element("name", "id")
# search_box1.send_keys('selfishracer')
# search_box2 = driver.find_element("name", "pw")
# search_box2.send_keys('%EyeCon12')
# search_box1.submit()

driver.get('https://map.kakao.com/')
search_line = driver.find_element(By.XPATH, """//*[@id="search.keyword.query"]""")
search_line.send_keys("제주도 카페")
search_line.send_keys(Keys.ENTER)

time.sleep(1)

driver.find_element(By.XPATH, """//*[@id="info.search.place.more"]""").send_keys(Keys.ENTER)
page = driver.find_element(By.XPATH, """//*[@id="info.search.place.cnt"]""").text
page = page.replace(",", "")
temp_page = int(page)
page = (temp_page // 15) + 1

f = open("jeju_cafe_list.csv", "w", encoding="utf-8")
f.write("업소명, 주소, 리뷰")

for j in range(1, page + 1):
    for i in range(1, 16):
        temp_address = driver.find_element(By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[5]/div[2]/p[1]""").text
        temp_name = driver.find_element(By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[3]/strong/a[2]""").text
        temp_review = driver.find_element(By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[4]/a/em""").text
        if temp_address[:6] == "제주특별자치":
            print("카페명: ", temp_name, "카페 주소: ", temp_address, "리뷰 갯수: ", temp_review)
            f.write(temp_name + "," + temp_address + "," + temp_review + "\n")
            time.sleep(0.5)

    if page % 5 == 0:
        driver.find_element(By.XPATH, """// *[ @ id = "info.search.page.next"]""").send_keys(Keys.ENTER)
        time.sleep(1)

    else:
        driver.find_element(By.XPATH, f"""//*[@id="info.search.page.no{(j % 5) + 1}"]""").send_keys(Keys.ENTER)
        time.sleep(1)

    page += 1

f.close()

# HTMl 분석하기 --- (※2)
# soup = BeautifulSoup(html, 'html.parser')

# 필요한 부분을 CSS 쿼리로 추출하기
# 타이틀 부분 추출하기 --- (※3)
# h1 = soup.select_one("div#meigen > h1").string
# print("h1 =", h1)
# url = ""

a = input()
