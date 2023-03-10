import collections
import requests
import time
import pymysql
# 웹사이트 연결
from selenium import webdriver
# 키 입력
from selenium.webdriver import Keys
# 경로 획득
from selenium.webdriver.common.by import By

start_time = time.time()

# 암묵적 대기
# driver = webdriver.Chrome()
# driver.implicitly_wait(0.3)

# 사이트 접속
# driver.get('https://map.kakao.com/')

# 검색어 입력 칸 지정
# search_line = driver.find_element(
#     By.XPATH, """//*[@id="search.keyword.query"]"""
# )

# DB 연동
conn = pymysql.connect(host="10.10.21.110", user="jeju_cafe", password="xlavmfhwprxm1", port=3306, database="jeju_cafe")
c = conn.cursor()


#카카오 API
def whole_region(keyword, start_x, start_y, end_x, end_y):
    page_num = 1
    # 데이터가 담길 리스트
    all_data_list = []

    while True:
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
        params = {'query': keyword, 'page': page_num,
                  'rect': f'{start_x},{start_y},{end_x},{end_y}'}
        headers = {'Authorization': 'KakaoAK 3e6f33dd880519c5be39333ce69e712a'}
        resp = requests.get(url, params=params, headers=headers)

        search_count = resp.json()['meta']['total_count']
        print('총 개수', search_count)

        if search_count > 45:
            print('좌표 4등분')
            dividing_x = (start_x + end_x) / 2
            dividing_y = (start_y + end_y) / 2
            ## 4등분 중 왼쪽 아래
            all_data_list.extend(whole_region(keyword, start_x, start_y, dividing_x, dividing_y))
            ## 4등분 중 오른쪽 아래
            all_data_list.extend(whole_region(keyword, dividing_x, start_y, end_x, dividing_y))
            ## 4등분 중 왼쪽 위
            all_data_list.extend(whole_region(keyword, start_x, dividing_y, dividing_x, end_y))
            ## 4등분 중 오른쪽 위
            all_data_list.extend(whole_region(keyword, dividing_x, dividing_y, end_x, end_y))
            return all_data_list

        else:
            if resp.json()['meta']['is_end']:
                all_data_list.extend(resp.json()['documents'])
                return all_data_list

            # 아니면 다음 페이지로 넘어가서 데이터 저장
            else:
                print('다음페이지')
                page_num += 1
                all_data_list.extend(resp.json()['documents'])


def overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y):
    # 최종 데이터가 담길 리스트
    overlapped_result = []

    # 지도를 사각형으로 나누면서 데이터 받아옴
    for i in range(1, num_x + 1):  ## 1,10
        end_x = start_x + next_x
        initial_start_y = start_y
        for j in range(1, num_y + 1):  ## 1,6
            end_y = initial_start_y + next_y
            each_result = whole_region(keyword, start_x, initial_start_y, end_x, end_y)
            overlapped_result.extend(each_result)
            initial_start_y = end_y
        start_x = end_x

    return overlapped_result


# 검색어, 시작 x 좌표 및 증가값
keywords = ['콘도', '음식점', '대형마트', '학교', '박물관', '전시관', '미술관', '영화관', '도서관', '교회', '성당', '사찰', '렌트카', '병원', '숙박업소', '관광명소', '공연장']

c.execute("DROP TABLE IF EXISTS jeju_total_list;")
conn.commit()

# 테이블 생성
c.execute(
    """CREATE TABLE jeju_total_list(
    num INT NOT NULL AUTO_INCREMENT,
    store TEXT NOT NULL,
    category_group TEXT NULL,
    category TEXT NULL,
    address TEXT NULL,
    x DOUBLE NOT NULL,
    y DOUBLE NOT NULL,
    review INT NULL,
    score DOUBLE NULL,
    PRIMARY KEY(num)
    )"""
)
conn.commit()

for keyword in keywords:
    start_x = 126.14
    start_y = 33.11
    next_x = 0.01
    next_y = 0.01
    num_x = 92
    num_y = 58

    overlapped_result = overlapped_data(keyword, start_x, start_y, next_x, next_y, num_x, num_y)

    # 최종 데이터가 담긴 리스트 중복값 제거
    results = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in overlapped_result)))
    f = open(f"{keyword}.csv", "w", encoding="utf-8")
    for item in results:
        f.write(f'{item["id"]}, '
        f'{item["place_name"]}, '
        f'{item["category_group_name"]}, '
        f'{item["road_address_name"]}, '
        f'{item["x"]}, {item["y"]}, '
        f'{item["category_name"]},'
        f'{item["address_name"]}\n')
    f.close()

    # 넘버
    num = 1

    # for place in results:
    #
    #     # 검색어 설정 및 검색창 초기화
    #     search_source = place['place_name']
    #     search_line.clear()
    #     # 검색어 설정
    #     word = f"제주도 {search_source}"
    #
    #     # 검색어 입력 및 검색 실행
    #     search_line.send_keys(word)
    #     search_line.send_keys(Keys.ENTER)
    #     time.sleep(0.1)
    #
    #     # 도로명 주소가 없을 경우 번지주소를 주소에 대입함
    #     if place['road_address_name'] == '':
    #         place['road_address_name'] = place['address_name']
    #
    #     try:
    #         for i in range(1, 7):
    #             temp_address = driver.find_element(
    #                 By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[5]/div[2]/p[1]"""
    #             ).text
    #             if place['road_address_name'] in temp_address:
    #
    #                 temp_score = driver.find_element(
    #                     By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[4]/span[1]/em[1]"""
    #                 ).text
    #                 if temp_score == "":
    #                     temp_score = "0"
    #
    #                 # 리뷰 평점 입력
    #                 temp_review = driver.find_element(
    #                     By.XPATH, f"""//*[@id="info.search.place.list"]/li[{i}]/div[4]/span[1]/a"""
    #                 ).text
    #
    #                 # 불필요한 문자 제거
    #                 temp_review = temp_review.replace("건", "")
    #
    #                 # 값이 없을 시 0으로
    #                 if temp_review == "":
    #                     temp_review = "0"
    #
    #                 # DB 입력
    #                 c.execute(
    #                     f"""INSERT INTO jeju_total_list VALUES(
    #                         {num},
    #                         "{place['place_name']}",
    #                         "{place['category_group_name']}",
    #                         "{place['category_name']}",
    #                         "{place['road_address_name']}",
    #                         {place['x']},
    #                         {place['y']},
    #                         {temp_review},
    #                         {temp_score}\n
    #                         )"""
    #                 )
    #                 conn.commit()
    #
    #     except:
    #         pass
    #
    #     # num 증가
    #     num += 1
    #     print(place, f"review: {temp_review}, score: {temp_score}")

# 소요시간 출력
end_time = time.time()
print(f"""{end_time-start_time}s""")

# 닫기
c.close()
conn.close()
driver.close()
