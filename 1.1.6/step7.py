# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name turt is used
spdr = trtl.Turtle()

#draws the body
spdr.pensize(40)
spdr.circle(20)

#leg variables
legs = 8 #num of legs
legdist = 70 #leg distance
space = 320 / legs #sets spacing between the leg
spdr.pensize(5)
inc = 0 #increment of distance between legs

#draws the legs
while inc < legs/2:
  spdr.goto(0,20)
  spdr.setheading(space*inc) #change leg direction
  spdr.forward(legdist)
  inc = inc + 1 #incrememnnt idk
spdr.setheading(180)
while inc < legs and not inc < 4:
    spdr.goto(0, 20)
    spdr.setheading(space*inc)
    spdr.forward(legdist)
    inc = inc + 1

spdr.penup()
spdr.goto(15,0)
spdr.pendown()
spdr.color("red")
spdr.circle(1)
spdr.penup()
spdr.goto(35,15)
spdr.pendown()
spdr.circle(1)

spdr.hideturtle()
wn = trtl.Screen()
wn.mainloop()