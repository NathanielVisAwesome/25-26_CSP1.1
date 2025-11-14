import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["circle", "arrow", "turtle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 67
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50

pixel_size = 20
distance = 1
move_back_x = 0
move_back_y = 0
for step in range (50):
    # For each vertical turtle
    for vt in vert_turtles:
        # For each horizontal turtle
        for ht in horiz_turtles:
            # Move each forward
            ht.forward(distance)
            vt.forward(distance)
            distance += 1

            if distance >= 10:
                distance = 1
            # If they collide
            if abs(ht.xcor() - vt.xcor()) < pixel_size:
                if abs(ht.ycor() - vt.ycor()) < pixel_size:
                    # define variables
                    ht_color = ht.fillcolor()
                    vt_color = vt.fillcolor()
                    ht_shape = ht.shape()
                    vt_shape = vt.shape()

                    # Move turtle backwards
                    ht.back(distance + 10)
                    vt.back(distance + 20)

                    # Once distance is far enough
                    if abs(ht.ycor() == move_back_x):
                        if abs(vt.xcor == move_back_y):
                            # move vertical turtle forward first
                            vt.forward(distance)

                            if vt.xcor == distance + 25:
                                ht.forward(distance)
                                
                    '''
                    # Turn the vertical turtle grey
                    vt.fillcolor("grey")

                    # Remove the horizontal turtle
                    ht.clear()
                    ht.hideturtle()

                    # Remove turtle from the list
                    horiz_turtles.remove(ht)
                    vert_turtles.remove(vt)
                    '''

wn = trtl.Screen()
wn.mainloop()