#FC버전
#numpy 수학, 과학 계산용 라이브러리

array( 배열 ): 여러 값들의 배열
2차원은 대괄호 두개

1D array = 1차원, 2D array = 2차원 ..
shape 과 axis 개념 중요!!

shape는 차원의 수를 확인
1차원 (3,) -> 1 x 3 의 배열
2차원 (4, 3) -> 4 x 3 의 배열
3차원 (2, 5, 3) -> 2 x 5 x 3 의 배열

axis는 기준이 되는 축
axis0 은 행 
axis1 은 열
axis 는 앞에서 부터 0, 1, 2
shape:(4,) 는 axis 0 이 4
shape:(2,3) 은 axis 0 이 2 1이 3 이다.

array 는 리스트와 다르게 한가지 타입만 가능
list 는 여러가지 타입이 대괄호 하나 안에 존재가능하지만
arr = np.array([1, 2, 3, 3.14])
이런경우에 >>> array([1. ,2., 3., 3.14])
이런식으로 출력이 된다. 즉 실수로 다같이 출력이 됨(dtype설정 안해줬을땐 정수가 실수를 따라감)

만약 int와 float타입이 혼재되어있지만, dtype을 지정한 경우
arr = np.array([1, 2, 3, 3.14], dtype = int)
>>> array([1, 2, 3, 3])

int 와 str이 혼재된 경우 >>> 문자열로 
arr = np.array([1, 3.14, '테디', '1234'])
>>> array(['1', '3.14', '테디', '1234'])
arr[0] + arr[1] >>> '13.14'

int와 str이 혼재되있고 int로 dype를 지정하면 그냥 오류,but 숫자를 문자열로 한것은 int로 변환됨

# 슬라이싱

<1차원>
arr([0, 1, 2, 3, 4, 5, 6, 7])
arr[0] >>>0

<2차원>
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]
                  [9, 10, 11, 12]])
arr2d.shape >>>(3, 4)
arr2d[0, 2] >>>3

행 을 모두 가져오려는 경우
arr2d[0, :] >>> array([1, 2, 3, 4])

열 을 모두 가져오려는 경우
arr2d([:, 2]) >>> array([3, 7, 11])

quiz) 부분적으로 가져오려는 경우
arr2d[:2, :] >>> [[1, 2, 3, 4]
                  [5, 6, 7, 8]]
arr2d[:2, 2:] >>> [[3, 4]
                   [7, 8]]

# Fancy 인덱싱
Fancy 인덱싱은 범위가 아닌 특정 index의 집합의 값을 선택하여 추출하고 싶을 때 활용합니다.
arr = np.array([10, 23, 2, 7, 90, 65, 32, 66, 70])

반드시 [추출하고 싶은 인덱스] 꺽쇠 괄호로 묶어준다.
변수 지정후 추출도 가능
idx = [1, 3, 5]
arr[idx] 
>>> array([23, 7, 65])

arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
arr2d[[0, 1], :]
>>> array([[1, 2, 3, 4],
           [5, 6, 7, 8]])

arr2d[:,[1, 2, 3]]
>>> array([[2, 3, 4],
           [6, 7, 8],
           [10, 11, 12]])

# 불리안 인덱싱
조건 필터링을 통하여 Boolean 값을 이용한 색인
arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

myTrueFalse = [True, False, True, False, True, False, True]

arr(myTrueFalse)
>>> array([1, 3, 5, 7])

arr2d > 2
>>> array([[False, False, True, True],
           [True, True, True, True],
           [True, True, True, True]])

