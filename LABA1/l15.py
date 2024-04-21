import turtle
turtle.shape('turtle')
a=100
for i in range(10):
  turtle.forward(a)
  turtle.left(90) 
  turtle.forward(a)
  turtle.left(90)
  turtle.forward(a)
  turtle.left(90) 
  turtle.forward(a)
  turtle.left(90)
  turtle.penup()
  turtle.forward(5)
  turtle.left(90)
  turtle.forward(5)
  turtle.right(90)
  turtle.pendown()
  a-=10
