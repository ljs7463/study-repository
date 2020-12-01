# # 파이썬 클래스

# # 클래스 / 객체
# # 붕어빵 틀 / 붕어빵
# # 자동차 설계도 / 자동차
# # 핸드폰 설계도 / 핸드폰


# class Unit:
#     def __init__(self, name, hp, damage):  #__init__ : 생성자 (마린이나, 탱크 같은객체가 만들어질 때 자동으로 호출되는 부분 )
#       self.name = name #멤버변수 : 어떤 클래스 내에 정의된 변수
#       self.hp = hp
#       self.damage = damage
#       print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#       print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5) #마린이나 탱크처럼 클래스로부터 만들어지는 것을 객체라고 칭함. 이때 마린과 탱크를 Unit클래스의 인스턴스 라고 칭함.
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# #레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print('유닛이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage)) #객체이름. 으로 멤버변수에 접근가능

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print('{0}는 현재 클로킹 상태입니다.'.format(wraith2.name))











# # 파이썬 메소드(클래스 내의 함수를 메소드 라고 칭함.)

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage): 
#       self.name = name 
#       self.hp = hp
#       self.damage = damage
#       print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#       print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# #공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage): 
#       self.name = name 
#       self.hp = hp
#       self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 파괴되었습니다.'.format(self.name))

# # 파이어뱃 
# firebat1 = AttackUnit("파이어뱃", 50, 16) #클래스로 초기화 시켜주는것(따라서 생성자 함수가 무조건 있어야함)
# firebat1.attack("5시") # attack함수 보면 location만 받고 나머지는 기존에 초기화해둔 값을 가져오므로 그대로 가지고 오면됨.
# firebat1.damaged(30)
# firebat1.damaged(10)  
# firebat1.damaged(10)















# # 상속
# # 일반유닛 클래스와 공격유닛 클래스 둘다 self.name과 self.hp 는 두 클래스에 존재 이때 유닛클래스를 상속받아서 공격유닛을 만들어보기


# #일반 유닛
# class Unit:
#     def __init__(self, name, hp): 
#       self.name = name 
#       self.hp = hp
     

# #공격 유닛
# class AttackUnit(Unit):  #AttackUnit은 Unit 클래스를 상속 받아서 만들어 졌다는 의미
#     def __init__(self, name, hp, damage): 
#       Unit.__init__(self, name, hp) #여기에 Unit에서 만들어준 생성자를 호출 해줌 
#       self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 파괴되었습니다.'.format(self.name))

# #매딕 : 의무병

# # 파이어뱃 
# firebat1 = AttackUnit("파이어뱃", 50, 16) #클래스로 초기화 시켜주는것(따라서 생성자 함수가 무조건 있어야함)
# firebat1.attack("5시") # attack함수 보면 location만 받고 나머지는 기존에 초기화해둔 값을 가져오므로 그대로 가지고 오면됨.
# firebat1.damaged(30)
# firebat1.damaged(10)  
# firebat1.damaged(10)











# #다중상속
# #일반 유닛
# class Unit:
#     def __init__(self, name, hp): 
#       self.name = name 
#       self.hp = hp
     

# #공격 유닛
# class AttackUnit(Unit):  
#     def __init__(self, name, hp, damage): 
#       Unit.__init__(self, name, hp) 
#       self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 파괴되었습니다.'.format(self.name))
# # 날 수 있는 기능을 가진 클래스
# class Flyable:  
#   def __init__(self, name, flying_speed):
#     self.name = name
#     self.flying_speed = flying_speed

#   def fly(self, location):
#     print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))

# # 공중 공격 유닛 클래스 
# class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속은 콤마로 구분
#   def __init__(self, name, hp, damage, flying_speed):
#     AttackUnit.__init__(self, name, hp, damage)
#     Flyable.__init__(self, name, flying_speed)

# #발키리: 공중공격 유닛 
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly( "3시") # 원래 fly함수는 name과 location 전달하면 되는데 Flyable 클래스 생성자에 name이 없어서 valkyrie.name으로 써준다










