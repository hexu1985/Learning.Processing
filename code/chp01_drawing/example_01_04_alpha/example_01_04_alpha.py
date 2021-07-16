# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 1-4: Alpha Transparency
from processing_py import *

app = App(480, 270);
app.background(0);
app.noStroke();

# No fourth argument means 100% opacity.
app.fill(0, 0, 255);
app.rect(0, 0, 240, 200);

# 255 means 100% opacity.
app.fill(255, 0, 0, 255);
app.rect(0, 0, 480, 40);

# 75% opacity.
app.fill(255, 0, 0, 191);
app.rect(0, 50, 480, 40);

# 55% opacity.
app.fill(255, 0, 0, 127);
app.rect(0, 100, 480, 40);

# 25% opacity.
app.fill(255, 0, 0, 63);
app.rect(0, 150, 480, 40);

app.redraw();
