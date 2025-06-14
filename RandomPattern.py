import turtle as t
import random

tom = t.Turtle()

colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "brown",
    "gray", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal", "aqua", "silver",
    "gold", "violet", "indigo", "beige", "chocolate", "coral", "darkblue", 
    "darkgreen", "darkred", "lightblue", "lightgreen", "lightpink", "lavender", 
    "peachpuff", "salmon", "seagreen", "sienna", "skyblue", "slategray", "tan", 
    "tomato", "turquoise", "wheat", "plum", "orchid", "khaki", "mintcream", "ivory"
]
direction = [0,90,180,270]
tom.pensize(10)
tom.speed("fastest")

for _ in range(300):
    tom.color(random.choice(colors))
    tom.forward(30)
    tom.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()