from ast import While
from cgitb import text
from email.headerregistry import Address
from pickle import TRUE
from telnetlib import SB
from tkinter import font
from turtle import right, title
import pygame
import time
import random
#1. 게임 초기화
pygame.init()

#2. 게임창 옵션 설정
size = [400, 800]
screen = pygame.display.set_mode(size)

title = "갤러그"
pygame.display.set_caption(title)

#3. 게임 내 필요한 설정
clock = pygame.time.Clock()

# 이미지 출력 클래스
class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()

        else:                        
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img,(self.x,self.y))   

def crash(a,b):
    if (a.x - b.sx <= b.x) and (b.x <= a.x + a.sx) :
        if (a.y - b.sy <= b.y) and (b.y <= a.y + a.sy):
           return True
        else :
            return False
    else :
        return False

# 우줜 이미지
ss = obj()
ss.put_img("C:/Users/dugkf/OneDrive/바탕 화면/갤러그/ss.png")
ss.change_size(20,20)
ss.x = round(size[0]/2- ss.sx/2)
ss.y = size[1] -ss.sy -50
ss.move = 10
class back:
    def __init__(self):
        self.y = 0
        self.x = 0
    def put_img (self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:                        
            self.img = pygame.image.load(address)
            self.bgx, self.bgy = self.img.get_size()
    def show(self):
        screen.blit(self.img,(self.x,self.y))
# 배경 이미지
bg = back()
bg.put_img("c:/Users/dugkf/OneDrive/바탕 화면/갤러그/space.png")
bg.x = (0,0)
bg.y = (0,0)


left_go = False
right_go = False
space_go = False





m_list = []
b_list = []
t_list = []

black = (0,0,0)
white = (255,255,255)
k=0


GO = 0
score = 0

#4. 메인 이벤트
SB = 0 
while SB == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SB = 1
    screen.fill(black)
    font =pygame.font.Font("C:\Windows\Fonts\coure.fon", 200)
    text = font.render("PRESS SPACE KEY TO START THE GAME",True , (255,255,255))
    screen.blit(text,(70,round(size[1]/2 - 50 )))
    pygame.display.flip()

SB = 0
while SB == 0:
    #4-1. fps 설정
    clock.tick(15)
    #4-2. 각종 입력 감지
    
    # 키보드 입출력

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False
    #4-3. 입력, 시간에 따른 변화
    if left_go == True:
        ss.x -= ss.move
        if ss.x <=0 :
            ss.x = 0

    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx
    
    # 미사일 생성
    if space_go == True and k % 4 == 0:
        mm = obj()
        mm.put_img("C:/Users/dugkf/OneDrive/바탕 화면/갤러그/boom.png")
        mm.x = round(ss.x + ss.sx/2 - mm.sx/2) 
        mm.y = ss.y - mm. sy - 10
        mm.move = 30
        m_list.append(mm)
    
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    d_list.reverse()
    for d in d_list:
        del m_list[d]
    
    if random.random() > 0.95:
        bb = obj()
        bb.put_img("C:/Users/dugkf/OneDrive/바탕 화면/갤러그/bug.png")
        bb.change_size(20,20)
        bb.x = random.randrange(0,size[0]-bb.sx-round(ss.sx/2)) 
        bb.y = 10
        bb.move = 9
        b_list.append(bb)
    p_list = []
    for i in range(len(b_list)):
        b = b_list[i]
        b.y += b.move
        if b.y >= size[1]:
            p_list.append(i)
    p_list.reverse()
    for p in p_list:
        del b_list[p]
        SB = 1
        GO = 1

    pm_list = []
    pb_list = []
    for i in range(len(m_list)):
        for j in range(len(b_list)):
            m = m_list[i]
            b = b_list[j]
            if crash(m,b) == True:
                pm_list.append(i)
                pb_list.append(j)
    pm_list = list(set(pm_list))
    pb_list = list(set(pb_list))
    pm_list.reverse()
    pb_list.reverse()
    try:
        for pm in pm_list:
            del m_list[pm]
    
        for pb in pb_list:
            del b_list[pb]
            score += 100
    except:
       
        pass
    for i in range(len(b_list)):
        b = b_list[i]
        if crash(b,ss) == True:
            SB = 1
            GO = 1
    # 적 개체 2

    if random.random() > 0.9:
        bt = obj()
        bt.put_img("C:/Users/dugkf/OneDrive/바탕 화면/갤러그/bug2.png")
        bt.change_size(20,20)
        bt.x = random.randrange(0,size[0]-bt.sx-round(ss.sx/2)) 
        bt.y = 10
        bt.move = 4 
        t_list.append(bt)
    k += 1
    o_list = []

    for i in range(len(t_list)):
        t = t_list[i]
        t.y += t.move
        if t.y >= size[1]:
            o_list.append(i)
    o_list.reverse()
    for o in o_list:
        del t_list[o]
        SB = 1
        GO = 1

    om_list = []
    ot_list = []
    for i in range(len(m_list)):
        for j in range(len(t_list)):
            m = m_list[i]
            t = t_list[j]
            if crash(m,t) == True:
                om_list.append(i) 
                ot_list.append(j)
    om_list = list(set(om_list))
    ot_list = list(set(ot_list))
    om_list.reverse()
    ot_list.reverse()

    try:
        for om in om_list:
            del m_list[om]
    
        for ot in ot_list:
            del t_list[ot]
            score += 50

    except:
        pass

    for i in range(len(t_list)):
        t = t_list[i]
        if crash(t,ss) == True:
            SB = 1
            GO = 1
        
    #4-4. 그리기
    
    
    screen.fill(black)
    bg.show()
    ss.show()
    for m in m_list:
        m.show()
    for b in b_list:
        b.show()
    for t in t_list:
        t.show()
    font =pygame.font.Font("C:\Windows\Fonts\h8514fix.fon", 20)
    text = font.render("score : {}".format(score),True , (255,255,0))
    screen.blit(text,(10,5))
    #4-5. 업데이트
    pygame.display.flip()
#5. 게임 종료
while GO == 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = 0
    
    font = pygame.font.Font("C:/Windows/Fonts/h8514fix.fon", 40)
    text = font.render("GAME OVER", True, (255,0,0))
    screen.blit(text, (80, round(size[1]/2-50)))
    
    pygame.display.flip()


pygame.quit()