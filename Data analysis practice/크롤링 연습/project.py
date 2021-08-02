from selenium import webdriver
from bs4 import BeautifulSoup
import selenium

browser = webdriver.Chrome()
browser.get('https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=latest')
browser.implicitly_wait(3)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
elem = soup.find_all(class_ ='news_list')
breakpoint()
for e in elem:
    print(e.a['href'])