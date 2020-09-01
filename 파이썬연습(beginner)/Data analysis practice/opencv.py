
# opencv 소개 및 기본 사용법 
영상처리와 컴퓨터 비전(컴퓨터에서 보여지는 분야 라고 생각하면 편함)을 위한 오픈소스 라이브러리
c, c++, python 등에서 사용
이미지를 파이썬 프로그램을 읽어서 처리를 해서 파일형태로 저장도 할 수 있음

# 이미지 읽어서 살펴보기

cv2.imread(file_name, flag)  :  이미지를 읽어 Numpy 객체로 만드는 함수
 - file_name: 읽고자 하는 이미지 파일
 - flag: 이미지를 읽는 방법 설정

 IMREAD_COLOR: 이미지를 Color로 읽고, 투명한 부분은 무시
 IMREAD_GRAYSCALE: 이미지를 Grayscale로 읽기
 IMREAD_UNCHANGED: 이미지를 Color로 읽고, 투명한 부분도 읽기(Alpha)

 반환 값: Numpy 객체 (행, 열, 생상: 기본 BGR)


cv2.imshow(title, image)  :  특정한 이미지를 화면에 출력합니다. (어떤 제목으로 어떤 이미지를 출력할지 설정하는것)
 - title : 윈도우 창의 제목
 - image : 출력할 이미지 객체


cv2.imwrite(file_name, image)  :  특정한 이미지를 파일로 저장하는 함수
 - file_name : 저장할 이미지 파일 이름
 - image : 저장할 이미지 객체

cv2.waitKey(time)  :  키보드 입력을 처리하는 함수
 - time: 입력 대기 시간(무한대기: 0)

 반환 값: 사용자가 입력한 Ascii code (ESC: 27)


cv2.destroyAllWindows()  :  화면의 모든 윈도우를 닫는 함수  (파이참 에서)


# 파이참에서 실행
import cv2

img_basic =cv2.imread('임정석.jpg', cv2.IMREAD_COLOR)
cv2.imshow('임정석.jpg', img_basic)
cv2.waitKey(0)

# 코렙에서 실행
from google.colab import files
uploaded = files.upload()  
>>>(파일선택)
# 위 코드는 구글코렙내에 있는 파일을 업로드 하기위한 코드이다
import cv2
import matplotlib.pyplot as plt

img_basic = cv2.imread('임정석.jpg', cv2.IMREAD_COLOR)
plt.imshow(cv2.cvtColor(img_basic, cv2.COLOR_BGR2RGB)) #opencv는 BGR순서이지만 matplotlib는 RGB이기 때문에 칼라를 저렇게 바꿔준다.
plt.show()

img_basic = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY) # cv2.cvtColor 에 대한 설명은 바로아래 설명
plt.imshow(cv2.cvtColor(img_basic, cv2.COLOR_GRAY2RGB))
plt.show()

                          ##   기억할것!!   ##
(1) 
opencv(BGR)와 matplotlib(RGB)의 색 구조 가 다르기때문에 꼭 코드를 입력해야 한다.

(2) 
import cv2
import matplotlib.pyplot as plt
그림BGR = cv2.imread("그림파일.jpg")
그림RGB = cv2.cvtColor(그림BGR, cv2.COLOR_BGR2RGB)

(3) 
cv2.cvtColor(원본 이미지, 색상 변환 코드)를 이용하여 이미지의 색상 공간을 변경할 수 있습니다.
색상 변환 코드는 원본 이미지 색상 공간2결과 이미지 색상 공간을 의미합니다.
원본 이미지 색상 공간은 원본 이미지와 일치해야합니다.
Tip : BGR은 RGB 색상 채널을 의미합니다. 



# OpenCV 이미지 연산

