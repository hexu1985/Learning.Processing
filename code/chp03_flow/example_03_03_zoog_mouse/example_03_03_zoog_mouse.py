# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 3-3: Zoog as dynamic sketch with variation

from processing_py import *

app = App(480, 270)     # Set the size of the window

while True:
    app.background(255);  # Draw a white background 

    # Set ellipses and rects to CENTER mode
    app.ellipseMode(CENTER);
    app.rectMode(CENTER); 

    # Draw Zoog's body
    app.stroke(0);
    app.fill(175);
    # Zoog's body is drawn at the location (mouseX, mouseY).
    app.rect(app.mouseX, app.mouseY, 20, 100);

    # Draw Zoog's head
    app.stroke(0);
    app.fill(255);
    # Zoog's head is drawn above the body at the location (mouseX, mouseY - 30).
    app.ellipse(app.mouseX, app.mouseY-30, 60, 60); 

    # Eyes
    app.fill(0); 
    app.ellipse(221, 115, 16, 32); 
    app.ellipse(259, 115, 16, 32);

    # Legs
    app.stroke(0);
    app.line(230, 195, 220, 205);
    app.line(250, 195, 260, 205);

    app.redraw();
