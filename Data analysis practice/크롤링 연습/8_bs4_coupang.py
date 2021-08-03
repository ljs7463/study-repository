import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'} # 값을 잘 못받아 올 경우
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
#print(res.text)

items = soup.find_all('li', attrs={'class':re.compile('^search-product')})
#print(items[0].find('div', attrs={'class':'name'}).get_text())
for item in items:
    name = item.find('div', attrs={'class':'name'}).get_text() #제품명
    price = item.find('strong', attrs = {'class':'price-value'}).get_text() #가격

    rate = item.find('em', attrs = {'class':'rating'}) #평점
    if rate:
        rate = rate.get_text()
    else:
        rate = '평점 없음' 

    rate_count = item.find('span', attrs = {'class':'rating-total-count'}) # 평점 수
    if rate_count:
        rate_count = rate_count.get_text()
    else:
        rate_count = '평점 수 없음'
        
    print(name, price, rate, rate_count)