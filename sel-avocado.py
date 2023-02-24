# BeautifulSoup lib import
from bs4 import BeautifulSoup
# 파일 열기
fp = open("fruits-vegetables.html", encoding="utf-8")
# 분석
soup = BeautifulSoup(fp, "html.parser")

# 선택된 문자열 프린트 람다식
sel = lambda q : print(soup.select_one(q).string)

# 근데 하나밖에..ㅎㅎ;;
sel("#ve-list > li:nth-of-type(4)")
# 이하 교재 예제(해당 예제는 print(soup.select_one(q값)).string) 사용함
print(soup.select("#ve-list > li.black")[1].string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)

# find 메서드로 추출하기
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)

#find 메서드를 연속적으로 사용하기
print(soup.find(id="ve-list").find("li", cond).string)
