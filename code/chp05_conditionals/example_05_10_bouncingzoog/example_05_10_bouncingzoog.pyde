# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 5-10: Zoog and conditionals
x = 100.0
y = 100.0
w = 60.0
h = 60.0
eyeSize = 16.0

# Zoog has variables for speed in the horizontal and vertical direction.
xspeed = 3.0
yspeed = 1.0


def setup(): 
    size(480, 270)  

def draw(): 
    global x
    global y
    global xspeed
    global yspeed

    # Change the location of Zoog by speed
    x = x + xspeed
    y = y + yspeed

    # An IF statement with a logical OR determines if Zoog has reached either the right or left edge of the screen.  
    # When this is true, we multiply speed by -1, reversing Zoog's direction!
    # Identical logic is applied to the y direction as well.
    if ((x > width) or (x < 0)):
        xspeed = xspeed * -1

    if ((y > height) or (y < 0)): 
        yspeed = yspeed * -1

    background(255)  
    ellipseMode(CENTER)
    rectMode(CENTER) 

    # Draw Zoog's body
    stroke(0)
    fill(150)
    rect(x,y,w/6,h*2)

    # Draw Zoog's head
    fill(255)
    ellipse(x,y-h/2,w,h) 

    # Draw Zoog's eyes
    fill(0) 
    ellipse(x-w/3+1,y-h/2,eyeSize,eyeSize*2) 
    ellipse(x+w/3-1,y-h/2,eyeSize,eyeSize*2)

    # Draw Zoog's legs
    stroke(0)
    line(x-w/12,y+h,x-w/4,y+h+10)
    line(x+w/12,y+h,x+w/4,y+h+10)
