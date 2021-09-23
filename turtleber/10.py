import turtle

turtle.shape('turtle')
turtle.speed(0)
for i in range(0,360,60):
    turtle.left(60)
    for j in range(0,361):
        turtle.forward(1)
        turtle.left(1)

input()
