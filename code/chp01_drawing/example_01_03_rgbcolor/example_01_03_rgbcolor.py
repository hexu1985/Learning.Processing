# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 1-3: RGB Color
from processing_py import *

app = App(480, 270);
app.background(255);
app.noStroke();

# Bright red
app.fill(255, 0, 0);
app.ellipse(20, 20, 16, 16);

# Dark red
app.fill(127, 0, 0);
app.ellipse(40, 20, 16, 16);

# Pink (pale red)
app.fill(255, 200, 200);
app.ellipse(60, 20, 16, 16);

app.redraw();
