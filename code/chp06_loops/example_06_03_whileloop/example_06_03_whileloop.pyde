# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 6-3: While loop

size(200, 200)
background(255)

y = 80       # Vertical location of each line
x = 50       # Initial horizontal location for first line
spacing = 10 # How far apart is each line
len = 20     # Length of each line

# A variable to mark where the legs end.
endLegs = 150 
stroke(0)

# Draw each leg inside a while loop.
while (x <= endLegs): 
    line (x, y, x, y + len)
    x = x + spacing
