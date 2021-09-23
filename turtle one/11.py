import turtle

turtle.shape('turtle')
for i in range(1,6):
    for j in range(360//i):
        turtle.forward(i*i)
        turtle.left(i)
    for j in range(360//i):
        turtle.forward(i*i)
        turtle.right(i)

input()
