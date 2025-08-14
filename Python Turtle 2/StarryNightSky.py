from turtle import *
from random import *

speed(0)

# Initialize the screen
bgcolor("black")
hideturtle()

# Get the window dimensions
width = window_width()
height = window_height()

# Function to draw a star at a given position
def draw_star(xpos, ypos):
    size = randrange(2, 7)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "yellow")

# Main loop to draw stars
for x in range(100):
    xpos = randrange(-width // 2, width // 2)
    ypos = randrange(-height // 2, height // 2)
    draw_star(xpos, ypos)

done()

