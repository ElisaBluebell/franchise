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
driver.get('https://map.kakao.com/')

# 저장 파일명
file_name = "jeju_temple_review_score"

# CSV 파일 생성
f = open(f"{file_name}.csv", "w", encoding="utf-8")

# CSV 헤더 작성
f.write("num, store, address, review, score\n")

# 검색어 입력 칸 지정
search_line = driver.find_element(
    By.XPATH, """//*[@id="search.keyword.query"]"""
)


# 오픈 파일명
search_f = open("jeju_temple_list.csv", "r", encoding="utf-8")
a = 0

while True:
    line = search_f.readline()
    if a != 0:
        if not line:
            break
        line = line.split(",")
        search_source = line[2]

        search_line.clear()

        # 검색어 설정
        word = f"제주도 {search_source}"

        # 검색어 입력 및 검색 실행
        search_line.send_keys(word)
        search_line.send_keys(Keys.ENTER)
        time.sleep(0.1)
        try:
            for i in range(1, 7):
                temp_address = driver.find_element(
                    By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[5]/div[2]/p[1]"""
                ).text
                if line[4] in temp_address:

                    temp_score = driver.find_element(
                        By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[4]/span[1]/em[1]"""
                    ).text
                    if temp_score == "":
                        temp_score = "0"

                    temp_review = driver.find_element(
                        By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[4]/span[1]/a"""
                    ).text
                    temp_review = temp_review.replace("건", "")
                    if temp_review == "":
                        temp_review = "0"

                    print("store: ", search_source, "address: ", temp_address, "review: ", temp_review, "score: ",
                          temp_score)

                    f.write(
                        f"""{a}, {search_source}, {temp_address}, {temp_review}, {temp_score}\n"""
                    )
                    break

        except:
            pass

    a += 1

search_f.close()
f.close()
print("저장 완료")
