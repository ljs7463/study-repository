import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#===============================================================================================================
# < 셀레니움 기본 조작 방법 > 

## 클래스 명으로 검색
# elem = browser.find_element_by_class_name("")

# elem = browser.find_element_by_id('query')
# elem = browser.find_elements_by_id('query') 복수개일때 s붙이기
# elem.click() 클릭한다.
# browser.back() 뒤로가기
# browser.forward() 앞으로 가기
# browser.refresh() 새로고침

# 엔터를 위해서는(=Keys.ENTER를 위해서는) -> from selenium.webdriver.common.keys import Keys
# elem.send_keys("~~") ~~로 작성
# elem.send_keys(Keys.ENTER) 엔터누르기
# browser.close() 현재 창 닫기
# browser.quit() 전체 창 닫기+

# elem = browser.find_elements_tag_name('query') # 태그검색/elements 복수개
# elem.get_attribute('href') # for문작성후 다음과같이 검색된 태그내에서 href속성 검색
# elem = browser.find_element_by_xpath('개발자도구에서 복사한것 붙여넣기')
#===============================================================================================================


# Chromedriver PATH
chromePath = "./chromedriver.exe"
browser = webdriver.Chrome(chromePath)

# 1. 네이버 이동
address = 'http://naver.com'
browser.get(address)

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. id, pw입력
logId = 'ljs7463'
logPass = 'wjdtjrdl1130!!'
browser.find_element_by_id('id').send_keys(logId)
time.sleep(1)
browser.find_element_by_id('pw').send_keys(logPass)

# 4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

time.sleep(3) # 화면이 바뀌고 전환을 기다리기 위한 시간
# 5. id 를 새로 입력

browser.find_element_by_id('id').clear() # 이전에 적은 아이디 지워준다.
browser.find_element_by_id('id').send_keys('my_id')

# 6. html 정보 출력
#print(browser.page_source) # 지금 페이지에 있는 모든 html소스를 출력 한다.

# 7. 브라우저 종료
browser.quit()
