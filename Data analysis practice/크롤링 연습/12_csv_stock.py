# 시가총액 데이터를 크롤링해서 csv파일로 저장하기
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

filename = '시가총액1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') # 한글깨질때 utf-8-sig로 바꿔서해보기
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split('\t')
writer.writerow(title)

for page in range(1, 5): # 1, 5페이지 가져오기
    res = requests.get(url+str(page))
    res.raise_for_status
    soup = BeautifulSoup(res.text,'lxml')

    data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1: #의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data) # 리스트 형태로 넣어주어야한다.