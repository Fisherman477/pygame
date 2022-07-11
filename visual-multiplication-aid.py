import turtle

#-----sets turtle speed, gains useer input, and sets the starting point
turtle.speed(0)
print("maximum is 15x15")
numa = input("number 1?")
numb = input("number 2?")
startX = -175
startY = 175


#-----creates one dot at any given point on our grid
def one_dot(x,y):
  turtle.penup()
  turtle.goto(startX+(25*x),startY-(25*y))
  turtle.pendown()
  turtle.dot(10)
  turtle.penup()

#-----creates one row of dots with the amount of dots being user input "number 1?"
def one_row(y):
  i = 0
  one_dot(0,0)
  while i < int(numa):
    one_dot(i,y)
    i += 1


#-----creates (x) rows of dots with x being user input "number 2?" 
def all_rows():
  k = 0
  while k < int(numb):
    one_row(k)
    k += 1


all_rows()