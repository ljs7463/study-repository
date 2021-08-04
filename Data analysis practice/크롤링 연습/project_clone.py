from selenium import webdriver
from bs4 import BeautifulSoup
import selenium
import re
import requests

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
# url = 'https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=latest'
# res =requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')
# news = soup.find_all('div', attrs={'class':'news_list'})
# print(news)

# news_list = first_child.find_all('li')
# print(first_child.find_all('li'))


#####

browser = webdriver.Chrome()
browser.get("https://sports.news.naver.com/wfootball/news/index?isphoto=N&type=latest")

page = browser.page_source
soup = BeautifulSoup(page, 'html.parser')

news = soup.find('div', attrs={'class':'news_list'})
news_list = news.find_all('li')

first_news = news_list[0]
first_news_alt = first_news.find('a').find('img').attrs['alt']
breakpoint()
print(first_news_alt)
# elem = browser.find_element_by_class_name("new_list")
# print(elem)





# html = browser.page_source
# soup = BeautifulSoup(html, 'lxml')
# news = soup.find_ele
# first_child = news[0]
# news_list = first_child.find_all('li')
# first_news_list = news_list[0]

# print(news)

