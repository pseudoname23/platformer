from tkinter import *
from tkinter import ttk
import time
xV, yV = 0, 0
x, y = 0, 0


def updateP():
    global x, y, xV, yV
    x += xV
    y += yV


class Player:
    def __init__(self, parent, xPos, yPos, color):
        self.parent, self.x, self.y, self.color = parent, xPos, yPos, color

    def create(self):
        self.parent.create_rectangle(self.x+950, self.y+540, self.x+970, self.y+520, fill=self.color, tags='player')


class Rectangle:
    def __init__(self, parent, xPos, yPos, xPos2, yPos2):
        self.parent,self.xPos,self.yPos,self.xPos2,self.yPos2 = parent,xPos+960,-yPos+540,xPos2+960,-yPos2+540
        self.xBounds = self.xPos, self.xPos2
        self.yBounds = self.yPos, self.yPos2

    def create(self):
        self.parent.create_rectangle(self.xPos, self.yPos, self.xPos2, self.yPos2,
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

plr = Player(canvas, 0, 0, '#000000')
plr.create()
root.mainloop()
