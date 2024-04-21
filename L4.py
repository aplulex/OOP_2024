import pygame
from pygame.draw import *
from random import randint
pygame.init()
i=0
FPS = 60
rect1=pygame.Rect((0,0,400,400))
screen = pygame.display.set_mode((400, 400))
class Ball: #Создаем класс шаров , который будет хранить их коориднаты, цвет ,радиус
    def __init__(self):
        self.r = randint(10, 50)
        self.color = (randint(0, 255),randint(0, 255), randint(0, 255))
        self.x = randint(0, 400)
        self.y = randint(0,400)
pygame.display.update()
clock = pygame.time.Clock()
b = [Ball() for _ in range(randint(2, 10))] #Создаем список хранящий ,который будет хранить информацию о каком-то количестве шаров
finished = False
while not finished:
    clock.tick(FPS)
    for ball in b:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.r) #Отрисовка шаров
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey =  pygame.mouse.get_pos() #Считываем координты шелчка мыши
            for ball in b:
                if ((ball.x - ball.r) <= mousex) and ((ball.x + ball.r) >= mousex) and ((ball.y- ball.r) <= mousey) and ((ball.y+ ball.r) >= mousey):
                    i+=1
                    print(i)
                    b.remove(ball)#Удаляем шар удовлетворяющий условию из списка
    if len(b) == 0:#Проверку на пустоту списка , если он пуст ,заполняем его опять
        b = [Ball() for _ in range(randint(2, 10))]
    pygame.display.update()
    for ball in b :#Цикл отвечает за движение шариков (в том числе отражение от границы))
        dx=randint(-10,10)
        dy=randint(-10,10)
        if ball.x+ball.r+dx>=400 or ball.x-ball.r+dx<=0:
           ball.x-=dx
        else :
           ball.x+=dx
        if ball.y + ball.r + dy >= 400 or ball.y - ball.r + dy <= 0:
           ball.y -= dy
        else:
           ball.y += dy
    screen.fill((0,0,0))
pygame.quit()
