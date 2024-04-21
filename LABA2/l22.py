import turtle
import  math
index = [(90,20,270,20,270,40,270,20,270,20),(45,math.sqrt(800),-135,40,180,20),(0,20,-90,20,-45,math.sqrt(800),135,20),(90,20,-180,20,90,20,90,20,-180,40,180,20),(45,math.sqrt(800),135,20,-180,20,-135,math.sqrt(800),135,20,-135,math.sqrt(800)),(90,20,-90,20,180,20,90,20,90,20,-90,20,-90,20),(0,20,-90,20,-90,20,-90,20,-45,math.sqrt(800)),(45,math.sqrt(800),135,20,180,20,-135,math.sqrt(800),45,20),(0,20,90,20,90,20,90,40,90,20,90,20),(0,20,90,20,90,20,90,20,90,20,-135,math.sqrt(800))]
a=0
q=-1
m=[1,2,7,5,6,0]
for j in m:
    q+=1
    if j==2:
        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(-90)
        turtle.pendown()
    for i in range(int(len(index[j])/2)):
        turtle.left(index[j][a])
        turtle.forward(index[j][a+1])
        a+=2
    turtle.left(270)
    turtle.penup()
    turtle.home()
    turtle.forward(40*(int(q)+1))   
    turtle.pendown()
    a=0

