# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Exercise 5-5: Write a program that implements a simple 
# rollover. In other words, if the mouse is over a 
# rectangle, the rectangle changes color. 

x = 50
y = 50
w = 100
h = 75

def setup(): 
    size(200,200)

def draw(): 
    background(255)
    stroke(0)
    if (mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h): 
        fill(0)
    else: 
        fill(175)

    rect(x,y,w,h)
