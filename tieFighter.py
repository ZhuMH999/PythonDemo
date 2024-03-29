import turtle

# Create a turtle screen
wn = turtle.Screen()
wn.screensize(600, 800)
wn.bgcolor('black')

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()
t.pencolor('white')

# Draw an octagon
t.goto(0, -25)
t.pendown()
t.left(22.5)
for i in range(8):
    t.forward(18.5)
    t.left(45)

# Reset the turtle's heading
t.setheading(0)

# Draw Tie cockpit
t.penup()
t.goto(0, -50)
t.pendown()
t.circle(50)

# Draw lines radiating from the center
t.penup()
t.goto(0, 0)
for i in range(8):
    t.forward(25)
    t.pendown()
    t.forward(25)
    t.penup()
    t.goto(0, 0)
    t.left(45)

# Draw Tie body
t.goto(0, -80)
t.pendown()
t.circle(80)

# Draw two smaller guns at the bottom
t.penup()
t.goto(0, 0)
t.setheading(270)
t.left(22.5)
t.forward(50)
t.setheading(270)
t.pendown()
t.forward(20)
t.circle(7, 180)
t.forward(30)

t.penup()
t.goto(0, 0)
t.setheading(270)
t.right(22.5)
t.forward(50)
t.setheading(270)
t.pendown()
t.forward(20)
t.penup()
t.goto(int(t.xcor() - 14), t.ycor())
t.pendown()
t.circle(7, 180)
t.penup()
t.goto(int(t.xcor() - 14), t.ycor())
t.pendown()
t.forward(30)

# Top Half circle
t.penup()
t.goto(0, 0)
t.setheading(90)
t.left(40)
t.forward(80)
t.setheading(330)
t.pendown()
t.circle(100, 62)

# Left Wing
t.penup()
t.goto(-80, 10)
t.pendown()
t.setheading(180)
t.forward(150)
t.penup()
t.goto(-80, -10)
t.pendown()
t.forward(150)
t.setheading(90)
t.forward(90)
t.right(45)
t.forward(90)
t.penup()
t.goto(-230, -10)
t.setheading(270)
t.pendown()
t.forward(80)
t.left(45)
t.forward(90)
t.right(135)
t.forward(10)
t.right(45)
t.forward(90)
t.right(45)
t.forward(170)
t.right(45)
t.forward(90)
t.right(45)
t.forward(10)

# Right Wing
t.penup()
t.goto(80, 10)
t.pendown()
t.setheading(0)
t.forward(150)
t.penup()
t.goto(80, -10)
t.pendown()
t.forward(150)
t.setheading(90)
t.forward(90)
t.left(45)
t.forward(90)
t.penup()
t.goto(230, 0)
t.setheading(270)
t.pendown()
t.forward(90)
t.right(45)
t.forward(90)
t.left(135)
t.forward(10)
t.left(45)
t.forward(90)
t.left(45)
t.forward(170)
t.left(45)
t.forward(90)
t.left(45)
t.forward(10)

# Keep the window open
wn.mainloop()
