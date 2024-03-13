import pygame
from pygame.draw import *
pygame.init()
FPS=30
screen=pygame.display.set_mode((400,400))
y=80
z=110
screen.fill((250,250,250))
def crug():
    pygame.draw.circle(screen,(225,225,0),(200,200),200)
    pygame.draw.circle(screen,(225,0,0),(295,150),25)
    pygame.draw.circle(screen,(225,0,0),(115,150),35)
    pygame.draw.circle(screen,(0,0,0),(295,150),10)
    pygame.draw.circle(screen,(0,0,0),(115,150),15)
def brov(y,z):
    for i in range(25):
        pygame.draw.aaline(screen,(0,0,0),(270,y+30),(400,y))
        y+=0.75
    for i in range(25):
        pygame.draw.aaline(screen,(0,0,0),(0,z-80),(150,z))
        z+=0.75
def rot(m):
    for i in range(100):
        pygame.draw.aaline(screen, (0, 0, 0), (50, m ), (350, m))
        m += 0.2
crug()
brov(y,z)
rot(290)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
