import pygame
from pygame.draw import *
pygame.init()
FPS=30
screen=pygame.display.set_mode((500,600))
screen.fill((0,0,0))
pygame.draw.rect(screen, (125,125,125), (0,0,500,250))
def dom(a,b):
    def pram(x,y,z,q,w,e,r,a,b):
        pygame.draw.rect(screen, (x,y,z), (2*q+b,2*w+a,2*e,2*r))
    def trap(a,b):
        pygame.draw.polygon(screen,(60,60,60),((8+b,40+a),(140+b,40+a),(128+b,28+a),(20+b,28+a)))
    pram(121,85,61,8,20,58,70,a,b)
    for i in range (4):
        pram(125,125,125,12+13*(i),24,6,30,a,b)
    pram(50,50,50,1,56,72,8,a,b)
    for i in range (6):
        pram(50,50,50,2+13*(i),44,4,16,a,b)
    pram(50,50,50,1,44,72,2,a,b)
    for i in range (2):
        pram(150, 75, 0, 13+18*(i), 70, 12, 12,a,b)
    pram(255, 255, 0, 13+18*2, 70, 12, 12,a,b)
    trap(a,b)
    pram(50,50,50,15,10,3,8,a,b)
    pram(50, 50, 50, 23, 7, 6, 8,a,b)
    pram(50, 50, 50, 46, 8, 4, 8,a,b)
    pram(50, 50, 50, 60, 9, 4, 8,a,b)
def el(a, b, c, d, s, w, q):
    pygame.draw.ellipse(screen, (a, b, c), (d, s, w, q))
el(225,255,255,400,10,100,100)
el(70, 70, 70, 16,280 , 200, 20)
el(70, 70, 70, 200, 30, 350, 50)
dom(200,0)
el(70, 70, 70, 16,240 , 500, 40)
el(70, 70, 70, 100,300 , 500, 40)
dom(150,350)
el(90, 90, 90, 100, 70, 350, 50)
el(105, 105, 105, 250, 100, 200, 50)
dom(100,140)
def prid(a,b):
    pygame.draw.circle(screen, (225, 225, 225), (400-a, 450-b), 16)
    pygame.draw.polygon(screen, (225, 225, 225),((384-a,450-b),(386-a,470-b),(380-a,490-b),(372-a,500-b),(381-a,501-b),(385-a,504-b),(387-a,500-b),(389-a,507-b),(396-a,500-b),(400-a,500-b),(403-a,502-b),(416-a,490-b),(436-a,495-b),(426-a,480-b),(416-a,450-b)))
    pygame.draw.circle(screen,(225, 0, 225), (408-a, 450-b), 4)
    pygame.draw.circle(screen, (0, 0, 0), (410-a, 450-b), 2)
    pygame.draw.circle(screen, (125, 125, 0), (392-a, 450-b), 4)
    pygame.draw.circle(screen, (0, 0, 0), (394-a, 450-b), 2)

prid(0,0)
prid(100,100)
prid(100,200)
prid(200,140)
prid(300,10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
