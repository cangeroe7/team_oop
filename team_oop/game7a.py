import random
import math

# Angry Bir- I mean Turtle Archery
# Fire a bow from the left side of the screen at some angle
# Try to hit a target on the right side of the screen
# Factor in wind and gravity and try to hit the center of the target


from turtle import *


# Create the Window
setup(width=1200, height=600, startx=None, starty=None)
bowx = -400
bowy = 0
bow = (bowx, bowy)
g = .0025
targdist = 450
hud = Turtle()
arr1 = Turtle()
arr2 = Turtle()
arr3 = Turtle()
arr1.penup()
arr2.penup()
arr3.penup()

# Main Menu UI
delay(0)
ht()
hud.speed(0)
hud.penup()
hud.setpos(0,250)
hud.write("Turtle Archery", False, align="center", font=('Arial', 20, 'bold'))
hud.setpos(bowx + 50, -190)
hud.write("Shots Left", False, align="center")
hud.setpos(targdist,100)
hud.pendown()
hud.color('black','red')
hud.begin_fill()
hud.fd(10)
hud.rt(90)
hud.fd(200)
hud.rt(90)
hud.fd(10)
hud.rt(90)
hud.fd(200)
hud.rt(90)
hud.end_fill()
hud.setpos(targdist,65)
hud.color('black','yellow')
hud.begin_fill()
hud.fd(10)
hud.rt(90)
hud.fd(130)
hud.rt(90)
hud.fd(10)
hud.rt(90)
hud.fd(130)
hud.rt(90)
hud.end_fill()
hud.setpos(targdist,25)
hud.color('black','green')
hud.begin_fill()
hud.fd(10)
hud.rt(90)
hud.fd(50)
hud.rt(90)
hud.fd(10)
hud.rt(90)
hud.fd(50)
hud.end_fill()
hud.hideturtle()

# Score Script
def score():
    dists = [arr1.distance(targdist,0), arr2.distance(targdist,0), arr3.distance(targdist,0)]
    score = 0
    num = 1
    hud.penup()
    hud.setpos(-50,30)
    hud.pendown()
    hud.begin_fill()
    hud.color('black','gray')
    hud.seth(0)
    for i in range(4):
        hud.fd(100)
        hud.rt(90)
    hud.end_fill()
    hud.penup()
    hud.setpos(0,0)
    hud.seth(270)
    for i in dists:
        if i <= 25:
            score = score + 50
            hud.color('Green')
            hud.write("Shot " + str(num) +": 50", False, align=('center'), font=('Arial', 15, 'normal'))
            hud.fd(20)
            num = num + 1
        elif i <= 65:
            score = score + 3
            hud.color('Yellow')
            hud.write("Shot " + str(num) +": 3", False, align=('center'), font=('Arial', 15, 'normal'))
            hud.fd(20)
            num = num + 1
        elif i <= 100:
            score = score + 1
            hud.color('Red')
            hud.write("Shot " + str(num) +": 1", False, align=('center'), font=('Arial', 15, 'normal'))
            hud.fd(20)
            num = num + 1
        else:
            hud.color('Black')
            hud.write("Shot " + str(num) + ": 0", False, align=('center'), font=('Arial', 15, 'normal'))
            hud.fd(20)
            num = num + 1
    hud.color('Black')
    hud.write("Score:  " + str(score), False, align=('center'), font=('Arial', 15, 'normal'))

# Gameplay Functions
def dir1(x,y):
    arr1.setpos(x,y)
    arr1.seth(arr1.towards(bow))
    if arr1.distance(bow) > 100:
        arr1.fd(arr1.distance(bow) - 100)

def dir2(x,y):
    arr2.setpos(x,y)
    arr2.seth(arr2.towards(bow))
    if arr2.distance(bow) > 100:
        arr2.fd(arr2.distance(bow) - 100)

def dir3(x,y):
    arr3.setpos(x,y)
    arr3.seth(arr3.towards(bow))
    if arr3.distance(bow) > 100:
        arr3.fd(arr3.distance(bow) - 100)

def shot1(x,y):
    strn = arr1.distance(bow)/50
    angle = arr1.heading()
    wind = random.randint(1,21)
    arr1.setpos(bow)
    arr1.speed(6)
    i = 0
    while True:
        if arr1.xcor() > targdist or arr1.xcor() < -550 or arr1.ycor() < -200:
            break
        if  i % 10 == 0:
            arr1.pendown()
        elif i % 5 == 0:
            arr1.penup()
        (tempx, tempy) = arr1.position()
        arr1.setpos(tempx + strn*math.cos(math.pi/180*angle), tempy + strn*math.sin(math.pi/180*angle)-(i*(1+wind/20)*g))
        arr1.seth(towards(tempx,tempy))
        i = i + 1
    arr1.penup()
    arr2.setpos(bow)

def shot2(x,y):
    strn = arr2.distance(bow)/50
    angle = arr2.heading()
    wind = random.randint(1,21)
    arr2.setpos(bow)
    arr2.speed(6)
    i = 0
    while True:
        if arr2.xcor() > targdist or arr2.xcor() < -550 or arr2.ycor() < -200:
            break
        if  i % 10 == 0:
            arr2.pendown()
        elif i % 5 == 0:
            arr2.penup()
        (tempx, tempy) = arr2.position()
        arr2.setpos(tempx + strn*math.cos(math.pi/180*angle), tempy + strn*math.sin(math.pi/180*angle)-(i*(1+wind/20)*g))
        arr2.seth(towards(tempx,tempy))
        i = i + 1
    arr2.penup()
    arr3.setpos(bow)


def shot3(x,y):
    strn = arr3.distance(bow)/50
    angle = arr3.heading()
    wind = random.randint(1,21)
    arr3.setpos(bow)
    arr3.speed(6)
    i = 0
    while True:
        if arr3.xcor() > targdist or arr3.xcor() < -550 or arr3.ycor() < -200:
            break
        if  i % 10 == 0:
            arr3.pendown()
        elif i % 5 == 0:
            arr3.penup()
        (tempx, tempy) = arr3.position()
        arr3.setpos(tempx + strn*math.cos(math.pi/180*angle), tempy + strn*math.sin(math.pi/180*angle)-(i*(1+wind/20)*g))
        arr3.seth(towards(tempx,tempy))
        i = i + 1
    arr3.penup()
    score()
        
arr1.setpos(bowx, bowy-2)
arr1.pendown()
arr1.circle(2)
arr1.penup()
arr1.setpos(bow)
arr2.setpos(bowx + 40,bowy - 200)
arr3.setpos(bowx + 60,bowy - 200)

arr1.ondrag(dir1)
arr1.onrelease(shot1)
arr2.ondrag(dir2)
arr2.onrelease(shot2)
arr3.ondrag(dir3)
arr3.onrelease(shot3)
mainloop()