import turtle as trtl
import time

print(time.localtime())

print("Painting!")

painter = trtl.Turtle()

painter.color("green")
painter.speed(10101010101010101110)
painter.turtlesize(15)
painter.pensize(10)
painter.right(45)
painter.forward(250)
painter.right(90)

painter2 = trtl.Turtle()

painter2.color('blue')
painter2.turtlesize(1)
painter2.pensize(5)
painter2.right(15)
painter2.backward(300)

painter3 = trtl.Turtle()

painter3.color('red')
painter3.right(0)
painter3.pensize(20)
painter3.forward(100)
painter3.circle(radius=150)

painter4 = trtl.Turtle()

painter4.pensize(10)
painter4.right(90)
painter4.forward(100)
painter4.teleport(100, 35)
painter4.forward(100)

print("Painted, Enjoy!")

wn = trtl.Screen()
wn.mainloop()
