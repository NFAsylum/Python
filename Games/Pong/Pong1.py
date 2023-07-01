import turtle
import winsound
import time
import os

#===============================================#
#-----------------------------------------------#
#===============================================#

# Screen
wn = turtle.Screen()
wn.title("Pong by Marco")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle L
paddleL = turtle.Turtle()
paddleL.speed(0)
paddleL.shape("square")
paddleL.color("white")
paddleL.penup()
paddleL.goto(-350, 0)
paddleL.shapesize(stretch_wid=5, stretch_len=1)

# Paddle R
paddleR = turtle.Turtle()
paddleR.speed(0)
paddleR.shape("square")
paddleR.color("white")
paddleR.penup()
paddleR.goto(350, 0)
paddleR.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3.5
ball.dy = 3.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
scoreL = 0
scoreR = 0

#===============================================#
#-----------------------------------------------#
#===============================================#

# Functions
def paddleLUp():
    y = paddleL.ycor()
    y += 20
    paddleL.sety(y)
def paddleLDown():
    y = paddleL.ycor()
    y -= 20
    paddleL.sety(y)

def paddleRUp():
    y = paddleR.ycor()
    y += 20
    paddleR.sety(y)
def paddleRDown():
    y = paddleR.ycor()
    y -= 20
    paddleR.sety(y)

#def ball():

#===============================================#
#-----------------------------------------------#
#===============================================#

# Keyboard
wn.listen()

# Left Paddle
wn.onkeypress(paddleLUp, "w")
wn.onkeypress(paddleLDown, "s")

# Right Paddle
wn.onkeypress(paddleRUp, "Up")
wn.onkeypress(paddleRDown, "Down")

#===============================================#
#-----------------------------------------------#
#===============================================#

# Main loop
while True:
    time.sleep(1/60)
    wn.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball hitting borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        #ball.setx(390)
        ball.dx *= -1
        ball.dx += 1.05
        scoreL += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreL, scoreR), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        #ball.setx(-390)
        ball.dx *= -1
        ball.dx += 1.05
        scoreR += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreL, scoreR), align="center", font=("Courier", 24, "normal"))

    # Ball hitting paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleR.ycor() + 40 and ball.ycor() > paddleR.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleL.ycor() + 40 and ball.ycor() > paddleL.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

    # Paddles limits
    if paddleL.ycor() > 250:
        paddleL.sety(250)
    if paddleL.ycor() < -250:
        paddleL.sety(-250)

    if paddleR.ycor() > 250:
        paddleR.sety(250)
    if paddleR.ycor() < -250:
        paddleR.sety(-250)