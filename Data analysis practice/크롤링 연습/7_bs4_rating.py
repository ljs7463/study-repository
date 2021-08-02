import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=736277&weekday=sun'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# 평점 구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    #rate = cartoon.strong.get_text() # 이렇게도 가능하다.
    print(rate)
    total_rates += float(rate)
print('전체 점수 :', total_rates)
print('평균 점수 :', total_rates/len(cartoons))