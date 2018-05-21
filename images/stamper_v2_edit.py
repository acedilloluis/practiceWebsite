'''
stamper.py uses a GUI to  create a montage from 
rotated and reduced iterations of an image. 
Rotation, reduction, and iteration are entered by slider.
Rotation direction is entered by a toggling button.
The stamp is initiated by a mouseclick.

version 1 creates the GUI window with the sliders, button, and canvas.
version 2 implements the mouse-click pasting an image
'''
from Tkinter import *    # Don't pollute namespace like this except for Tkinter
import PIL                # for most of the PIL routines
from PIL import ImageTk   # this submodule is separated from PIL

import matplotlib.pyplot as plt

import os.path              
__dir__ = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(__dir__, 'cat1-a.gif')

img = PIL.Image.open(filename)
'''
#This line isn't needed with the PNG, but is here for your use with JPGs
imga = img.convert('RGBA') # use alpha so rotate() will fill corners with a=0
'''

root = Tk() # Create main window; must be done before using ImageTk
tkimg=PIL.ImageTk.PhotoImage(img)



# A slider to set degrees per iteration
rotation = IntVar()
rotSlider = Scale(root,variable=rotation, from_=1, to=30,
                  orient=HORIZONTAL, label='Degrees:')
rotSlider.set(10)
rotSlider.grid(column=0, row=0, sticky=W)

# A slider to set the number of iterations
iteration = IntVar()
iterSlider = Scale(root,variable=iteration, from_=2, to=15,
                   orient=HORIZONTAL, label='Iterations:')
iterSlider.set(6)
iterSlider.grid(column=0, row=1, sticky=W)

# A slider to set the resizing factor for each iteration
reduction = DoubleVar()
reduceSlider = Scale(root,variable=reduction, from_=0.5, to=0.99,
                     orient=HORIZONTAL, resolution=.01, label='Reduction:')
reduceSlider.set(.95)
reduceSlider.grid(column=0, row=2, sticky=W)

# A checkbutton to toggle the direction
# A button wasn't the right widget for toggling a variable.
direction = Checkbutton(root, text='Reverse', offvalue=-1) #onvalue=1 by default
direction.grid(column=0, row=3, sticky=W)

# A canvas for mouse events and image drawing
# Maybe relief=RAISED isn't for Canvas?
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='cyan')
canvas.grid(column=1, row=0, rowspan=4, sticky=W)

# Bind a function to the left mouse button down event.
def stamp(event):
    canvas.create_image(event.x,event.y,image=tkimg)
    print reduceSlider.get()
canvas.bind('<ButtonPress-1>', stamp)

# Enter event loop
root.mainloop() 