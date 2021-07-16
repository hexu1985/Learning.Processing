# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com
#
# Example 1-2: noFill
from processing_py import *

app = App(480, 270);
app.background(255);

# noFill() leaves the shape with only an outline.
app.noFill();
app.stroke(0);
app.ellipse(60, 60, 100, 100);

app.redraw();
