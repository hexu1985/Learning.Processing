# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 3-4: Drawing a continuous line
def setup():
    size(480, 270)
    background(255)

def draw():
    stroke(0)

    # Draw a line from previous mouse location to current mouse location.
    line(pmouseX, pmouseY, mouseX, mouseY)
