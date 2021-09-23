import turtle
import math

turtle.shape('turtle')
a=30
r=[0, 0, 0]
fi=math.pi/3
for i in range (3,14):
    turtle.penup()
    turtle.left(360-turtle.heading())
    fi=math.pi/i
    r.append(a/2/math.sin(fi))
    turtle.forward(r[i]-r[i-1])
    turtle.left(90+180/i)
    turtle.pendown()
    for j in range (i):
        turtle.forward(a)
        turtle.left(180-(i-2)*180/i)
    a=a+20

input()
