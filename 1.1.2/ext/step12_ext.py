# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color = input("What is the color of the circle?")

# ask user for the radius of a circle
radius = int(input("What is the radius of the circle?"))

# ask user for the stroke size
stroke = int(input("What is the stroke size of the circle?"))

# draw a circle with the radius and line color entered by the user
#color calls user defined color variable
painter.color(color)
#circle calls user defined radius variable
painter.circle(radius)
#pensize calls user defined stroke variable
painter.pensize(stroke)

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()