import requests
res = requests.get('http://google.com') # url불러오기
res.raise_for_status() # 정상적으로 불러왔는지 확인하는 코드( 이코드 이후 코드가 실행되지 않으면 정상적으로 불러오지 않은것)
print('>>> 정상적으로 불러오는데 성공하였습니다.')
print(f'>>> 가져온 html내의 텍스트는 {len(res.text)}개 입니다.')