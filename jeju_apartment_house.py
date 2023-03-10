# 웹사이트 연결
from selenium import webdriver
# 키 입력
from selenium.webdriver import Keys
# 경로 획득
from selenium.webdriver.common.by import By

# 매너
import time

def get_dom(query):
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait

    dom = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, query))

# 암묵적 대기
driver = webdriver.Chrome()
driver.implicitly_wait(1)

# 사이트 접속
driver.get('https://disco.re')

# 저장 파일명
file_name = "jeju_apartment_temp"

# CSV 파일 생성
f = open(f"{file_name}.csv", "w", encoding="utf-8")

# CSV 헤더 작성
f.write("num, store, address, house\n")

# 오픈 파일명
search_f = open("jeju_temple_list.csv", "r", encoding="utf-8")
a = 0

while True:
    line = search_f.readline()
    if a != 0:
        if not line:
            break
        driver.find_element(By.XPATH, """/html/body/span/div[131]/div[2]/div/div[3]/div[1]""").send_keys(Keys.ENTER)

        # 검색어 입력 칸 지정
        search_line = driver.find_element(
            By.XPATH, """//*[@id="top_search_ds_input"]"""
        )
        line = line.split(",")

        search_source = line[3]
        search_line.clear()

        # 검색어 입력 및 검색 실행
        search_line.send_keys(search_source)
        search_line.send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element(By.XPATH, """//*[@id="top_search"]/div[4]/div""").click()

        try:
            temp_house = driver.find_element(By.XPATH, """/html/body/div[10]/div/div[2]/div/div[5]/div[26]/div/div/div[15]/div[2]/div[2]/span[1]""")

            print("store: ", line[1], "address: ", line[3], "house: ", temp_house)

            f.write(
                f"""{a}, {line[1]}, {line[3]}, {temp_house}\n"""
            )
            break

        except:
            pass

    a += 1

search_f.close()
f.close()
print("저장 완료")
