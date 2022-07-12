import os
import sys
import time
import tkinter
from tkinter import *
from tkinter import ttk
from threading import Thread

# Example..
# animate(500, 250, 'animation-directory')
# copy all below to script for use..

def animate(xpos, ypos, xvar):

	xpos = int(xpos)
	ypos = int(ypos)

	files = next(os.walk(f'img/{xvar}'))[2]
	count = int(len(files))

	frame = PhotoImage(file=f'img/{xvar}/1.png')
	ximg = world.create_image(xpos, ypos, image=frame, anchor=CENTER)

	for i in range(1, count+1):

		time.sleep(0.01)
		yvar = str(f'img/{xvar}/'+str(i)+'.png')
		frame = PhotoImage(file=yvar)
		world.itemconfig(ximg, image=frame)
		world.update()