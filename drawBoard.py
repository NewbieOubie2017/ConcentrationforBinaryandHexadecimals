import turtle
from turtle import Screen
from turtle import *

class drawBoard():
    screen = Screen()
    screen.setup(width=600, height=600, startx=10, starty=10)


    # Draw large off-white square
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-250, -250)
    color('#000000', '#e4e4ff')
    begin_fill()
    turtle.pendown()
    forward(500)
    left(90)
    forward(500)
    left(90)
    forward(500)
    left(90)
    forward(500)
    end_fill()
    turtle.penup()


    #draw vertical lines
    turtle.goto(-150, 250)
    turtle.pendown()
    turtle.goto(-150, -250)
    turtle.penup()

    turtle.goto(-50, 250)
    turtle.pendown()
    turtle.goto(-50, -250)
    turtle.penup()

    turtle.goto(50, 250)
    turtle.pendown()
    turtle.goto(50, -250)
    turtle.penup()

    turtle.goto(150, 250)
    turtle.pendown()
    turtle.goto(150, -250)
    turtle.penup()

    # draw horizonal lines
    turtle.goto(-250, -150)
    turtle.pendown()
    turtle.goto(250, -150)
    turtle.penup()

    turtle.goto(-250, -50)
    turtle.pendown()
    turtle.goto(250, -50)
    turtle.penup()

    turtle.goto(-250, 50)
    turtle.pendown()
    turtle.goto(250, 50)
    turtle.penup()

    turtle.goto(-250, 150)
    turtle.pendown()
    turtle.goto(250, 150)
    turtle.penup()
    #print('Board Drawn')

