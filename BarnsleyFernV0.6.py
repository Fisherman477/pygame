import turtle
import random

v = turtle.Turtle()
v.speed(0)
v.color("green")
v.penup()

x = 0
y = 0
for n in range(11000):
    v.goto(65 * x, 35 * y - 250)  # scale the fern to fit nicely inside the window
    v.pendown()
    v.dot(3)
    v.penup()
    r = random.random()
    if r < 0.01:
        x, y =  0.00 * x + 0.00 * y,  0.00 * x + 0.16 * y + 0.00
    elif r < 0.86:
        x, y =  0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60
    elif r < 0.93:
        x, y =  0.20 * x - 0.26 * y,  0.23 * x + 0.22 * y + 1.60
    else:
        x, y = -0.15 * x + 0.28 * y,  0.26 * x + 0.24 * y + 0.44