# 이미지 크기 및 픽셀 확인(코랩)
import cv2
image = cv2.imread('임정석,jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape) # >>> (787, 591, 3)
print(image.size) # >>> 1395351

# 이미지 Numpy 객체의 특정 픽셀을 가리킵니다.
px = image[100, 100]

# B, G, R 순서로 출력됩니다.
# (단, Gray Scale인 경우에는 B, G, R,로 구분되지 않습니다.)
print(px) # >>> [255 255 255]

# R 값만 출력하기
print(px[2]) # >>> 255



# OpenCV를 활용한 특정 범위 픽셀 변경
import cv2
import matplotlib.pyplot as plt 
import time

image = cv2.imread('임정석.jpg')

# (1) 첫번째 방법
start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [50, 50, 50]
print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#  (2) 두번째 방법
start_time = time.time()
image[0:100, 0:100] =  [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#당연히 시간은 두번째 것이 더 빠르다



# openCV를활용한 ROI(Region of Interest:관심 있는 영역) 추출
# 컴퓨터 비전에서 관심이란 유의미한 feature가 들어있는 공간을 의미
import cv2
import matplotlib.pyplot as plt 

image = cv2.imread('임정석.jpg')

# Numpy Slicing: R이 처리 가능
roi = image[200:350, 50:200]

# ROI 단위로 이미지 복사하기
image[0:150, 0:150] = roi

plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()



# openCV를 활용한 픽셀별 색상 다루기
import cv2
import matplotlib.pyplot as plt 

image = cv2.imread('임정석.jpg')
image[:, :, 2] = 0  # R 값을 0으로

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()


# openCV를 활용한 이미지 변형

# 이미지 크기 조절
cv2.resize(image, dsize, fx, fy, interpolation)  :  이미지 크기를 조절합니다.
 - dsize : Manual size (결과 이미지 크기)(튜플 형식으로)
 - fx : 가로 비율
 - fy : 세로 비율
 - interpolation : 보간법
 INTER_CUBIC : 사이즈를 크게 할 때 주로 사용합니다.
 INTER_AREA : 사이즈를 작게 할 때 주로 사용합니다.

 보간법은 사이즈가 변할 때 픽셀 사이의 값을 조절하는 방법을 의미합니다.


import cv2
import matplotlib.pyplot as plt

image = cv2.imread('임정석.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

expand = cv2.resize(image, None, fx = 2.0, fy = 2.0,  interpolation=cv2.INTER_CUBIC)
plt.imshow(cv2.cvtColor(expand, cv2.COLOR_BGR2RGB))
plt.show()

shrink = cv2.resize(image, None, fx = 0.8, fy = 0.8, ineterpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB))
plt.show()


# 이미지 위치 변경
cv2.warpAffine(image, M, dsize)  :  이미지의 위치를 변환시킴
 - M : 변환 행렬
 - dsize : Manual size (결과 이미지 크기)

# 변환 행렬과 반환

[M11  M12  M13]
[M21  M22  M23]           (a, b)

(M11*a + M12*b +M13, M21 *a + M22 * b + M23)

단순히 이미지의 위치를 변경할 때 변환 행렬은
[1  0  tx]
[0  1  ty]                 (a, b)
 
 (a + tx, b + ty) 즉 기존 a,b 의 좌표에서 가로로 tx만큼 세로로 ty만큼 이동한 것과 같다


import cv2
import numpy as np
import matplotlib.pyplot as plt 

image = cv2.imread('임정석.jpg')

 # 행과 열 정보만 저장합니다.
height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()


# 이미지 회전
cv2.getRotationMatrix2D(center, angle, scale)  :  이미지 회전을 위한 변환 행렬을 생성하는 함수.
 - center : 회전중심
 - angle : 회전각도
 - scale : Scale Factor (크기)

import cv2
import numpy as np
import matplotlib.pyplot as plt 

image = cv2.imread('임정석.jpg')

# 행과 열 정보만 저장합니다.
height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5) # 회전의 중심값을 너비와 높이의 중간으로 설정, scale값을 반으로 = 크기 반
dst = cv2.warpAffine(image, M, (width, height))

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()
 

# 이미지 합치기

1. cv2.add():   Saturation 연산을 수행한다.
   0보다 작으면 0, 255보다 크면 255로 표현

2. np.add():    Modulo 연산을 수행한다.
   256은 0, 257은 1로 표현

주로 1 번을 많이 한다. 2번은 특정한 픽셀에 255가 넘어가서 0으로 시작되기땜에


# OpenCV 임계점 처리하기

# 이미지의 기본 이진화(흑과 백 으로 나누겠다)
cv2.threshold(image, thresh, max_value, type) : 임계값을 기준으로 흑/백으로 분류하는 함수
  - image : 처리할 Gray Scale 이미지
  - thresh : 임계 값 (전체 픽셀에 적용)
  - max_value : 임계 값을 넘었을 때 적용할 값
  - type : 임계점을 처리하는 방식

1) THRESH_BINARY : 임계 값보다 크면 max_value, 작으면 0
2) THRESH_BINARY_INV : 임계 값보다 작으면 max_value, 크면 0
3) THRESH_TRUNC : 임계 값보다 크면 임계 값, 작으면 그대로
4) THRESH_TOZERO : 임계 값보다 크면 그대로, 작으면 0
5) THRESH_TOZERO_INV : 임계 값보다 크면0, 작으면 그대로 
 
*thresh 값을 초과하면 max_value값으로 넣어주겠다


예제 적용 해 보기
from google.colab import files
uploaded = files.upload()
-------------------------------
import cv2
import matplotlib.pyplot as plt 

image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

images =[]
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # 반환값 두개를 ret과 thresh1이라는 변수에 받겠다.
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
images.append(thresh1)
images.append(thresh2)
images.append(thresh3)
images.append(thresh4)
images.append(thresh5)

for i in images:
   plt.imshow(cv2.cvtColor(i, cv2.COLOR_GRAY2RGB))
   Plt.show()

# 이미지의 적응 임계점 처리
   - 하나의 이미지에 다수의 조명 상태가 존재하는 경우 적용하면 좋습니다.(즉 여러임계점 적용)
