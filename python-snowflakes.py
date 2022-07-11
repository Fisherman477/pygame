#!/bin/python3

import random
from random import randint
import turtle
vin=turtle.Turtle()
vin.speed("max")

turtle.Screen().bgcolor("sky blue")
colours = ["black", "cyan", "blue", "maroon", "purple", "green"]
vin.pensize(4)
#branch function (12.09.21)
def branch():
  for i in range(3):
    for i in range(3):
      vin.forward(30)
      vin.backward(30)
      vin.right(45)
    vin.left(90)
    vin.backward(30)
    vin.left(45)
  vin.right(90)
  vin.color(random.choice(colours))
  
#miniature branch function (12.16.21)
def babybranch():
  vin.color("white")
  for i in range(3):
    for i in range(3):
      vin.forward(10)
      vin.backward(10)
      vin.right(45)
    vin.left(90)
    vin.backward(10)
    vin.left(45)
  vin.right(90)
  
  
#calling the branch function
for i in range(7):
  branch()
  vin.forward(90)
  vin.left(45)
branch()

#spiral bit (12.10.21)
# r = circle radius
vin.pensize(3)
vin.setheading(0)
vin.color("gray")
vin.right(90)
vin.forward(10)
vin.left(90)

r=10
for i in range(22):
  vin.circle(r+i,60)
  
#call this for testing purposes
#gets and prints the X and Y coordinates (12.16.21)
def GetC():
  x = vin.xcor()
  y = vin.ycor()
  print(x)
  print(y)
  
#this bit looks stupid, and it is
#but its how vin gets set up to write Happy Holidays
#without it they wrte in the wrong place
vin.left(81)
vin.forward(40)
vin.penup()
vin.goto(0,0)
vin.setheading(0)
vin.forward(30)
vin.right(90)
vin.forward(60)

vin.goto(75,-55)
vin.right(45)

#makes a baby snowflake
vin.pensize(3)
def babysf():
  vin.pendown()
  for i in range(7):
    babybranch()
    vin.forward(30)
    vin.left(45)
  babybranch()
  

for i in range(5):
  vin.penup()
  vin.goto(randint(-190,190),randint(-190,20))
  vin.pendown()
  babysf()
  vin.penup()
  
for i in range(3):
  vin.penup()
  vin.goto(randint(0,190),randint(0,190))
  vin.pendown()
  babysf()
  vin.penup()

#has vin write the Happy Holidays bit
vin.goto(80,-60)
vin.color("black")
vin.write("Happy Holidays!", align="center", font=("veranda", 16, "normal"))
vin.ht()

