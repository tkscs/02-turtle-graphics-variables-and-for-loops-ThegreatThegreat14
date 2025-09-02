from turtle import *

speed(3)

sides = 10
angle = 360/sides
for i in range (sides):
    forward(20)
    right(angle)

exitonclick()