"""
This program demonstrates drawing a star on the window using the turtle module.
The star would be drawn on the screen when mouse clicks on the screen.
But when drawing in progress, no new stars would be drawn.

@Author : ZhuMH999
"""

import turtle
from random import randint


def drawStar(x, y):
    """
    This function draws a star at the required position specified by x and y.
    The number of points and color of the star are randomly generated.
    :param x: The x coordinate of the star
    :param y: The y coordinate of the star
    """
    global drawing
    if drawing:  # Checks if drawing in progress
        return
    drawing = True
    points = (randint(2, 10) * 2) + 1  # Randomly generates an odd number of points
    angle = 180 - (180/points)
    size = randint(10, 40)

    player.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    player.penup()
    player.goto(x, y)
    player.pendown()

    for i in range(points):
        player.begin_fill()
        player.forward(size)
        player.right(angle)
    drawing = False

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgcolor('dark blue')

    turtle.colormode(255)
    player = turtle.Turtle()
    player.speed(0)
    player.hideturtle()
    drawing = False  # Indicates whether turtle is drawing in progress.

    turtle.onscreenclick(drawStar)
    turtle.mainloop()
