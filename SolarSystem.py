import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")   # space background
screen.title("Sun in Space")

# Create turtle for sun
sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)

# Draw the sun
sun.penup()
sun.goto(0, -100)   # center the circle
sun.pendown()
sun.color("yellow")
sun.begin_fill()
sun.circle(100)
sun.end_fill()

# Draw sun rays
sun.penup()
sun.goto(0, 0)
sun.pendown()
sun.pensize(2)

for _ in range(36):  # 36 rays
    sun.penup()
    sun.forward(100)
    sun.pendown()
    sun.forward(50)
    sun.penup()
    sun.backward(150)
    sun.right(10)

# --- Draw stars in background ---
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.color("white")

for _ in range(200):   # number of stars
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    stars.penup()
    stars.goto(x, y)
    stars.dot(random.randint(2, 4))  # random star size

# Keep window open
screen.mainloop()
