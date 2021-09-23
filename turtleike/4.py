from random import randint
import turtle

#def close(x1,x2,y1,y2):
    #if (x2-x1)**2+(y2-y1)**2<=5:
        #return True
    #return False

number=5
steps=300
V=4
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
for i in range(4):
    turtle.forward(600)
    turtle.left(90)
turtle.hideturtle()

pool=[turtle.Turtle(shape='circle') for i in range(number)]
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.shapesize(0.5, 0.5, 0.1)
    unit.left(randint(0,360))
    unit.goto(randint(-295,295), randint(-295, 295))

for i in range (steps):
    for unit in pool:
        unit.forward(V)
        a=unit.heading()
        #for particle in pool:
            #if abs(unit.xcor()-particle.xcor())+abs(unit.ycor()-particle.ycor())<=10:
                #unit.left(180)
                #particle.left(180)
        if abs(unit.xcor())>=295:
            unit.left(180-2*a)
        if abs(unit.ycor())>=295:
            unit.right(2*a)
input()