# # 연산자 오버로딩(자식클래스에서 정의한 메소드를 쓰고싶을때 메소드를 새롭게 정의해서 사용할 수 있음)

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): 
#       self.name = name 
#       self.hp = hp
#       self.speed = speed
                             
#     def move(self, location):
#       print("[지상 유닛 이동]")
#       print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# #공격 유닛
# class AttackUnit(Unit):  
#     def __init__(self, name, hp, speed, damage): 
#       Unit.__init__(self, name, hp, speed) 
#       self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 파괴되었습니다.'.format(self.name))
# # 날 수 있는 기능을 가진 클래스
# class Flyable:  
#   def __init__(self, name, flying_speed):
#     self.name = name
#     self.flying_speed = flying_speed

#   def fly(self, name,  location):
#     print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))

# # 공중 공격 유닛 클래스 
# class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속은 콤마로 구분
#   def __init__(self, name, hp, damage, flying_speed):
#     AttackUnit.__init__(self, name, hp, 0, damage) #지상  speed 0
#     Flyable.__init__(self, name, flying_speed)
#   def move(self, location): #move함수만으로 지상유닛 과 공중유닛 이동을 모두 가능하게 하기 위한 코드, 즉 move 재정의
#     print("[공중 유닛 이동")
#     self.fly(self.name, location)


# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 2)

# # 배틀크루저 : 공중 유닛, 체력,공격 다좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move('11')
# # battlecruiser.fly("9시")
# battlecruiser.move("9시")

# # 여기서 문제는 지상유닛은 move함수를 사용하고 공중유닛은 fly함수를 이용하여 이동을 시켜야 한다 그렇게 되면 매번 객체가 어떤 유닛인지 파악하고 써야함... 귀찮아..
# # 따라서 move함수 만으로 지상유닛이면 이동하고 공중유닛이면 날아가게 처리해야함...













# #pass
# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): 
#       self.name = name 
#       self.hp = hp
#       self.speed = speed
                             
#     def move(self, location):
#       print("[지상 유닛 이동]")
#       print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# #공격 유닛
# class AttackUnit(Unit):  
#     def __init__(self, name, hp, speed, damage): 
#       Unit.__init__(self, name, hp, speed) 
#       self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 파괴되었습니다.'.format(self.name))
# # 날 수 있는 기능을 가진 클래스
# class Flyable:  
#   def __init__(self, name, flying_speed):
#     self.name = name
#     self.flying_speed = flying_speed

#   def fly(self, name,  location):
#     print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))

# # 공중 공격 유닛 클래스 
# class FlyableAttackUnit(AttackUnit, Flyable): 
#   def __init__(self, name, hp, damage, flying_speed):
#     AttackUnit.__init__(self, name, hp, 0, damage) 
#     Flyable.__init__(self, name, flying_speed)
#   def move(self, location):
#     print("[공중 유닛 이동")
#     self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit):
#   def __init__(self, name, hp, location):
#     pass #pass의 의미는 아무것도 안하고 일단 넘어간다.(완선된거 처럼 보여지게 하고 넘어가기)

# # 서플라이 디폿 : 거문, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")















# # super
# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): 
#       self.name = name 
#       self.hp = hp
#       self.speed = speed
                             
#     def move(self, location):
#       print("[지상 유닛 이동]")
#       print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# #공격 유닛
# class AttackUnit(Unit):  
#     def __init__(self, name, hp, speed, damage): 
#       Unit.__init__(self, name, hp, speed) 
#       self.damage = damage
    
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
#         self.hp -= damage
#         print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 파괴되었습니다.'.format(self.name))
# # 날 수 있는 기능을 가진 클래스
# class Flyable:  
#   def __init__(self, name, flying_speed):
#     self.name = name
#     self.flying_speed = flying_speed

#   def fly(self, name,  location):
#     print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(self.name, location, self.flying_speed))

