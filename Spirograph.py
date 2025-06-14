import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.speed("fastest")

def spirograph(size):
    for _ in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)

spirograph(5)

screen = t.Screen()
screen.exitonclick()