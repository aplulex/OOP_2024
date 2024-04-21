import math
n=3
import turtle
turtle.shape('turtle')
a=30
for i in range(10): 
    turtle.penup()
    turtle.home()  
    turtle.forward(abs(a/(2*(math.sin(math.pi/n)))))
    turtle.pendown()
    turtle.left(180-90*(n-2)/n)
    for j in range(n):
         turtle.forward(a)
         turtle.left(180-180*(n-2)/n)
    n+=1
    a+=20     
   
