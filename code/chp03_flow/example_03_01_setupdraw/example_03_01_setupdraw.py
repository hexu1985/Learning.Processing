# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 3-1: Zoog as dynamic sketch

# setup() runs first one time.  
# size() should always be first line of setup

from processing_py import *


# Set the size of the window
app = App(480, 270);

# draw() loops continuously until you close the sketch window.
while True:
    # Draw a white background
    app.background(255);   

    # Set CENTER mode
    app.ellipseMode(CENTER);
    app.rectMode(CENTER); 

    # Body
    app.stroke(0);
    app.fill(150);
    app.rect(240, 145, 20, 100);

    # Head
    app.fill(255);
    app.ellipse(240, 115, 60, 60); 

    # Eyes
    app.fill(0); 
    app.ellipse(221, 115, 16, 32); 
    app.ellipse(259, 115, 16, 32);

    # Legs
    app.stroke(0);
    app.line(230, 195, 220, 205);
    app.line(250, 195, 260, 205);

    app.redraw();

