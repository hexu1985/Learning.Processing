# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 5-9: Simple Gravity

x = 240.0   # x location of square
y = 0.0     # y location of square

speed = 0.0   # speed of square

# A new variable, for gravity (i.e. acceleration).   
# We use a relatively small number (0.1) because this accelerations accumulates over time, increasing the speed.   
# Try changing this number to 2.0 and see what happens.
gravity = 0.1  

def setup(): 
    size(480, 270)

def draw(): 
    global x
    global y
    global speed
    global gravity
    
    background(255)

    # Display the square
    fill(175)
    stroke(0)
    rectMode(CENTER)
    rect(x, y, 10, 10)

    # Add speed to location.
    y = y + speed

    # Add gravity to speed.
    speed = speed + gravity

    # If square reaches the bottom
    # Reverse speed
    if (y > height): 
        # Multiplying by -0.95 instead of -1 slows the square down each time it bounces (by decreasing speed).  
        # This is known as a "dampening" effect and is a more realistic simulation of the real world (without it, a ball would bounce forever).
        speed = speed * -0.95
        y = height #<>#
