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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




# 암묵적 대기
driver = webdriver.Chrome()
driver.implicitly_wait(300)

wait = WebDriverWait(driver, 10)

# 사이트 접속
driver.get('https://hogangnono.com/search?q=%EC%A0%9C%EC%A3%BC%EB%8F%84%20%EA%B3%A0%EC%82%B0%EB%8A%98%ED%91%B8%EB%A5%B8%ED%8C%B0%EB%A6%AC%EC%8A%A4%EC%95%84%ED%8C%8C%ED%8A%B8')

geo_local = Nominatim(user_agent="South Korea")

# 검색어 입력 칸 지정
search_line = driver.find_element(
    By.XPATH, """/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[4]/div/fieldset/div[1]/div/input"""
)

# 오픈 파일명
search_f = open("jeju_apartment_list.csv", "r", encoding="utf-8")
a = 0

while True:
    line = search_f.readline()
    if a != 0:
        if not line:
            break
        line = line.split(",")
        search_source = line[1]
        # search_line.clear()
        # for i in range(20):
        #     try:
        #         search_line.send_keys(Keys.BACKSPACE)
        #     except:
        #         pass
        # 검색어 설정
        word = f"제주도 {search_source}"

        # 검색어 입력 및 검색 실행
        # try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[2]/fieldset/div/div[1]/button").click()
        search_line.send_keys(word)
        # except:
        #     pass
        # try:
        #     search_line.send_keys(Keys.ENTER)
        # except:
        #     pass
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[4]/div/fieldset/div[1]/div/button[2]").click()
        # if driver.find_element(
        #         By.XPATH, f"""//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]"""
        # ).text != "부동산":
        #     pass
        #
        # else:
        #     try:
        #         driver.find_element(
        #             By.XPATH, f"""//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]"""
        #         ).send_keys(Keys.ENTER)
        #
        #         wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH))
        #         # wait.until(EC.number_of_windows_to_be(2))
        #
        #         # driver.switch_to.new_window('tab')
        #
        #
        #         temp_house = driver.find_element(
        #             By.XPATH, f"""//*[@id="__next"]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div/div[1]"""
        #         ).text
        #         driver.close()
        #
        #         print("name: ", search_source, "address: ", line[2], "house: ",
        #               temp_house)
        #
        #     except:
        #         pass

    a += 1

search_f.close()
print("저장 완료")
