# Learning Processing
# Daniel Shiffman
# http://www.learningprocessing.com

# Example 1-5: Zoog
from processing_py import *

app = App(480, 270);
app.background(255);
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
