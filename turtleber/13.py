import turtle

turtle.speed(0)
turtle.shape('turtle')
turtle.color('yellow')
turtle.begin_fill()
for i in range (180):
    turtle.forward(2)
    turtle.left(2)
turtle.end_fill()

turtle.color('blue')
turtle.width(5)
turtle.penup()
turtle.goto(0,40)
turtle.left(90)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,80)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
for i in range (36):
    turtle.forward(2)
    turtle.left(10)
turtle.end_fill()

turtle.penup()
turtle.goto(0,80)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
for i in range (36):
    turtle.forward(2)
    turtle.right(10)
turtle.end_fill()

turtle.penup()
turtle.goto(5,15)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
for i in range (18):
    turtle.forward(2)
    turtle.left(20)
turtle.end_fill()
turtle.hideturtle()

input()
