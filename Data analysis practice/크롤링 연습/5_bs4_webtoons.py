import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status() 

soup = BeautifulSoup(res.text, 'lxml')

# 네이버 웹툰 전체 목록 가져오기("find_all")
cartoons = soup.find_all('a', attrs={'class':'title'}) # 리스트로 반환된다.

# 모든 웹툰 전체 목록 출력
for cartoon in cartoons:
    print(cartoon.get_text())