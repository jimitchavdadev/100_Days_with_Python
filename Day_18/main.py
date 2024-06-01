import turtle as t
import random
import colorgram

jimmy = t.Turtle()
jimmy.shape("turtle")
jimmy.color("red")


def square():
    for i in range(4):
        jimmy.forward(100)
        jimmy.right(90)


# colored way of doing it
def dashed_color():
    for _ in range(20):
        jimmy.forward(10)
        jimmy.color("white")
        jimmy.forward(10)
        jimmy.color("black")


# using penup, pendown
def dashed_pen():
    jimmy.color("black")
    for _ in range(20):
        jimmy.forward(10)
        jimmy.penup()
        jimmy.forward(10)
        jimmy.pendown()


shapes = {
    "triangle": [3, 180-60],
    "square": [4, 180-90],
    "pentagon": [5, 180-108],
    "hexagon": [6, 180-120],
    "heptagon": [7, 180-128.57],  # Approximately
    "octagon": [8, 180-135],
    "nonagon": [9, 180-140],
    "decagon": [10, 180-144]
}


def shape(aakar):
    for _ in range(shapes[aakar][0]):
        jimmy.forward(100)
        jimmy.left(shapes[aakar][1])


# defining the colormode range
t.colormode(255)

directions = [0, 90, 180, 270]

colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "turquoise", "gold",
    "lavender", "salmon", "coral", "aquamarine", "lime", "navy", "teal",
    "olive", "maroon", "chocolate", "indigo", "violet", "orchid", "khaki",
    "tan"
]

jimmy.pensize(1)
jimmy.speed("fastest")


# def random_walk():
#     direction = random.choice(directions)
#     rang = random.choice(colors)
#     jimmy.color(rang)
#     jimmy.forward(100)
#     jimmy.setheading(direction)


# function to generate random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


# function for random walk
def random_walk():
    direction = random.choice(directions)
    jimmy.color(random_color())
    jimmy.pencolor(random_color())
    jimmy.forward(100)
    jimmy.setheading(direction)


# function to draw spirograph
def spirograph(gap):
    for _ in range(round(360/gap)):
        jimmy.speed("fastest")
        jimmy.color(random_color())
        jimmy.circle(100)
        current_heading = jimmy.heading()
        jimmy.setheading(current_heading + gap)


t.bgcolor("LightBlue")

screen = t.Screen()
screen.exitonclick()
