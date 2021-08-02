import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음으로 발견되는 a태그를 뿌려줘!!
# print(soup.a.attrs) # a element 의 속성정보를 확인하기
# print(soup.a['href']) # a element 의 href 속성 '값' 정보를 출력

# 위에 것들은 해당페이지의 html정보에 대한 이해도가 높을때 바로바로 쉽게 입력해서 찾는방법이다.
# 하지만 처음 본 페이지의 경우 어떻게 html이 구성되어 있는지 모른다.

# print(soup.find('a', attrs={'class':'Nbtn_upload'})) # 클래스 값이 'Nbtn_upload' 인 a element 를 찾아줘
# # soup.find() : 괄호안에 입력해준 정보에 따라 처음으로 발견되는 것을 출력

rank1 = soup.find('li', attrs = {'class':'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling 
# print(rank1.parent)
# rank2 = rank1.find_next_sibling('li') n # "li" element 기준으로 다음것을 찾는것
# print(rank2.a.get_text())
# rank1 = rank2.find_previous_sibling('li')
# print(rank1.a.get_text())

print(rank1.find_next_siblings('li')) # 다음 형제들을 모두 가져오는것 siblings

webtoon = soup.find('a', text ='싸움독학-90화 : 유도와 싸워 이기는 법' ) # text를 통해 가져올 수도 있음.
print(webtoon)