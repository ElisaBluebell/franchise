import urllib.request
url = "http://dalong.net/reviews/pg/p02/p/p02_01.jpg"
savename = "test.png"

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다...!")
