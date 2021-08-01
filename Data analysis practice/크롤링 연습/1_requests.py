import requests
res = requests.get('http://google.com') # url불러오기
res.raise_for_status() # 정상적으로 불러왔는지 확인하는 코드( 이코드 이후 코드가 실행되지 않으면 정상적으로 불러오지 않은것)
print(len(res.text))
print(res.text)



