# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com
#
# Example 1-1: stroke and fill
from processing_py import *

app = App(480, 270);
app.background(255);
app.stroke(0); 
app.fill(150);
app.rect(50, 50, 75, 100);
app.redraw();