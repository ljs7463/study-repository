import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=2019%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84')
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

images = soup.find_all('img', attrs={'class':'thumb_img'})
for image in images:
    print(image['src'])