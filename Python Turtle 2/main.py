from turtle import *

move_distance = 20

# Set up the screen
bgcolor("#d2691E")

penup()
goto(100,200)
pendown()

# Draw a rectangle
color("blue")

begin_fill()
goto(300,200)
goto(300,-200)
goto(100,-200)
goto(100,200)
end_fill()

# Draw a turtle shape
penup()
goto(-200, 0)
shape("turtle")
color("green")

# Function to move the turtle in different directions
def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)  
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() > 100:
         hideturtle()
         color("white")
         write("Goal Reached!", align="center", font=("Arial", 16, "normal"))

         onkey(None, "up")
         onkey(None, "down")
         onkey(None, "left")
         onkey(None, "right")


# Keyboard bindings

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")

listen()
done()

