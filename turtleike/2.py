from random import *
import turtle

def away(n):
    if len(n)<2:
        return n
    a=[]
    b=[]
    n=n.replace('(','')
    n=n.replace(')','')
    a=n.split(', ')
    for i in range (len(a)//2):
        b.append([int(a[2*i]), int(a[2*i+1])])
    return b

nums_dict = {}
key=[]
s=[]
with open ('1.txt') as file:
    for counter, line in enumerate(file, start=1):
        if counter % 2 == 1:
            key.append(line.rstrip())
        else:
            s.append(away(line))
for i in range (len(key)):
    nums_dict[key[i]]=s[i]

a=input()
turtle.left(270)
for x, ind_num in enumerate(a):
    turtle.penup()
    if ind_num == '1':
        turtle.goto( -600 + (x + 1) * 150, -100 )
    elif ind_num=='6':
        turtle.goto( -600 + (x + 1) * 150+100, 0)
    else:
        turtle.goto( -600 + (x + 1) * 150, 0 )
    turtle.pendown()
    for el in nums_dict[ind_num]:
        turtle.left(el[0])
        turtle.forward(el[1])
input()
