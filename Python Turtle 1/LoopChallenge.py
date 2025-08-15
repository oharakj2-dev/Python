from turtle import *

num = 8

def move_and_turn(angle):
    forward(50)
    right(angle)

for x in range(num):
    move_and_turn(45)

done()