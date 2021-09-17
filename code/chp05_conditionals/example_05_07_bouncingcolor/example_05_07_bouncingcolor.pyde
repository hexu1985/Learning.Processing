# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 5-7: "Bouncing" color

# Two variables for color.
c1 = 0.0
c2 = 255.0    

# Start by incrementing c1.
c1Change = 1.0
# Start by decrementing c2.
c2Change = -1.0

def setup(): 
    size(480, 270)

def draw(): 
    global c1
    global c2
    global c1Change
    global c2Change

    noStroke()

    # Draw rectangle on left
    fill(c1, 0, c2)
    rect(0, 0, 240, 270)

    # Draw rectangle of right
    fill(c2, 0, c1)
    rect(240, 0, 240, 270)

    # Adjust color values
    c1 = c1 + c1Change
    c2 = c2 + c2Change

    # Instead of reaching the edge of a window, 
    # these variables reach the "edge" of color:  
    # 0 for no color and 255 for full color.  
    # When this happens, just like with the 
    # bouncing ball, the change is reversed.

    # Reverse direction of color change 
    if (c1 < 0 or c1 > 255): 
        c1Change *= -1

    if (c2 < 0 or c2 > 255): 
        c2Change *= -1
