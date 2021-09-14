from tkinter import *
from tkinter import ttk


class Rectangle:
    def __init__(self, parent, xPos, yPos, length, height):
        self.parent, self.xPos, self.yPos, self.length, self.height = parent, xPos, yPos, length, height
        # Will be used for platforming soon
    def create(self):
        self.parent.create_rectangle(self.xPos, self.yPos, self.xPos + self.length, self.yPos + self.height,
                                     fill='#FFF000', outline='blue', tags=('rectangle', 'platform'))


class cnv(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = cnv(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

rect = Rectangle(canvas, 10, 10, 80, 50)
rect.create()

root.mainloop()
