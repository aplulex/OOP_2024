
n=int(input())
import turtle
turtle.shape('turtle')
for i in range(n):
 turtle.left(360/n*int(i))
 turtle.forward(100)
 turtle.stamp()
 turtle.home()
