# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 5-4: Hold down the button
button = False

x = 50
y = 50
w = 100
h = 75

def setup(): 
    size(480, 270) 

def draw(): 
    # The button is pressed if (mouseX,mouseY) is inside the rectangle and mousePressed is true.
    if (mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h and mousePressed):
        button = True 
    else: 
        button = False

    if (button): 
        background(255)
        stroke(0)
    else: 
        background(0)
        stroke(255)

    fill(175)
    rect(x,y,w,h)






