import turtle as trtl

print("Painting!")

painter = trtl.Turtle()

painter.color("green")
painter.turtlesize(15)
painter.pensize(10)
painter.forward(250)
painter.right(15)

print("Painted, Enjoy!")

wn = trtl.Screen()
wn.mainloop()
