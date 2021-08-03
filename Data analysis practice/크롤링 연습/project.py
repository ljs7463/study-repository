from selenium import webdriver
from bs4 import BeautifulSoup
import selenium
import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
url = 'https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=latest'
res =requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
news = soup.find_all('a', attrs={'class':'title'})

for i in news:
    print(i.get_text())

//*[@id="_newsList"]/ul