from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = ''
browser.get(url)

# 스크롤 내리기
browser.execute_script('window.scrollTo(0,1080)')