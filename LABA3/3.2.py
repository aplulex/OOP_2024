import pygame
from pygame.draw import *
pygame.init()
FPS=30
screen=pygame.display.set_mode((500,600))
screen.fill((0,0,0))
pygame.draw.rect(screen, (125,125,125), (0,0,500,250))
def dom():
    def pram(x,y,z,q,w,e,r):
        pygame.draw.rect(screen, (x,y,z), (q,w,e,r))
    def trap():
        pygame.draw.polygon(screen,(60,60,60),((20,100),(350,100),(320,70),(50,70)))
    pram(121,85,61,40,100,290,350)
    for i in range (4):
        pram(125,125,125,60+65*(i),120,30,150)
    pram(50,50,50,5,280,360,40)
    for i in range (6):
        pram(50,50,50,10+65*(i),220,20,80)
    pram(50,50,50,5,220,360,10)
    for i in range (2):
        pram(150, 75, 0, 65+90*(i), 350, 60, 60)
    pram(255, 255, 0, 65+90*2, 350, 60, 60)
    trap()
    pram(50,50,50,75,50,15,40)
    pram(50, 50, 50, 115, 35, 30, 40)
    pram(50, 50, 50, 230, 40, 20, 40)
    pram(50, 50, 50, 300, 45, 20, 40)
def el(a, b, c, d, s, w, q):
    pygame.draw.ellipse(screen, (a, b, c), (d, s, w, q))
el(225,255,255,400,10,100,100)
el(70, 70, 70, 200, 30, 350, 50)
el(70, 70, 90, 25, 10, 350, 50)
dom()
el(90, 90, 90, 100, 70, 350, 50)
el(70, 70, 90, 200, 50, 150, 20)
def prid():
    pygame.draw.circle(screen, (225, 225, 225), (400, 450), 40)
    pygame.draw.polygon(screen,(225,225,225),((360,450),(340,490),(320,530),(340,550),(360,545),(380,550),(400,540),(410,550),(420,540),(440,530),(450,540),(480,515),(460,495),(450,480),(440,450)))
    pygame.draw.circle(screen,(225, 0, 225), (375, 450), 10)
    pygame.draw.circle(screen, (0, 0, 0), (375, 450), 5)
    pygame.draw.circle(screen, (125, 125, 0), (415, 450), 10)
    pygame.draw.circle(screen, (0, 0, 0), (415, 450), 5)

prid()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
