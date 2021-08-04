from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = 'https://beta-flight.naver.com/'
browser.get(url) # url로 이동
time.sleep(2)

# 가는 날 달력 선택
browser.find_element_by_class_name("tabContent_option__2y4c6.select_Date__1aF7Y").click()
#find_elements_by_link_text 는 엥커태그(a)안에있는 text를 지정해서 찾을 수 있음(엥커태그 한정!!)


# 이번달 27일, 28일 선택
calender = browser.find_element_by_class_name('sc-crzoAE.hnpClg.inner')
elem = calender.find_elements_by_tag_name('b')
print(elem.text)

# browser.find_elements_by_link_text("27")[0].click() # 이번달 달력[0]
# browser.find_elements_by_link_text("28")[0].click() # 이번달 달력[0]


# 나중에 해보기
