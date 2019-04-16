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
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple", "teal", "pink"]

#random capabilities
import random


#TO DO: Change paint to random size circles at random points on the screen
# void drawObstacle() {
#     double x = this.rand.nextDouble() * this.dimensions.width;
#     double y = this.rand.nextDouble() * this.dimensions.height;
# }

#pick up pen so that there are individual lines
t1.up()
#move pen left
t1.goto(-200,0)
#pen down to draw
t1.down()
#pen thickness
t1.width(10)
#Hide turtle icon
#t1.hideturtle()
#Set turtle speed to Max speed
t1.speed(0)

#loop for graphics to be built
                #run a long time
for i in range(100000000):
    #choose random color
    colorChoice = random.choice(colors)
    #make turtle take on random color
    t1.color(colorChoice)
    #move turtle forward
    t1.forward(400)
    #have turtle turn 180 degrees (x>180 is clockwise x<180 is counter clockwise)
    t1.right(213)
