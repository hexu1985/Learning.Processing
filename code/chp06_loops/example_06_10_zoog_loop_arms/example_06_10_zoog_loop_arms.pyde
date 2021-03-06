# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 6-10: Zoog with arms

x = 100
y = 100
w = 60
h = 60
eyeSize = 16
speed = 1

def setup(): 
    size(480, 270)

def draw(): 
    global x
    global y
    global w
    global h
    global eyeSize
    global speed

    # Change the x location of Zoog by speed
    x = x + speed

    # If we've reached an edge, reverse speed (i.e. multiply it by -1)
    #(Note if speed is a + number, square moves to the right,- to the left)
    if ((x > width) or (x < 0)): 
        speed = speed * -1

    background(255) # Draw a white background

    # Set ellipses and rects to CENTER mode
    ellipseMode(CENTER)
    rectMode(CENTER)

    # Arms are incorporated into Zoog's design with a for loop. 
    i = y + 5
    while (i < y + h):
        stroke(0)
        line(x-w/3,i,x + w/3,i)
        i += 10
    
    # Draw Zoog's body
    stroke(0)
    fill(175)
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
    line(x-w/12,y + h,x-w/4,y + h + 10)
    line(x+w/12,y + h,x + w/4,y + h + 10)
