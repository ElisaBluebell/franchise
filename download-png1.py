# 라이브러리 읽어 들이기 --- (※1)
import urllib.request

# URL과 저장 경로 지정하기
url = "http://dalong.net/reviews/pg/p02/p/p02_01.jpg"
savename = "test.png"

# 다운로드 --- (※2)
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")
