from tkinter import *
from tkinter import ttk
import random


class Rectangle:
    def __init__(self, parent, xPos, yPos, length, height):
        self.position = xPos, yPos
        self.dimensions = length, height
        self.parent = parent

    def create(self, parent, xPos, yPos, length, height):
        parent.create_rectangle(xPos, yPos, xPos+length, yPos+height, fill='#FFF000', outline='blue')


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Sketchpad(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

rect = Rectangle(canvas, 10, 10, 80, 50)
rect.create(canvas, 10, 10, 80, 50)

root.mainloop()
