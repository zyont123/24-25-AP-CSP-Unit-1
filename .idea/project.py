

import turtle as trtl


t = trtl.Turtle()
t.speed(0)

def color(color):
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


t.circle(100)
t.circle(95)
t.circle(90)
t.circle(85)
t.circle(80)
t.circle(75)
t.circle(70)
def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']


radius=100
interval=10

for r_color in roygbiv:
    filled_circle(radius,r_color)
    radius -= interval

    # Move turtle a up by a littel
    t.left(90)
    t.forward(interval)
    t.right(90)
def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def rainbow(radius=100,interval=10):
    roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    for r_color in roygbiv:
        filled_circle(radius,r_color)
        radius -= interval

        # Move turtle a up by a little
        t.left(90)
        t.forward(interval)
        t.right(90)


rainbow(100,10)




def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def cloud(radius, cloud_color="white"):
    filled_circle(radius,cloud_color)
    t.forward(radius)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)

def rainbow(radius=100,interval=10):
    roygbiv=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    for r_color in roygbiv:
        filled_circle(radius,r_color)
        radius -= interval

        # Move turtle a up by a little
        t.left(90)
        t.forward(interval)
        t.right(90)

t.penup()

t.goto(100,900)
cloud(20)
t.goto(-50,850)
cloud(30)
t.goto(50,600)
cloud(50)
t.goto(200,500)
cloud(5)

t.goto(0,0)
rainbow(1000,10)

t.goto(-200,200)
cloud(15)
t.goto(50,200)
cloud(10)
t.goto(50,200)
cloud(10)


t.goto(-90, 150)
cloud(10)

t.goto(110,180)
cloud(15)


t.goto(150, 350)
cloud(10)

t.goto(-30, 200)
cloud(10)

t.goto(-150, 300)
cloud(10)

t.goto(-250, 450)
cloud(10)

t.goto(-200, 450)
cloud(10)



t.color("white","white")
t.begin_fill()
t.circle(10)
t.end_fill()

def filled_circle(radius, color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


radius = 10
cloud_color="white"

filled_circle(radius,cloud_color)
t.forward(radius)
filled_circle(radius,cloud_color)
t.right(50)
filled_circle(radius,cloud_color)
t.right(50)
filled_circle(radius,cloud_color)
t.right(50)
filled_circle(radius,cloud_color)
t.right(50)





wn = trtl.Screen()
wn.bgcolor('lightblue')
'''wn.screensize(100,100)
wn.setworldcoordinates(-300,300,300,900)
wn.tracer(0,0)
'''
wn.mainloop()