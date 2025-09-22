# import the turtle module
import turtle
import turtle as trtl
from fileinput import close

# create the turtle object
painter = trtl.Turtle()

amount = int(input("How many times would you like to draw the circle?"))

print("making a circle...")
if amount == 2:
    painter2 = trtl.Turtle()
    asksecond = 1

# ask user for a color (such as red, green, blue, pink, purple)
color = input("What is the color of the circle? ")

# ask user for the radius of a circle
radius = int(input("What is the radius of the circle? "))

# ask user for the stroke size
stroke = int(input("What is the stroke size of the circle? "))

# draw a circle with the radius and line color entered by the user
#color calls user defined color variable
painter.color(color)
#pensize calls user defined stroke variable
painter.pensize(stroke)
#circle calls user defined radius variable
painter.circle(radius)

done = 1

if asksecond == 1:
    # ask user for a color (such as red, green, blue, pink, purple)
    color2 = input("What is the color of the second circle? ")

    # ask user for the radius of a circle
    radius2 = int(input("What is the radius of the second circle? "))

    # ask user for the stroke size
    stroke2 = int(input("What is the stroke size of the second circle? "))

    # draw a second circle with the radius and line color entered by the user
    # color calls user defined color variable
    painter2.color(color2)
    # pensize calls user defined stroke variable
    painter2.pensize(stroke2)
    # circle calls user defined radius variable
    painter2.circle(radius2)

    done = 2

if done == amount:
    print("you did it! goodbye!")
    turtle.bye()

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