# # 공중 공격 유닛 클래스 
# class FlyableAttackUnit(AttackUnit, Flyable): 
#   def __init__(self, name, hp, damage, flying_speed):
#     AttackUnit.__init__(self, name, hp, 0, damage) 
#     Flyable.__init__(self, name, flying_speed)
#   def move(self, location):
#     print("[공중 유닛 이동")
#     self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit):
#   def __init__(self, name, hp, location):
#     #Unit.__init__(self, name, hp, 0) #이렇게 상속하여 할 수 도있지만
#     super().__init__(name, hp, 0) #super로 상속할 수 있는데 이때 self는 가져오지 않고 super뒤에 괄호 붙여준다. 하지만 문제는 다중상속할 때 발생한다. 다중상속때 super를 사용하면 첫번째 인자에 있는 상속자만 상속된다.
#     self.location = location













# # 예외 처리

# try:
#   print('나누기 전용 계산기입니다.')
#   num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#   num2 = int(input("두 번째 숫자를 입력하세요 : "))
#   print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#   print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#   print(err)
# except: # 지정해준 에러 이외의 것이 발생했을때
#   print('알 수 없는 에러가 발생하였습니다.')
# except Exception as err: # 지정하지 않은 에러가 무슨 에러인지 알고 싶을때
#   print('알 수 없는 에러가 발생하였습니다.')
#   print(err)


# # 에러 발생 시키기
# try:
#   print('한 자리 숫자 나누기 전용 계산기입니다.')
#   num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#   num2 = int(input('첫 번째 숫자를 입력하세요 : '))
#   if num1 >= 10 or num2 >= 10:
#     raise ValueError
#   print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
# except ValueError:
#   print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')


# 사용자 정의 예외처리
# class BigNumberError(Exception):
#   def __init__(self, msg):
#     self.msg = msg

#   def __str__(self):
#     return self.msg

# try:
#   print('한 자리 숫자 나누기 전용 계산기입니다.')
#   num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#   num2 = int(input('첫 번째 숫자를 입력하세요 : '))
#   if num1 >= 10 or num2 >= 10:
#     raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
#   print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
# except ValueError:
#   print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#   print('에러가 발생 하였습니다. 한 자리 숫자만 입력하세요.')
#   print(err)




# # finally
# class BigNumberError(Exception):
#   def __init__(self, msg):
#     self.msg = msg

#   def __str__(self):
#     return self.msg

# try:
#   print('한 자리 숫자 나누기 전용 계산기입니다.')
#   num1 = int(input('첫 번째 숫자를 입력하세요 : '))
#   num2 = int(input('첫 번째 숫자를 입력하세요 : '))
#   if num1 >= 10 or num2 >= 10:
#     raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))
#   print('{0} / {1} = {2}'.format(num1, num2, int(num1 / num2)))
# except ValueError:
#   print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#   print('에러가 발생 하였습니다. 한 자리 숫자만 입력하세요.')
#   print(err)
# finally:
#   print('계산기를 이용해 주셔서 감사합니다.')










# # 모듈 위치 찾기
# import inspect
# import random
# import numpy as np
# print(inspect.getfile(np))



# #패키지 설치하기
# 터미널 창에 pip install <원하는 패키지>
# pip list 하면 현재 가지고 있는 패키지 리스트

# #깔려있는 패키지 업그레이드
# pip install --upgrade <패키지 명>

# #패키지 삭제
# pip uninstall <패키지 명>


# #glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob('*.py')) #확장자가 py인 모든 파일

# #os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 디렉토리

# folder = "sample_dir"
# if os.path.exists(folder): #sample_dir이라는 폴더가 있으면 이 구문을 탄다
#     print('이미 존재하는 폴더입니다.')
#     #삭제할 떄는 OS.rmdir(folder)
# else: 
#     os.makedirs(folder) #폴더생성
#     print(folder, '폴더를 생성하였습니다.')


# print(os.listdir)

# import time
# print(time.localtime())
# print(time.strftime('%y-%m-%d %H : %M : %S'))

import datetime
# print('오늘 날짜는', datetime.date.today)

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days = 100)
print('우리가 만난지 100일은', today + td)

