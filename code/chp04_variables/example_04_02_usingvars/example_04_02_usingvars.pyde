# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 4-2: Using variables

# Declare and initialize two integer variables at the top of the code.
circleX = 100
circleY = 100

def setup(): 
    size(480, 270)

def draw(): 
    background(255)
    stroke(0)
    fill(175)
    # Use the variables to specify the location of an ellipse.
    ellipse(circleX, circleY, 50, 50)
