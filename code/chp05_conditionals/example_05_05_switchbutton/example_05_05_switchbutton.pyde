# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 5-5: Button as switch
button = False

x = 50
y = 50
w = 100
h = 75

def setup(): 
    size(480, 270)

def draw(): 
    if (button): 
        background(255)
        stroke(0)
    else: 
        background(0)
        stroke(255)

    fill(175)
    rect(x, y, w, h)

# When the mouse is pressed, the state of the button is toggled.   
# Try moving this code to draw() like in the rollover example.  
# What goes wrong?
def mousePressed(): 
    global button
    if (mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h): 
        button = not button
