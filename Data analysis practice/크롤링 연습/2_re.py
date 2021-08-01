# 정규식
# 교통사고가 나서 차번호 판을 보는데 번호판이 4자리의 문자로 이루어져있다고 가정할때
# 네자리가 다 기억안나고 세자리만 기억난다고 하자.(ca?e)이런식으로
# cafe가 될수도 care가 될수도 등등 많은 경우의수가있다.
import re 
p = re.compile('ca.e') 
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case (o) | caffe(x)
# ^ (^de)  : 문자열의 시작 -> desk, destination (o) | fade (x)
# $ (se$)  : 문자열의 끝 -> case, base (o) | face (x) 

# m = p.match('case')
# print(m.group()) # case가 위에있는 정규식에 매칭이 되어서 출력이 되었다, 매치되지 않으면 에러가 발생

# # 매칭 되지 않았을때 에러대신에 출력문으로 만들기
# if m:
#     print(m.group())
# else:
#     print('매칭되지 않음')

# 위의 과정을 함수로 만들어 보자

def print_match(m):
    if m:
        print('m.group():', m.group()) # 일치하는 문자열 반환
        print('m.string:', m.string) # 입력받은 문자열 반환
        print('m.start():', m.start()) # 일치하는 문자열의 시작 index
        print('m.end():', m.end()) # 일치하는 문자열의 끝 index
        print('m.span():', m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print('매칭되지 않음')

# m = p.match('cafe') # careless를 넣어주어도 care가 출력 즉, match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)


# m = p.search('good care') # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall('good care cafe') # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)





###### 정리 #######

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") :  주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# # 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case (o) | caffe(x)
# ^ (^de)  : 문자열의 시작 -> desk, destination (o) | fade (x)
# $ (se$)  : 문자열의 끝 -> case, base (o) | face (x) 