import collections
import requests
import pandas as pd
import numpy as np
# 웹사이트 연결
from selenium import webdriver
# 키 입력
from selenium.webdriver import Keys
# 경로 획득
from selenium.webdriver.common.by import By
# 위도, 경도 획득
from geopy.geocoders import Nominatim
# 매너
import time

def get_dom(query):
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait

    dom = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, query))

# 암묵적 대기
driver = webdriver.Chrome()
driver.implicitly_wait(300)

# 사이트 접속
driver.get('https://map.kakao.com/')

geo_local = Nominatim(user_agent="South Korea")

# 저장 파일명
file_name = "jeju_hospital_review_score"

# CSV 파일 생성
f = open(f"{file_name}.csv", "w", encoding="utf-8")

# CSV 헤더 작성
f.write("name, address, review, score\n")

# 검색어 입력 칸 지정
search_line = driver.find_element(
    By.XPATH, """//*[@id="search.keyword.query"]"""
)


# 오픈 파일명
search_f = open("jeju_hospital_list.csv", "r", encoding="utf-8")
a = 0

while True:
    line = search_f.readline()
    if a != 0:
        if not line:
            break
        line = line.split(",")
        search_source = line[1]

        search_line.clear()

        # 검색어 설정
        word = search_source

        # 검색어 입력 및 검색 실행
        search_line.send_keys(word)
        search_line.send_keys(Keys.ENTER)
        time.sleep(0.1)

        try:
            temp_address = driver.find_element(
                By.XPATH, f"""//*[@id="info.search.place.list"]/li[1]/div[5]/div[2]/p[1]"""
            ).text

            temp_score = driver.find_element(
                By.XPATH, f"""//*[@id="info.search.place.list"]/li[1]/div[4]/span[1]/em[1]"""
            ).text

            temp_review = driver.find_element(
                By.XPATH, f"""//*[@id="info.search.place.list"]/li[1]/div[4]/a/em"""
            ).text

            print("name: ", search_source, "address: ", temp_address, "review: ", temp_review, "score: ",
                  temp_score)

            f.write(
                f"""{search_source}, {temp_address}, {temp_review}, {temp_score}\n"""
            )

        except:
            pass

    a += 1

search_f.close()
f.close()
print("저장 완료")
