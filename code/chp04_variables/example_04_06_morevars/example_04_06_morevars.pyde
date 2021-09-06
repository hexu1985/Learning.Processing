# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 4-6: Ellipse with variables

# Declare and initialize your variables!
r = 100.0
g = 150.0
b = 200.0
a = 200.0

diam = 20.0
x = 100.0
y = 100.0

def setup():
    size(480, 270)
    background(255)

def draw(): 
    # Use those variables to draw an ellipse
    stroke(0)
    # (Remember, the fourth argument for a color is transparency.
    fill(r, g, b, a)
    ellipse(x, y, diam, diam)
