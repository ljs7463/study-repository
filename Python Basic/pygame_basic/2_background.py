import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임이름

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\ljs74\\OneDrive\\바탕 화면\\임정석\\PythonWorkspace\\pygame_basic\\background.png")

#이벤트 루프(위에 코드까지 작성후 실행하면 아무것도 없기땜에 실행하고 바로 꺼져서)
running = True #게임이 진행중인가?(True면 계속 돌고있다는것)
while running: #게임이 진행되는동안
    for event in pygame.event.get():  #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
  
    #screen.fill((0, 0, 255)) #배경이미지 안불러오고 R,G,B 값으로 불러오는것
    screen.blit(background, (0, 0))  #배경그리기[맨왼쪽 맨위(0, 0)]

    pygame.display.update() #게임화면을 다시 그리기!![업데이트 해줌으로서 while문을 돌면서 계속 그려주는거(필수)]
#pygame 종료
pygame.quit()