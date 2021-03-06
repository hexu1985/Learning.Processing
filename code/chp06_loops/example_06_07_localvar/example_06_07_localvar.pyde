# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 6-7: Local variables

def setup(): 
    size(480, 270)
    # x is not available! It is local to the draw() block of code.

def draw(): 
    background(0)
    x = 0
    # x is available! Since it is declared within the draw() block of code, it is available here. 
    # Notice, however, that it is not available inside draw() above where it is declared. 
    # Also, it is available inside the while block of code because while is inside of draw().
    while (x < width): 
        stroke(255)
        line(x,0,x,height)
        x += 15

def mousePressed(): 
    # x is not available! It is local to the draw( ) block of code.
    print( " The mouse was pressed! " )
