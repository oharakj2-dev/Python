from turtle import *

diameter = 40
pop_diameter = 100
pop = False

def draw_balloon():
    color("red")
    dot(diameter)

def inflate_balloon():
    global diameter, pop
    diameter += 10
    if pop:
        clear()
        pop = False
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 20
        write("pop!", align="center", font=("Arial", 24, "bold"))
        pop = True

draw_balloon()
onkey(inflate_balloon, "space")
listen()

done()