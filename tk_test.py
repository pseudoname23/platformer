from tkinter import *
from tkinter import ttk
import time
xV, yV = 0, 0
x, y = 0, 0


def velocityUpdate():
    if yV > 0:
        pass


class Rectangle:
    def __init__(self, parent, xPos, yPos, xPos2, yPos2):
        self.parent,self.xPos,self.yPos,self.xPos2,self.ypos2 = parent,xPos+960,-yPos+540,xPos2+960,-yPos2+540
        # Will be used for platforming soon

    def create(self):
        self.parent.create_rectangle(self.xPos, self.yPos, self.xPos2, self.ypos2,
                                     fill='#FFF000', outline='blue', tags=('rectangle', 'platform'))


class Canv(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canv(root, width=1920, height=1080)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

canvas.create_line(-20 + 960, 540, 20 + 960, 540, width=5, tags='center')
canvas.create_line(960, -20 + 540, 960, 20 + 540, width=5, tags='center')

rect = Rectangle(canvas, -100, -50, 100, 0)
rect.create()

canvas.create_rectangle(-10+960, 540, 10+960, -20+540, fill='#10fa7c', tags='player')
root.mainloop()