arr2d[ arr2d > 2 ]
>>> array([ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2d[ arr2d < 5 ]
>>> array([1, 2, 3, 4])

즉, arr2d[조건필터]


arr = np.arange(1, 11) >>> array([1, 2, 3, 4..., = 10])
**이것을 키워드 인자로 사용하면**
arr = np.arange(start = 1, stop = 11) 
왜 키워드 인자를 사용하느냐면 나중에 복잡한 코드일때 이렇게 키워드 인자를 사용하면 
좀더 코드가 직관적으로 보이기 때문 또한 키워드 인자를 사용하면 순서도 상관없음
arr = np.arange(stop = 11, start = 1) 이렇게 사용해도 무관하다.

quiz) 홀수의 값만 생성(1부터 10사이의 숫자중에 홀수값 만 생성)
arr = np.arange(1, 11, 2)
arr = np.arange(start = 1. stop = 11, step = 2 )

# 정렬  (sort)
arr = np.array([1, 10, 5, 6, 2 ,4 ,3 ,8 ])
np.sort(arr)
기본적으로 오름차순 정렬을 수행한다.

내림차순으로 하고싶으면 np.sort(arr)[::-1]

하지만 이 값들은 유지가 되지 않는다.
값을 유지하고 싶으면 변수arr자체에 sort를 시켜주면 된다 arr.sort()
다른 방법으로는 새로운 변수에 대입한다 arr2 = np.sort(arr) 이런식으로 편한걸로 하면된다.
두번째 꺼를 추천함!!

# n차원 정렬
n차원 정렬은 어떤축(axis)을 중심으로 정열 할건지 정해줘야함
arr2d = array([[5,  6,  7,  8],
               [4,  3,  2,  1],
               [10, 9, 12, 11]])

np.sort(arr2d, axis =1) # 열 기준 정렬
>>>array([[5,  6,  7,  8],
          [1,  2,  3,  4],
          [0, 10, 11, 12]])

np.sort(arr2d, axis = 0) # 행 기준 정렬
>>>array([[4,  3,  2,  1],
          [5,  6,  7,  8],
          [10, 9, 12, 11]])

# index를 반환하는 argsort
arr2d = array([[5,  6,  7,  8],
               [4,  3,  2,  1],
               [10, 9, 12, 11]])
sort는 값을 출력 argsort는 인덱스를 출력
np.argsort(arr2d, axis = 1)
>>> array([[0, 1, 2, 3],
           [3, 2, 1, 0],
           [1, 0, 3, 2]])

np.argsort(arr2d, axis = 0)
>>> array([[1, 1, 1, 1],
           [0, 0, 0, 0],
           [2, 2, 2, 2]])

# Matrix  :  행렬
데이터 분석에 Matrix 빼놓고 이야기 할 수 없다.

덧셈  :  shape 이 같아야 한다, 같은 position 끼리 연산한다.
곱셉(dot)  :  맞닿는 shape 이 같아야 한다. ( 2x3 과 3x2 이런식, 결과값은 바깥 2x2shape이 나옴)

# sum 
a = np.array([[1, 2, 3],
              [2, 3, 4]])
np.sum(a, axis = 0)
>>> array([3, 5, 7])
np.sum(a, axis = 1)
>>> array([6, 9])


# 일반 곱셈 과 dot
일반 곱셈 
a = np.array([[1, 2, 3],
              [2, 3, 4]])
b = np.array([[3, 4, 5],
              [1, 2, 3]])
a * b = array([[3, 8, 15],
               [2, 6, 12]])

하지만 dot product는 다름
a = np.array([[1, 2, 3],
              [2, 3, 4]])
b = np.array([[1, 2],
              [3, 4],
              [5, 6]])
np.dot(a, b) 
array([[22, 28],
       [31, 40]])


# Broadcasting

a = array([1, 2, 3],
          [2, 3, 4]])
a  +  3 = array([4, 5, 6],
                [5, 6, 7])


**************************************************************************************************************************************************************************
import numpy as np

arr = np.array([1, 2, 3, 4], dtype = int)
list_data = [1, 2, 3]
array = np.array(list_data)

print(array)

print(array.size) # 배열의 크기
print(array.dtype) # 배열 원소의 타입
print(array[2]) # 인덱스 2 의 원소

#list로 부터 생성하기
mylist1 = [1, 2, 3, 4]
mylist2 = [[1, 2, 3 ,4]
            5, 6, 7, 8]]
arr1 = np.array(mylist1)
arr2 = np.array(mylist2)

arr1.shape
arr2.shape


0부터 3까지의 배열 만들기
array1 = np.arange(4)
array2 = np.zeros((4, 4), dtype = float ) # dtype를 넣으면 그타입에 맞게 만들어줌, 4곱하기4크기의 2차원배열을 만들고 모든값이 0으로 초기화되있으며 그 값들은 각각실수형 데이터를 가지고있다.
array3 = np.ones((3, 3), dtype = str) # 위와 같은데 1로 초기화 하고 타입은 문자열
print(array1)
print(array2)
print(array3)

0 부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0 ,10, (3, 3)) #randint는 끝자리 -1 까지
print(array4)


# 평균이 0이고. 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print(array5)


# 배열 합치기
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])
print(array3.shape)
print(array3)


# 배열 형태 바꾸기
array1 = np.array([1, 2, 3, 4])
array2 = array1.reshape((2, 2))

print(array2)


