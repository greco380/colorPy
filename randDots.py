#Creating a color wheel in Python
    #I will try to use this with the implementation
    #of the random colors I need for the opening screen
    #the random color obstacles and the end screen

#Import graphics capabilities
from turtle import *

#pop-up window
setup()

t1 = Turtle()
#pick up pen so that there are no trails
t1.up()

#List of colors that the program will have to choose from
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple", "teal", "pink"]

#random capabilities
import random

#TO DO: Change paint to random size circles at random points on the screen

while True:
    #Where the circles will be placed on the screen
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    #pen thickness
    t1.width(7)

    #How big the circles will randomly be
    circleSize = random.randint(1,100)

    #choose random color
    objectColor = random.choice(colors)

    #move pen to randomly chosen location
    t1.goto(x,y)

    #pen down to draw
    t1.down()

    #paint color
    t1.color(objectColor)

    #fill circle
    t1.begin_fill()
    #circle size
    t1.circle(circleSize)
    #fill circle
    t1.end_fill()

    #pick up pen so that there are individual lines
    t1.up()

    #Set turtle speed to Max speed
    t1.speed(0)

