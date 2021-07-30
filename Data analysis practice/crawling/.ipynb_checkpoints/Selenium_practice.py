from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.get('https://www.dailyhotel.com')
elem = browser.find_element_by_class_name("swiper-wrapper") 
comon = elem.get_attribute('href')
print(comon)

