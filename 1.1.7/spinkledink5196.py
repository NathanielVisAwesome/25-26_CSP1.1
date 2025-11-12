# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["gold", "purple", "orange", "green", "blue", "red"]

ct = 0
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors[ct])
  t.penup()
  my_turtles.append(t)
  ct += 1

#
startx = -50
starty = 50

#
direction = 45
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.forward(50)
  direction = t.heading() -45

#
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
wn.cl