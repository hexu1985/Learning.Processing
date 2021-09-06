# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 4-3: Varying variables

# Declare and initialize two integer variables at the top of the code.
circleX = 0
circleY = 100

def setup():
    size(480, 270)

def draw(): 
    global circleX
    background(255)
    stroke(0)
    fill(175)
    # Use the variables to specify the location of an ellipse.
    ellipse(circleX, circleY, 50, 50)

    # An assignment operation that increments the value of circleX by 1.
    circleX = circleX + 1
