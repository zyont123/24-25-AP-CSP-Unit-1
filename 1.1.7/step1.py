#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange",  "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#
startx = 10
starty = 10



#
for t in my_turtles:
  t.goto(startx, starty)
  t.right(50)
  t.forward(50)
  t.penup()
  t.pendown()
  t.left(90)
  t.right(90)

#
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()