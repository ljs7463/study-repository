# 데스크탑으로 페이지를 열어보는 것과 모바일로 열어볼때 페이지가 다르다, 
# 이것은 각각이 저장된 헤더값이 있기때문인데, 크롤링으로 접속했을때 사이트 입장에서는
# 차단을 할 수 있다.(ex)403에러)

import requests
# https://www.whatismybrowser.com/detect/what-is-my-user-agent 여기접속해서 얻는 나의 user-agent값
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
url = 'https://nadocoding.tistory.com'
res = requests.get(url, headers= headers) 
res.raise_for_status() 
res



