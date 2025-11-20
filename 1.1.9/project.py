# Import APIs
import turtle as trtl

# Define Variable(s)

sk = trtl.Turtle()

# Define List(s)

print("well, looks like there are no lists!")

# Create Skelebro Head

sk.pencolor("beige")
sk.fillcolor("beige")
sk.pensize(25)

# Skelebro Variables

size = 50
ychange = 50
ypos = 0

for t in range(1):
    # Do the main head
    sk.penup()
    sk.goto(0, sk.ycor()+ychange)

    ypos = sk.ycor()

    sk.pendown()
    sk.begin_fill()
    sk.circle(size)
    sk.end_fill()
    ychange = -25

    for l in range(1):
        # Do the jaw
        sk.goto(0, sk.ycor()+ychange)
        sk.begin_fill()
        sk.circle(size / 2)
        sk.end_fill()

# Eye Variable(s)
eye_color = "black"
pupil = "red"
fillcol_eye = "black"
fillcol_pup = "red"

# Draw the eyes & pupils

eye_size = 10
pupil_size = 1
xpos = 10

sk.pencolor(eye_color)

# Draw the Eyes

for t in range(2):

    # Draw the eyeholes
    sk.pencolor(eye_color)
    sk.fillcolor(fillcol_eye)
    sk.penup()
    sk.goto(xpos-35, ypos*2)
    sk.pendown()
    sk.begin_fill()
    sk.circle(eye_size)
    sk.end_fill()
    sk.penup()

    # Draw the pupils
    sk.pencolor(pupil)
    sk.fillcolor(fillcol_pup)
    sk.goto(xpos-35, (ypos*2)+5)
    sk.pendown()
    sk.begin_fill()
    sk.circle(pupil_size)
    sk.end_fill()

    # Change position of eye
    xpos = (xpos+20)*2

# Nose variables
xpos = 10
nose_size = 0.25
nose_color = "black"
nose_fill = "black"

# Draw the Nose
for t in range(2):
    sk.penup()
    sk.pencolor(nose_color)
    sk.fillcolor(nose_fill)
    sk.goto(xpos-15,(ypos*2)-20)
    sk.pendown()
    sk.circle(nose_size)

    xpos = xpos*2

# teeth

sk.pensize(5)
toothline = 40
heading = 90
xpos = -15
ypos = 40

for t in range(3):
    sk.penup()
    sk.goto(xpos,ypos-25)
    sk.pendown()
    sk.setheading(heading)
    sk.forward(toothline)
    sk.penup()

    xpos = xpos+15

    if ypos == 40:
        ypos = ypos-5
    elif ypos == 35:
        ypos = ypos+5
    else:
        ypos = 40

wn = trtl.Screen()
wn.mainloop()