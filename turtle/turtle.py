# import random
from turtle import Turtle, Screen
import random


turtle = Turtle()
screen = Screen()
dashed_turtle = Turtle()
all_turtle = Turtle()
random_turtle = Turtle()
circular_turtle = Turtle()


def square():
    turtle.shape("turtle")
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def dashed_square():
    dashed_turtle.shape("turtle")
    for j in range(4):
        for i in range(5):
            dashed_turtle.forward(20)
            dashed_turtle.penup()
            dashed_turtle.forward(20)
            dashed_turtle.pendown()
        dashed_turtle.right(90)


def draw_all_shapes():
    for i in range(3,11):
        for j in range(i):
            all_turtle.forward(100)
            all_turtle.right(360/i)


def random_walk(n):
    directions = [0, 90, 180, 270]
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    random_turtle.pensize(15)
    for i in range(n):
        random_turtle.forward(40)
        random_turtle.right(random.choice(directions))
        random_turtle.color(random.choice(colours))
        random_turtle.speed(random.choice(range(11)))


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def circular_circle(n):
    screen.colormode(255)
    circular_turtle.speed(10)
    for i in range(n):
        colour = color_change()
        circular_turtle.color(colour)
        circular_turtle.circle(50)
        circular_turtle.left(360/n)



circular_circle(50)
screen.exitonclick()

