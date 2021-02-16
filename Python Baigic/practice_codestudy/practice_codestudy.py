# # 로또 번호 추출기 만들기

# from random import shuffle
# from time import sleep

# gamenum = input("로또 게임 회수를 입력하세요 : ")

# for i in range(int(gamenum)):
#     balls = [x + 1 for x in range(45)]
#     ret = []
#     for j in range(6):
#         shuffle(balls)
#         number = balls.pop()
#         ret.append(number)
#     ret.sort()
#     print("로또번호[%d]:" %(i + 1), end = "")
#     print(ret)
#     sleep(1)
#*****************************************************************************************
    # 남녀 파트너 정해주기 프로그램

# from random import shuffle

# male = ["슈퍼맨", "심봉사", "로미오", "이몽룡", "마루치"]
# female= ["원더우먼", "뻉덕", "줄리엣", "성춘향", "아라치"]
# shuffle(male)
# shuffle(female)
# couples = zip(male, female)

# for i, couple in enumerate(couples):
#     print("커플%d: [%s]-[%s]"%(i + 1, couple[0],couple[1]))
#*****************************************************************************************
# 데이터 처리하기 1(연도별 출생아 수 계산하기)

# def countBirths():
#     ret = []
#     for y in range(1880, 2016):
#         count = 0
#         filename = "yob%d.txt" %y
#         with open(filename,"r") as f:
#             data = f.readlines()
#             for d in data:
#                 if d[-1] == "\n":
#                     d= d[:-1]

#                 birth = d.split(",")[2]
#                 count += int(birth)
#         ret.append((y, count))
#     return ret #출생아 수 총합

# result = countBirths()
# with open("birth_by_year.csv","w") as f:
#     for year, birth in result:
#         data = "%s,%s\n"%(year, birth)
#         print(data)
#         f.write(data)
#****************************************************************************************

# 데이터 처리하기 2(연도별 성별 출생아 수 계산하기)
# def countBirthsBySex():
#     ret = []
#     for y in range(1880, 2016):
#         count_f = 0     #여자아기 출생아 수
#         count_m = 0     #남자아기 출생아 수
#         filename = "names/yob%d.txt" %y
#         with open(filename, "r") as f:
#             data = f.readlines()
#             for d in data:
#                 if d[-1] == "\n":
#                     d = d[:-1]

#                 tmp = d.split(",")
#                 sex = tmp[1]
#                 birth = tmp[2]

#                 if sex == "F":
#                     count_f += int(birth)
#                 else:
#                     count_m += int(birth)
#         ret.append((y, count_f, count_m))
#     return ret

# result = countBirthsBySex()
# with open("birth_by_sex.csv","w") as f:
#     for y, bf, bm in result:
#         data = "%s, %s, %s\n" %(y, bf, bm)
#         print(data)
#         f.write(data)

#**************************************************************

# 데이터 처리하기3(연도별 인기있는 상위 10개 성별 출생아 이름 구하기)
#???????
# from os.path import exists

# def getTop10BabyName(year):
#     nameF = {}
#     nameM = {}

#     filename = 'names/yob%s.txt'%year
#     if not exists(filename):
#         print('[%s] 파일이 존재하지 않습니다.'%filename)
#         return None

#     with open(filename, 'r') as f:
#         data = f.readlines()
#         for d in data:
#             if d[-1] =='\n':
#                 d = d[:-1]

            
#             tmp = d.split(',')
#             name = tmp[0]
#             sex = tmp[1]
#             birth = tmp[2]

#             if sex == 'F':
#                 ret = nameF
#             else:
#                 ret = nameM

#             if name in ret:
#                 ret[name] += int(birth)
#             else:
#                 ret[name] = int(birth)

#     retF = sorted(nameF.items(), key = lambda x:x[1], reverse = True)
#     retM = sorted(nameM.items(), key = lambda x:x[1], reverse = True)

#     for i, name in enumerate(retF):
#         if i > 9:
#             break
#         print('TOP_%d 여자아기이름: %s'%(i + 1, name))

#     for i, name in enumerate(retM):
#         if i > 9:
#             break
#         print('TOP_%d 남자아기이름: %s'%(i + 1, name))
        
# y = input('인기순 상위 10개 이름을 알고 싶은 출생년도를 입력하세요(예: 2001):')
# getTop10BabyName(y)

# 웹서버 로그 처리하기 1(총 페이지뷰 수 계산하기)


# #숫자와 문자를 분리하기
# my_list = ['a', 'b', 'n', 'x', 1, 2, 3, 'a', 'n', 'b']

# string = my_list[4:7]
# number = my_list[:4 & 7:]



# print(string)
# print(number)

# # zip 파일 압축 풀기
# from zipfile import*

# def extractZip(zipname):
#     with ZipFile(zipname, 'r') as ziph:
#         ziph.extractall()
#         print("[%s]가 성공적으로 추출되었습니다."%zipname)
    
# extractZip('files.zip')

# # 문장에 나타나는 문자 빈도수 계산하기 
# def getTextFreq(filename):
#     with open(filename, 'r') as f:
#         text = f.read()
#         fa = {}
#         for c in text:
#             if c in fa:
#                 fa[c] += 1
#             else:
#                 fa[c] = 1
#     return fa

# ret = getTextFreq('mydata.txt')
# ret = sorted(ret.items(), key = lambda x:x[1], reverse = True)
# for c,freq in ret:
#     if c =='\n':
#     continue
#     print('[%c] -> [%d]회 나타남'%(c, freq))


# 스택 구현하기 (append, pop)
# mystack = []

# def putdata(data):
#     global mystack
#     mystack.append(data)

# def popdata():
#     global mystack
#     if len(mystack) == 0:
#         return None
#     return mystack.pop()

# putdata('데이터1')
# putdata([3, 4, 5, 6])
# putdata(12345)

# print('<스택상태>:', end =""); print(mystack)

# ret - popdata()
# while ret !=None:
#     print('스택에서 데이터 추출:', end = ""); print(ret)
#     print('<스택상태>:', end = ""); print(mystack)
#     ret = popdata()
# ***************************************************************************************************************

# 표준 체중을 구하는 프로그램을 작성하시오

# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight 
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# def std_weight(height, gender):
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height * 21
    

# height = 175 #cm
# gender = '남자'
# weight = round(std_weight(height/100, gender), 2)

# print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))

# def std_weight(height, gender):
#     if gender == '남자':
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 175
# gender = '남자'
# weight = round(std_weight(height/100, gender), 2)
# print("키{0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))

# *******************************************************************************************************************

