import time
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://events.interpark.com/exhibition?exhibitionCode=201215006')
page = browser.page_source
soup = BeautifulSoup(page, 'html.parser')

discounts = soup.find('div', attrs={'class':'inner'}).find_all('a')
for discount in discounts:
    print("호텔 명 :", discount['gtm-label'].split('>')[2])
    print("내용 :", discount.find('div', attrs={'class':'contentWrap'}).find_all('li'))# string추출 작업 해야함.
    print("주소 :", discount.attrs['href'])
    print("이미지 :", discount.find('img').attrs['src'])# 이미지로 바꾸기
    print('-'*100)


