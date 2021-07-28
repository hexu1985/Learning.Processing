# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 3-2: mouseX and mouseY

from processing_py import *

app = App(480, 270);

while True:
  # Try moving background() to setup() and see the difference!
  app.background(255);

  # Body
  app.stroke(0);
  app.fill(175);
  app.rectMode(CENTER);

  # mouseX is a keyword that the sketch replaces with the horizontal position of the mouse.
  # mouseY is a keyword that the sketch replaces with the vertical position of the mouse.
  app.rect(app.mouseX, app.mouseY, 50, 50);

  app.redraw();
