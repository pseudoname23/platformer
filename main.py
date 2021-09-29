from tkinter import *
from tkinter import ttk
import time
x,y,xV,yV = 0,0,0,10
TPS = 120
tCount = 0

objBounds = {}


class Solid:
    def __init__(self, parent, xPos, yPos, xPos2, yPos2):
        global objBounds
        self.parent,self.xPos,self.yPos,self.xPos2,self.yPos2 = parent,xPos+960,-yPos+540,xPos2+960,-yPos2+540
        self.bounds = self.xPos, self.xPos2
        self.id = -1

    def create(self):
        self.id = self.parent.create_rectangle(self.xPos, self.yPos, self.xPos2, self.yPos2,
                                               fill='#FFF000', outline='blue', tags=('rectangle', 'platform'))
        objBounds[self.id] = self.parent.coords(self.id)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, width=1920, height=1080)  # 0
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

canvas.create_line(-20 + 960, 540, 20 + 960, 540, width=5, tags='center')  # 1
canvas.create_line(960, -20 + 540, 960, 20 + 540, width=5, tags='center')  # 2

rect = Solid(canvas, -100, -50, 100, 0)  # 3
rect.create()

plr = canvas.create_rectangle(950, 530, 970, 510, fill='#000000', tags='player')  # 4


def gravitate():
    global y, yV
    y += yV
    yV -= 64/TPS


touching, xAligned, yAligned = False, False, False
def detectCollision(bounds, player):
    global touching, xAligned, yAligned, canvas
    coords = canvas.coords(player)
    for v in bounds.values():
        if xAligned: continue
        elif v[0] < coords[0] and v[2] > coords[0]: xAligned = True
        elif v[0] < coords[2] and v[2] > coords[2]: xAligned = True
        else: xAligned = False
        if yAligned: continue
        elif v[1] > coords[1] and v[3] < coords[1]: yAligned = True
        elif v[1] > coords[3] and v[3] < coords[3]: yAligned = True
        else: yAligned = False
        if xAligned and yAligned: touching = True


def jump(n):  # For some reason the code breaks if i don't include an argument
    global yV, y, touching, xAligned, yAligned
    while 1:
        if not touching:
            canvas.move(4, 0, -yV)
            gravitate()
            detectCollision(objBounds, plr)
            Tk.update(root)
            time.sleep(1/TPS)
        print(xAligned, yAligned, touching)
        if touching: break


canvas.bind('<ButtonPress-1>', jump)
root.mainloop()
