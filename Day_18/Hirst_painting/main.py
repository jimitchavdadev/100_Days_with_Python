import turtle as t
import colorgram as cg
import random

color_pallete = [
    (253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32),
    (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69),
    (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
    (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
    (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62),
    (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
    (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
    (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233),
    (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110),
    (243, 15, 14), (38, 43, 221)
]

jimmy = t.Turtle()
t.colormode(255)

jimmy.penup()
jimmy.hideturtle()
jimmy.goto(-100, -100)
jimmy.setheading(0)
jimmy.speed("fastest")


def hirst():
    for _ in range(10):
        for _ in range(10):
            jimmy.dot(20, random.choice(color_pallete))
            jimmy.forward(50)
        jimmy.setheading(90)
        jimmy.forward(50)
        jimmy.setheading(180)
        jimmy.forward(500)
        jimmy.setheading(0)


hirst()
screen = t.Screen()
screen.exitonclick()
