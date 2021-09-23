import turtle

turtle.speed(0)
turtle.penup()
turtle.goto(0, -400)
turtle.pendown()
turtle.shape('turtle')
while True:
    for j in range(180):
        turtle.forward(1.5)
        turtle.left(1)
    for j in range(180):
        turtle.forward(0.25)
        turtle.left(1)
