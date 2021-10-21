# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 6-6: Legs with a for loop

size(480, 270)
background(255)

y = 80       # Vertical location of each line
spacing = 10 # How far apart is each line
len = 20     # Length of each line

# Translation of the legs while loop to a for loop.
for x in range(50, 150+1, spacing):
    line(x, y, x, y + len)
