""" Draw a cube, lots of cubes!!!

Authored by Emma and Daddy <3 (Kyle)
"""
import random
import turtle


def draw_square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)


def draw_left_square():
    turtle.left(30)
    turtle.forward(80)
    turtle.right(30)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(30)
    turtle.forward(80)
    turtle.right(30)
    turtle.left(90)


def draw_top_square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(30)
    turtle.forward(80)
    turtle.right(30)
    turtle.left(90)
    turtle.forward(100)


def draw_cube():
    draw_square()
    draw_left_square()
    draw_top_square()


def move_turtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_lots_of_turtles(
    cubes_to_draw,
    x_start,
    y_start,
):
    """Draw lots of cubes!

    The name was a mistake on Daddy's part, but Daughter decided it was too
    funny to fix.
    """
    for z in range(cubes_to_draw):

        color = tuple(random.choices(range(256), k=3))
        turtle.pencolor(color)

        move_turtle(x_start + z, y_start + z)
        draw_cube()


turtle.speed(0)
turtle.colormode(255)


CUBES_TO_DRAW = 70


draw_lots_of_turtles(
    cubes_to_draw=CUBES_TO_DRAW,
    x_start=-300,
    y_start=-300,
)
draw_lots_of_turtles(
    cubes_to_draw=CUBES_TO_DRAW,
    x_start=300,
    y_start=300,
)


turtle.done()
