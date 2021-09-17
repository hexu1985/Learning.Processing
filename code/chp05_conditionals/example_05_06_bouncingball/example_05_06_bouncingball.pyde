# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 5-6: Bouncing Ball
x = 0
speed = 2

def setup(): 
    size(480, 270)

def draw(): 
    global x
    global speed

    background(255)

    # Add the current speed to the x location.
    x = x + speed

    # Remember, || means "or."
    if ((x > width) or (x < 0)): 
        # If the object reaches either edge, 
        # multiply speed by -1 to turn it around.
        speed = speed * -1

    # Display circle at x location
    stroke(0)
    fill(175)
    ellipse(x, 100, 32, 32)
