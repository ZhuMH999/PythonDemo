"""
This program demonstrates Tic Tac Toe using the Turtle module.
The turtle will first draw out the playing grid,
when the player clicks on the respective boxes, X or O will be drawn on the screen.
However, if the box already has an X or O, nothing else would be drawn on it.

@Author : ZhuMH999
"""
import turtle
import math

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')

t = turtle.Turtle()
t.pencolor('white')
t.pensize(5)
t.speed(0)
t.hideturtle()
player = 'O'
xLocation = 0
yLocation = 0
win = False

a = [['', '', ''], ['', '', ''], ['', '', '']]

#  These are the coordinates for drawing the symbols.
location = [[(-200, -200), (0, -200), (200, -200)], [(-200, 0), (0, 0), (200, 0)], [(-200, 200), (0, 200), (200, 200)]]

def drawGrid():  # This draws the playing grid.
    global t

    t.penup()
    t.goto(-100, 300)
    t.pendown()
    t.goto(-100, -300)

    t.penup()
    t.goto(100, 300)
    t.pendown()
    t.goto(100, -300)

    t.penup()
    t.goto(-300, 100)
    t.pendown()
    t.goto(300, 100)

    t.penup()
    t.goto(-300, -100)
    t.pendown()
    t.goto(300, -100)

def locateGrid(x, y):  # This locates which grid the player clicked.
    global player, xLocation, yLocation
    x += 300
    y += 300
    xLocation = int(math.floor(x / 200))
    yLocation = int(math.floor(y / 200))
    if a[yLocation][xLocation] == '':
        a[yLocation][xLocation] = player
        drawScreen(player)
        checkWin()

def drawX():  # This draws the 'X' symbol on the grid.
    global xLocation, yLocation, player
    t.penup()
    t.goto(location[yLocation][xLocation])
    t.pendown()
    t.setheading(90)
    t.right(45)
    t.forward(50)
    t.backward(100)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(100)

def drawO():  # This draws the 'O' symbol on the grid.
    global xLocation, yLocation, player
    t.penup()
    t.goto(location[yLocation][xLocation])
    t.setheading(90)
    t.right(90)
    t.forward(50)
    t.pendown()
    t.left(90)
    t.circle(50)
    t.left(45)

def drawScreen(XorO):
    global player
    if XorO == 'X':
        drawX()
    if XorO == 'O':
        drawO()

def writeWin():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.clear()
    t.write(player + ' wins!', align='center', font=('Arial', 60, 'normal'))

def checkWin():
    global player, xLocation, yLocation
    #  Checks the vertical and horizontal
    if (a[0][xLocation] == player and a[1][xLocation] == player and a[2][xLocation] == player) or (a[yLocation][0] == player and a[yLocation][1] == player and a[yLocation][2] == player):
        writeWin()
    #  Checks the diagonal "\"
    if (xLocation == 0 and yLocation == 0) or (xLocation == 2 and yLocation == 2) or (xLocation == 1 and yLocation == 1):
        if (a[0][0] == player) and (a[1][1] == player) and (a[2][2] == player):
            writeWin()
    #  Checks the diagonal "/"
    if (xLocation == 0 and yLocation == 2) or (xLocation == 2 and yLocation == 0) or (xLocation == 1 and yLocation == 1):
        if (a[2][0] == player) and (a[1][1] == player) and (a[0][2] == player):
            writeWin()

    if player == 'X':
        player = 'O'
    else:
        player = 'X'


drawGrid()
turtle.onscreenclick(locateGrid)

turtle.mainloop()
