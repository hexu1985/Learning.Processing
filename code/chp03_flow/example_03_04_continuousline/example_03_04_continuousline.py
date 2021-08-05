# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 3-4: Drawing a continuous line

from processing_py import *

app = App(480, 270);
app.background(255);

while True:
    app.stroke(0);

    # Draw a line from previous mouse location to current mouse location.
    app.line(app.pmouseX, app.pmouseY, app.mouseX, app.mouseY);

    app.redraw();
