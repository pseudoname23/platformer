from tkinter import *
from tkinter import ttk
import time
x,y,xV,yV = 0,0,0,10
TPS = 60
tCount = 0


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

canvas = Canv(root, width=1920, height=1080)  # 0
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

canvas.create_line(-20 + 960, 540, 20 + 960, 540, width=5, tags='center')  # 1
canvas.create_line(960, -20 + 540, 960, 20 + 540, width=5, tags='center')  # 2

rect = Rectangle(canvas, -100, -50, 100, 0)  # 3
rect.create()

plr = canvas.create_rectangle(950, 540, 970, 520, fill='#000000', tags='player')  # 4


def tick():
    global y, yV, tCount, TPS
    if y >= 0:
        y += yV
        yV -= 64/TPS
        tCount += 1
        time.sleep(1/TPS)
    else:
        y = 0
        yV = 0


def jump(n):  # For some reason the code breaks if i don't include an argument
    global yV, y
    while True:
        canvas.move(4, 0, -yV)
        tick()
        Tk.update(root)
        if y < 5:
            y = 10
            break


canvas.bind('<ButtonPress-1>', jump)
root.mainloop()
