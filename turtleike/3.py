import turtle
import math

x=-400
y=0.00000001
V=int(input('put velocity:'))
a=float(input('put angle in radians:'))
Vx=V*math.cos(a)
Vy=V*math.sin(a)
ay=-10
dt=0.1
turtle.shape('turtle')
turtle.speed(1)
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
for i in range (1000):
    if y<=0:
        Vy=-0.9*Vy
        Vx=0.9*Vx
    x += Vx*dt
    y += Vy*dt + ay*dt*dt/2
    Vy += ay*dt
    turtle.goto(x,y)
    if Vy==0:
        break

input()
