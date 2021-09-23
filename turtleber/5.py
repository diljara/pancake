import turtle

turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.penup()
turtle.forward(10)
turtle.left(90)

for i in range (70, 250, 20):
    turtle.backward(10)
    turtle.pendown()
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)

input()
