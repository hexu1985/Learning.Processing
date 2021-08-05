# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 3-5: mousePressed and keyPressed
def setup():
    size(480, 270)
    background(255)

def draw():
    # Nothing happens in draw() in this example!
    pass
    

# Whenever a user clicks the mouse the code written inside mousePressed() is executed.
def mousePressed(): 
    stroke(0)
    fill(175)
    rectMode(CENTER)
    rect(mouseX, mouseY, 16, 16)

# Whenever a user presses a key the code written inside keyPressed() is executed.
def keyPressed(): 
    background(255)
