# 카카오맵 크롤링 프로그램

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

# 암묵적 대기
driver = webdriver.Chrome()
driver.implicitly_wait(300)

# 사이트 접속
driver.get('https://map.kakao.com/')

geo_local = Nominatim(user_agent="South Korea")

# 검색어 설정
word = "제주도 펜션"
# 검색어 입력 칸 지정
search_line = driver.find_element(
    By.XPATH, """//*[@id="search.keyword.query"]"""
)

# 검색어 입력 및 검색 실행
search_line.send_keys(word)
search_line.send_keys(Keys.ENTER)
time.sleep(1)

# 검색 기록 확장(카카오맵의 경우 확장을 해야 페이지 이동이 가능)
driver.find_element(
    By.XPATH, """//*[@id="info.search.place.more"]"""
).send_keys(Keys.ENTER)
time.sleep(1)

# 페이지 수 정의
page = driver.find_element(
    By.XPATH, """//*[@id="info.search.place.cnt"]"""
).text
page = page.replace(",", "")
temp_page = int(page)

# 페이지당 15건 출력되므로 // 15, 15건이 넘어갈 경우 다음 페이지 + 1
page = (temp_page // 15) + 1

# 파일명
file_name = "jeju_pension_list"

# CSV 파일 생성
f = open(f"{file_name}.csv", "w", encoding="utf-8")

# CSV 헤더 작성
f.write("업소명, 주소, 리뷰, 위도, 경도\n")

# # 시도명 선택
# driver.find_element(By.XPATH, """//*[@id="localInfo.map.province"]""").send_keys(Keys.ENTER)
# time.sleep(1)
#
# # 제주도
# driver.find_element(By.XPATH, """//*[@id="localInfoList.province.list"]/li[17]/a""").send_keys(Keys.ENTER)
# time.sleep(1)
#
# # 시군구명 선택
# driver.find_element(By.XPATH, """//*[@id="localInfo.map.county"]""").send_keys(Keys.ENTER)

for j in range(1, page + 1):
    for i in range(1, 16):
        try:
            temp_address = driver.find_element(
                By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[5]/div[2]/p[1]"""
            ).text

            # 위도, 경도 산출
            try:
                geo = geo_local.geocode(temp_address)
                temp_latitude = geo.latitude
                temp_longitude = geo.longitude

            # 데이처 산출 불가시 0, 0 입력
            except AttributeError:
                temp_latitude = 0
                temp_longitude = 0

            temp_name = driver.find_element(
                By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[3]/strong/a[2]"""
            ).text

            temp_review = driver.find_element(
                By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[4]/a/em"""
            ).text

            if temp_address[:6] == "제주특별자치":
                print("name: ", temp_name, "address: ", temp_address, "review: ", temp_review, "latitude: ",
                      temp_latitude, "longitude: ", temp_longitude)

                f.write(
                    temp_name + "," + temp_address + "," + temp_review + "," + temp_latitude + "," + temp_longitude + "\n"
                )
                time.sleep(1)

        except:
            pass

    if page % 5 == 0:
        driver.find_element(
            By.XPATH, """// *[ @ id = "info.search.page.next"]"""
        ).send_keys(Keys.ENTER)
        time.sleep(1)

    else:
        driver.find_element(
            By.XPATH, f"""//*[@id="info.search.page.no{(j % 5) + 1}"]"""
        ).send_keys(Keys.ENTER)
        time.sleep(1)

    page += 1

f.close()
print("저장 완료")