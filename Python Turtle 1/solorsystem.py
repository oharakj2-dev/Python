from turtle import *

bgcolor("black")

#create orange planet
color("orange")
begin_fill()
circle(60)
end_fill()

#move to next planet
penup()
forward(100)
pendown()

#create grey planet
color("grey")
begin_fill()
circle(20)
end_fill()

#move to next planet
penup()
forward(80)
pendown()

# create red planet
color("red")
begin_fill()
circle(40)
end_fill()

#move to next planet
penup()
forward(90)
pendown()

#create green planet
color("green")
begin_fill()
circle(30)
end_fill()


done()