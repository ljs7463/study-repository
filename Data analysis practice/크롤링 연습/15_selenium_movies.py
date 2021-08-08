# 동적 크롤링
# 구글무비에서 정가에 줄을 그어 할인가격으로 표시되어있는 영화만 크롤링하기.

import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies?hl=ko&gl=US'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Accept-Language' : 'ko-KR,ko' # 한국언어로 페이지를 받기 
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs={'class':'WHE7ib.mpg5gc'})
print(len(movies)) # 정보를 찾을 수 없다고 뜬다.


# # html을 직접 파일로 저장해서 확인해 보기
# with open('movie.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify()) 