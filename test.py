# import pymysql
#
# # 클라이언트로부터 받아온 x, y좌표의 값
# x = 126.723442
# y = 33.4534214
#
# conn = pymysql.connect(host="10.10.21.110", user="jeju_cafe", port=3306, password="xlavmfhwprxm1", database="1team_db")
# c = conn.cursor()
#
# # x좌표와 y좌표 대입
# c.execute(f"CALL in_one_kilometer({x}, {y})")
# result = c.fetchall()
# print(result)
#
# c.close()
# conn.close()


a = {"a": 4, "b": 5}
print(a)