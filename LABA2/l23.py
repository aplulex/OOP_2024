import turtle
q=-1
j=0
my_file=open('plumbum.txt','w')
print(90,20,270,20,270,40,270,20,270,20,'\n',45,26,-135,40,180,20,'\n',0,20,-90,20,-45,26,135,20,'\n',90,20,-180,20,90,20,90,20,-180,40,180,20,'\n',45,26,135,20,-180,20,-135,26,135,20,-135,26,'\n',90,20,-90,20,180,20,90,20,90,20,-90,20,-90,20,'\n',0,20,-90,20,-90,20,-90,20,-45,26,'\n',45,26,135,20,180,20,-135,26,45,20,'\n',0,20,90,20,90,20,90,40,90,20,90,20,'\n',0,20,90,20,90,20,90,20,90,20,-135,26,'\n',file=my_file)
my_file.close()
with open("plumbum.txt","r") as cal:
    x=cal.readline()
    t=list(map(int,x.split()))
    while x !="":
        if j==2:
                turtle.penup()
                turtle.left(90)
                turtle.forward(20)
                turtle.left(-90)
                turtle.pendown()
        for i in range(1,len(t)+1):
           
            if i%2==0:
                turtle.forward(t[i-1])
            else:
                 turtle.left(t[i-1])
        q+=1
        j+=1
        x = cal.readline()
        t = list(map(int, x.split()))
        turtle.left(270)
        turtle.penup()
        turtle.home()
        turtle.forward(40*(int(q)+1))   
        turtle.pendown()
