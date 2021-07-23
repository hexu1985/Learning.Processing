# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com
#
# Exercise 1-4: Try to guess what the instructions 
# would be for the following screenshot.
from processing_py import *

app = App(200, 200);
app.background(255);
app.stroke(0);
app.fill(0);
app.rect(0,0,100,100);
app.fill(150);
app.rect(100,100,100,100);
app.redraw();
