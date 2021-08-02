from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=latest')
browser.implicitly_wait(3)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
elem = soup.find_all(class_='news_list')

breakpoint()
