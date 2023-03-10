# separator.py -> 카테고리별 갯수를 출력하는 프로그램
# data 내 띄어쓰기에 주의할 것

import pymysql

# 클라이언트로부터 받아온 x, y좌표의 값
x = 126.47331737221904
y = 33.48660112476012

conn = pymysql.connect(host="10.10.21.110", user="jeju_cafe", port=3306, password="xlavmfhwprxm1", database="1team_db")
c = conn.cursor()

# x좌표와 y좌표 대입
c.execute(f"CALL in_one_kilometer({x}, {y})")
data = c.fetchall()

franchise = 0
total = {}

for line in data:
    # 딕셔너리가 비어있을 경우
    if total.keys() == "":
        # 카테고리가 아파트가 아니라면
        if line[3] != "아파트":
            # {해당 분류명: 1}로 일반적인 갯수 입력
            total[line[3]] = 1

        # 카테고리가 아파트일 경우
        else:
            # line[3]은 세대수의 위치, 세대수가 불명이 아닌 경우
            if line[7] != None:
                # {아파트: +=세대수}
                total[line[3]] += int(line[7])

    else:
        if line[3] in total.keys():
            if line[3] != "아파트":
                total[line[3]] += 1

            else:
                if line[7] != None:
                    total[line[3]] += int(line[7])

        else:
            total[line[3]] = 1

    # 프랜차이즈 업체명이 리스트에 있다면 franchise 변수 +1
    if "빽다방" in line[1]:
        franchise += 1

franchises = ["paikdabang", "starbucks"]
for store in franchises:
    score = 0
    query = f"SELECT * FROM {store}_coefficient;"
    c.execute(query)
    db_table = c.fetchall()
    for item in total:
        for coefficient in db_table:
            if coefficient[1] == item:
                score += total[item] * coefficient[2]

    print(f"{store} score: {score}")

c.close()
conn.close()
