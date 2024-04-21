from random import randint
import turtle
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
number_of_turtles = 30
steps_of_time_number = 1000
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(0,360))
for i in range(steps_of_time_number):
        for unit in pool:
            unit.forward(2)
            if unit.xcor()>300 or unit.xcor()<-300:
                unit.left(180)
            elif unit.ycor()>300 or unit.ycor()<-300:
                unit.left(180)
