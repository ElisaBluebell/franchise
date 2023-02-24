import urllib.request
url = "http://dalong.net/reviews/pg/p02/p/p02_01.jpg"
savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")