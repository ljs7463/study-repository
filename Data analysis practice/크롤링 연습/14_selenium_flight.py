from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

time.sleep(1)
browser.find_elements_by_class_name('sc-crzoAE.hnpClg.inner')[26].click()
browser.find_elements_by_class_name('sc-crzoAE.hnpClg.inner')[27].click()
# browser.find_elements_by_link_text("27")[0].click() # 이번달 달력[0]
# browser.find_elements_by_link_text("28")[0].click() # 이번달 달력[0]
#find_elements_by_link_text 는 엥커태그(a)안에있는 text를 지정해서 찾을 수 있음(엥커태그 한정!!)


# 다음달 27일, 28일 선택

time.sleep(1)
next_month = browser.find_elements_by_class_name('sc-kEqXSa.bAVzgZ.month')[1]
time.sleep(1)
next_month.find_elements_by_class_name('sc-crzoAE.hnpClg.inner')[26].click()
next_month.find_elements_by_class_name('sc-crzoAE.hnpClg.inner')[27].click()



# 이번달 27일, 다음달 28일 선택

time.sleep(1)
these_month = browser.find_elements_by_class_name('sc-kEqXSa.bAVzgZ.month')[0]
these_month.find_elements_by_class_name('sc-crzoAE.hnpClg.inner')[26].click()
time.sleep(1)
next_month = browser.find_elements_by_class_name('sc-kEqXSa.bAVzgZ.month')[1]
next_month.find_elements_by_class_name('sc-crzoAE.hnpClg.inner')[27].click()


# 인기여행지중 4번째에 있는것 클릭 
time.sleep(1)
travel = browser.find_element_by_class_name('Popular_list__3QyU6')
travel.find_elements_by_tag_name('li')[3].click()

#  항공권 검색후 로딩창이 나타났을경우

# 1. time.sleep()을 통한 기다림
# 2. 기다리다가 창이 나타나면 바로 실행하게 하는것

# 2번째 경우의 수
travel = browser.find_element_by_class_name('Popular_list__3QyU6')
travel.find_elements_by_tag_name('li')[3].click()

# 10초를 기다리는데 어떤 엘리먼트가 나올때까지 기다릴껀데 XPATH안에 들어간 값에 해당하는 element가 나올때까지(즉, 일찍나오면 빨리끝남)
# 10초 초과해도 안나오면 에러를 내고 종료시킨다
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(BY.XPATH('') )) 
    # 성공했을때 동작 수행
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()
    # 실패하면 창 종료

