#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition
x = 0
while x < 0:  # condition is false immediately
    trtl.forward(100)

# Add an infinite loop
while True:
    trtl.forward(100)
    trtl.right(90)  # keeps turning and making squares endlessly

wn = trtl.Screen()
wn.mainloop()