임
cv2.adaptiveThreshold(image, max_value, adaptive_method, type, block_size, C) : 적응 계점 처리 함수
  - max_value : 임계 값을 넘었을 때 적용할 값
  - adaptive_method : 임계 값을 결정하는 계산 방법
  ADAPTIVE_THRESH_MEAN_C : 주변영역의 평균값으로 결정
  ADAPTIVE_THRESH_GAUSSIAN_C
  - type : 임계 값을 처리하는 방식
  - block_size : 임계 값을 적용할 영역의 크기
  - C : 평균이나 가중 평균에서 차감할 값
Adaptive Threshold를 이용하면,전체 픽셀을 기준으로 임계 값을 적용하지 않습니다. 즉 특정영역마다 다른 픽셀값을 사용하게 할 수 있다.


예제)
import cv2

image = cv2.imread('hand_writing_image.jpg',cv2.IMREAD_GRAYSCALE)

ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres1, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2, cv2.COLOR_GRAY2RGB))
plt.show()


# opencv Tracker
Tracker 사용방법 (트렉커바란 사용자가 바를 이리저리 움직여 보면서 값 을 편하게 바꿔볼 수 있는 기능)
cv2.createTrackbar(track_bar_name, window_name, value, count, on_change) : Tracker를 생성하는 함수
   - value : 초기 값
   - count : Max 값(Min:0)
   - on_change: 값이 변경될 때 호출되는 Callback 함수

예제)

import cv2
import numpy as np

def change_color(x):
   r = cv2.getTrackbarPos("R", "Image")
   g = cv2.getTrackbarPos("G", "Image")
   b = cv2.getTrackbarPos("B", "Image")
   image[:] = [b, g, r]
   cv2.imshow('Image', image)

image = np.zeros((600, 400, 3), np.unit8)
cv2.namedWindow("Image")

cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)


# opencv 도형 그리기

직선 그리기

cv2.line(image, start, end, color, thickness) : 하나의 직선을 그리는 함수
   -start : 시작 좌표(2차원)
   -end : 종료 좌표(2차원)
   -thickness : 선의 두께


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8) # np.full((x,y),z) -> z를 x,y만큼 채움
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 3)

plt.imshow(image)
plt.show()


하나의 사각형을 그리기

cv2.rectangle(image, start, end, color, thickness) : 하나의 사격형을 그리는 함수
   - start: 시작 좌표(2차원)
   - end: 종료 좌표(2차원)
   - thickness: 선의 두께(채우기:-1) (선의두께에 -1 을 설정하면 내부를 채우게 가능)


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 10)

plt.imshow(image)
plt.show()

원 그리기
cv2.circle(image, center, radian, color, thickness) : 하나의 원을 그리는 함수
   - center : 원의 중심 (2차원)
   - radian : 반지름
   - thickness : 선의 두께 (채우기: -1)

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.circle(image, (255, 255), 30, (255, 0, 0), 3)

plt.imshow(image)
plt.show()

다각형 그리기
cv2.polylines(image, points, is_closed, color, thickness) : 하나의 다각형을 그리는 함수
   - points : 꼭지점들
   - is_closed : 닫힌 도형 여부
   - thickness : 선의 두께(채우기: -1)

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 0, 255), 4)

plt.imshow()
plt.show()

텍스트 그리기
cv2.putText(Image, text, position, font_type, font_scale,color) : 하나의 텍스트를 그리는 함수
   - position : 텍스트가 출력될 위치
   - font_type : 글씨체
   - font_scale : 글씨 크기 가중치

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
image =cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))

plt.imshow(image)
plt.show()


# Contours찾기(그림안에서 어떤 사물의 외각(테두리)을 찾는것)
cv2.findContours(image, mode, method) : 이미지 에서 Contour들을 찾는 함수
- mode: Contour들을 찾는 방법
RETR_EXTERNAL : 바깥쪽 Line만 찾기
RETR_LIST : 모든Line을 찾지만, Hierarchy 구성 x
RETR_TREE : 모든Line을 찾으며, 모든 Hierarchy 구성 ㅇ

- method : Contour들을 찾는 근사치 방법
CHAIN_APPROX_NONE : 모든 Contour포인트 저장
CHAIN_APPROX_SIMPLE: Contour Line을 그릴 수 있는 포인트만 저장

입력 이미지는 Grayscale Threshold 전처리 과정이 필요합니다.


Contours 그리기
cv2.drawContours(image, contours, contour_index, color, thickness) : Contour들을 그리는 함수
- contour_index: 그리고자 하는 Contours Line( 전체: -1)

예제)

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('gray_image.jpg')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
image = cv2.drawContours(image, contours, -1, (0, 255, 0),4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# openCV Contours처리
Contor의 사각형 외각 찾기
cv2.boundingRect(contour)  :  Contour를 포함하는 사각형을 그립니다.
사각형의 X, Y 좌표와 너비, 높이를 반환합니다.

예제)
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('digit_image.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
# 하얀색과 검정석 반전을 시키는 코드 bitwise_not(),findCotours값은
# threshold값을 넣었을때 하얀색값을 추출하기때문
plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()