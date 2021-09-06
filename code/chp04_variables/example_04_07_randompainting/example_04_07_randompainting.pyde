# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 4-7: Filling variables with random values

r = 0.0
g = 0.0
b = 0.0
a = 0.0

diam = 0.0
x = 0.0
y = 0.0

def setup(): 
    size(480, 270)
    background(255)

def draw(): 
    global r
    global g
    global b
    global a

    global diam
    global x
    global y

    # Each time through draw(), new random 
    # numbers are picked for a new ellipse.
    r = random(255)
    g = random(255)
    b = random(255)
    a = random(255)
    diam = random(20)
    x = random(width)
    y = random(height)

    # Use values to draw an ellipse
    noStroke()
    fill(r, g, b, a)
    ellipse(x, y, diam, diam)
