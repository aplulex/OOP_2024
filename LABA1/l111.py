import turtle

a=10

from krug import w
turtle.left(7.5)
turtle.left(90)
for j in range(5):
    for i in range(2):
        turtle.left(180)
        w(a)
    a+=5
