import turtle

def star(n):
    a=180//n
    for i in range(n):
        turtle.forward(100)
        turtle.left(180-a)

turtle.shape('turtle')
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
star(5)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
star(11)
input()
