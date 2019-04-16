#Creating a color wheel in Python
    #I will try to use this with the implementation
    #of the random colors I need for the opening screen
    #the random color obstacles and the end screen

#Import graphics capabilities
from turtle import *

#pop-up window
setup()

t1 = Turtle()

#List of colors that the program will have to choose from
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

#random capabilities
import random

#pick up pen so that there are individual lines
t1.up()
#move pen left
t1.goto(-200,0)
#pen down to draw
t1.down()
#pen thickness
t1.width(5)
#Hide turtle icon???
t1.hideturtle()

#loop for graphics to be built
for i in range(9001):
    #choose random color
    colorChoice = random.choice(colors)
    #make turtle take 
    t1.color(colorChoice)

