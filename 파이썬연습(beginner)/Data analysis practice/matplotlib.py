# # 단순한 그래프 그리기 (그래프를 그리려면 matplotlib의 pyplot 모듈을 이용합니다.)(sin함수 그려보기)
# import numpy as np
# import matplotlib.pyplot as plt

#  # 데이터 준비
# x = np.arange(0, 6, 0.1) 
# y = np.sin(x)  # np.sin() sin함수-> 넘파이 x의 각 원소에 넘파이의 sin 함수

#  # 그래프 그리기
# plt.plot(x, y) # plot(X, Y)는 X의 대응값에 대한 Y 데이터의 2차원 선 플롯을 생성합니다.
# plt.show()





# # cos 함수도 추가로 그려보기, 제목과 각 축의 이름(레이블) 표시 등, pyplot의 다른기능 추가

# import numpy as np
# import matplotlib.pyplot as plt

#  # 데이터 준비
# x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1간격으로 생성
# y1 = np.sin(x)
# y2 = np.cos(x)

#  # 그래프 그리기
# plt.plot(x, y1, label ="sin")
# plt.plot(x, y2, linestyle = "--", label ="cos") # cos함수는 점선으로 그리기
# plt.xlabel("x") # x축 이름
# plt.ylabel("y") # y축 이름
# plt.title('sin & cos') # 제목
# plt.legend() # 범례 입력
# plt.show()




# 이미지 표시하기 (pyplot 에는 이미지를 표시해주는 메서드인 imshow() 도 
# 준비되어 있다, 이미지를 읽어 들일 때는 matplotlib.image 모듈의 imread() 
# 메서드를 이용합니다. 예를 보시죠)

import matplotlib.pyplot as plt 
from matplotlib.image import imread

img = imread(C:\\Users\\ljs74\\OneDrive\\바탕 화면\\임정석\\사진자료\\임정석02(1))

plt.imshow(img)
plt.show()