배열 세로 축으로 합치기
array1 = np.arange(4).reshape(1, 4)
array2 = np.arange(8).reshape(2, 4)

array3 = np.concatenate([array1, array2], axis = 0 ) #axis값으로 0을 넣으면 위의 행에 다음행에 데이터가 들어가게됨
print(array1)
print(array2)
print(array3)



# 배열 나누기
array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis = 1) # 열을기준으로 인덱스 2를 기준으로 반으로 쪼갠다
print(left.shape)
print(right.shape)
print(array)
print(left)
print(right)


# 넘파이 활용

# 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1 = array1, array2 = array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)

# Numpy 원소 오름차순 정렬

array = np.array([5, 9, 10, 3, 1])
array.sort()
print(array)
# 내림차순
print(array[::-1])


# 각 열을 기준으로 정렬
array  = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array)
array.sort(axis = 0)
print(array)

균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5)  # 0 과 10사이에 5개의 데이터
array = np.linspace(0, 10, 11)
print(array)

난수의 재연 (실행마다 결과 동일)
np.random.seed(7) #어떤값을() 기준으로 난수를 생성할것인지 정하는 코드 나중에 머신러닝 모델을 학습시킬떄 난수가 달라서 학습결과가 달라질 일 없음
print(np.random.randint(0, 10, (2, 3))) #이것만하면 실행때마다 다른 난수가 나오는데 위의코드땜에 동일한값으로 고정

# Numpy 배열 객체 복사
array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print(array1)
#이렇게 하면 array2 값이 변경된것이 array1에 영향을 미치지만
array1 = np.arange(0, 10)
array2 = array1.copy()
array2[0] = 99
print(array1)
#이렇게 해줌으로서 array1은 변하지 않는다.


# 중복된 원소 제거 
array = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array))

# 스칼라 값 과 브로드캐스트
# "스칼라" 란 수치가 하나 인 것을 말함, "브로드 캐스트" 란 스칼라 값이 앞에 계산하고자 하는 행렬과 같은형태로 확대되어 연산이 이루어지는 기능을 뜻함.
A = np.array([[1, 2], [3,4]])
B = np.array([10, 20])
print(A * B)

원소 접근
x = np.array([[51, 55], [14, 19], [0, 4]])
print(x)
print(x[0]) # 0행
print(x[0][1]) # (0, 1) 위치의 원소
for문 으로도 가능
for row in x:
    print(row)

넘파이는 지금까지의 방법외에도, 인덱스를 배열로 지정해 한번에 여러 원소에 접근할 수도 있습니다.
x = x.flatten() # flatten 은 x를 1차원 배열로 변환(평탄화)
print(x)
x[np.array([0, 2, 4])]
print(x[np.array([0, 2, 4])])
print(x > 15)
print(x[x > 15])

**************************************************************************************************************

simple practice

# 1.각 요소의 차이가 10이되도록 100에서 200 사이의 범위에서 5X2 정수 배열을 만듭니다.

try -> 
arr1 = np.linspace(100,200,10, dtype =int)
print(arr1)
arr2 = np.reshape(arr1,(5,2))
print(arr2)


arr1 = np.linspace(100,200,11, dtype =int)
print(arr1)
arr2 = np.reshape(arr1,(5,2))
print(arr2)


arr1 = np.linspace(100,200,11, dtype =int)
print(arr1)
arr2 = np.reshape(arr1,(5,2))
print(arr2)

answer -> 
arr1 = np.arange(100,200,10)
print(arr1)
arr2 = arr1.reshape((5, 2))
print(arr2)

must ->
*arange*
홀수의 값만 생성(1부터 10사이의 숫자중에 홀수값 만 생성)
arr = np.arange(1, 11, 2)
arr = np.arange(start = 1. stop = 11, step = 2 )

*linspace*
균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5)  # 0 과 10사이에 5개의 데이터
array = np.linspace(0, 10, 11)
print(array)

*reshape*
array1 = np.array([1, 2, 3, 4])
array2 = array1.reshape((2, 2))

# 2.다음은 제공된 numPy 배열입니다. 모든 행에서 세 번째 열의 항목 배열을 반환합니다.

sampleArray = numpy.array ([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

answer ->
arr= np.array ([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(arr)
arr2=arr[:,2] 
print(arr2)

# 3.다음은 홀수 행과 짝수 열의 주어진 numpy 배열 반환 배열입니다.

arr = np.array ([[3, 6, 9, 12], [15, 18, 21, 24], 
[27,30, 33, 36], [39,42, 45, 48], [51,54, 57, 60]])


