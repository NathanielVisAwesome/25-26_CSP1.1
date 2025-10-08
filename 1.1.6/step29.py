# CODE TO COPY
#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

#legs config
legs = 6 #num of legs
legdist = 50 #leg distance
space = 360 / legs #sets spacing between the leg
ladybug.pensize(5)
inc = 0 #increment of distance between legs

#drawlegs
while inc < legs:
  ladybug.goto(0,-45)
  print(ladybug.pos())
  ladybug.setheading(space*inc) #change leg direction
  ladybug.forward(legdist)
  inc = inc + 1 #incrememnnt idk

# and body
ladybug.penup()
ladybug.goto(-17,-45)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while num_dots <= 2:
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()