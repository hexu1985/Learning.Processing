# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com
from processing_py import *

app = App(200, 200);
# Exercise 1-1: Looking at how we wrote the instruction for line "line(1,0,4,5);" 

# How would you guess you would write an instruction to draw a rectangle? 
app.rect(50,25,75,25);

# A circle? 
app.ellipse(150,75,25,25);

# A triangle? 
app.triangle(50,150,50,175,100,135);

app.redraw();
