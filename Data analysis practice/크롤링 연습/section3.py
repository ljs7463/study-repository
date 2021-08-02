from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.dailyhotel.com/')
browser.implicitly_wait(3)
html = browser.page_source

spongebob = BeautifulSoup(html, 'lxml')
spongebob.find_all('div', attrs={'class':'swiper-wrapper'})
breakpoint()
crab = spongebob.find_all('div', attrs={'class':'swiper-wrapper'})[2]
crab.a.get('href')
