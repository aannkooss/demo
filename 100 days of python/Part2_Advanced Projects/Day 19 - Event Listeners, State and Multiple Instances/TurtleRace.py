#Ankush Joshi
#October 9, 2024
#Day 19 - Turtle Race

from turtle import *
from venv import create

screen = Screen()
screen.setup(500, 400) #500x400 (w by h) size
userChoice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

redTurtle = Turtle()
redTurtle.color("Indian Red")

orangeTurtle = Turtle()
orangeTurtle.color("Orange")

pinkTurtle = Turtle()
pinkTurtle.color("Pink")

greenTurtle = Turtle()
greenTurtle.color("Dark Green")

blueTurtle = Turtle()
blueTurtle.color("blue")

purpleTurtle = Turtle()
purpleTurtle.color("purple")

turtles = [redTurtle, orangeTurtle, pinkTurtle, greenTurtle, blueTurtle, purpleTurtle]

def createTurtle():
    for turtle in turtles:
        turtle.shape("turtle")

def positionTurtles():
    createTurtle()
    positionFactor = 50
    yValue = -150

    for turtle in turtles:
        turtle.penup()
        yValue += positionFactor
        turtle.goto(-230, yValue)

positionTurtles()

#set turtle speed random
#set condition for winning bet and printing ot terminal
screen.exitonclick()