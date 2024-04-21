import turtle
x=0
t=0.001
y=0
v=40
for i in range(300):
    if y>=0:
        x+=5*t
        y+=v*t-5*t**2
        v-=10*t
        turtle.goto(x,y)
        t+=0.001
    elif y < 0:
        v=abs(v)-4.3
        y=0
        continue
