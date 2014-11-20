from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=700, background='white')
sq1 = drawpad.create_rectangle(0,0,100,100)
sq2 = drawpad.create_rectangle(100,0,200,100)
sq3 = drawpad.create_rectangle(200,0,300,100)
sq4 = drawpad.create_rectangle(300,0,400,100)
sq5 = drawpad.create_rectangle(400,0,500,100)
sq6 = drawpad.create_rectangle(500,0,600,100)
sq7 = drawpad.create_rectangle(600,0,700,100)
sq8 = drawpad.create_rectangle(700,0,800,100)
sq9 = drawpad.create_rectangle(700,100,800,200)
sq10 = drawpad.create_rectangle(700,200,800,300)
sq11 = drawpad.create_rectangle(600,200,700,300)
sq12 = drawpad.create_rectangle(500,200,600,300)
sq13 = drawpad.create_rectangle(400,200,500,300)
sq14 = drawpad.create_rectangle(300,200,400,300)
sq15 = drawpad.create_rectangle(200,200,300,300)
sq16 = drawpad.create_rectangle(100,200,200,300)
sq17 = drawpad.create_rectangle(0,200,100,300)
sq18 = drawpad.create_rectangle(0,300,100,400)
sq19 = drawpad.create_rectangle(0,400,100,500)
sq20 = drawpad.create_rectangle(100,400,200,500)
sq21 = drawpad.create_rectangle(200,400,300,500)
sq22 = drawpad.create_rectangle(300,400,400,500)
sq23 = drawpad.create_rectangle(400,400,500,500)
sq24 = drawpad.create_rectangle(500,400,600,500)
sq25 = drawpad.create_rectangle(600,400,700,500)
sq26 = drawpad.create_rectangle(700,400,800,500)
sq27 = drawpad.create_rectangle(700,500,800,600)
sq28 = drawpad.create_rectangle(700,600,800,700)
sq29 = drawpad.create_rectangle(600,600,700,700)
sq30 = drawpad.create_rectangle(500,600,600,700)
sq31 = drawpad.create_rectangle(400,600,500,700)
sq32 = drawpad.create_rectangle(300,600,400,700)
sq33 = drawpad.create_rectangle(200,600,300,700)
sq34 = drawpad.create_rectangle(100,600,200,700)
sq35 = drawpad.create_rectangle(0,600,100,700)
player = drawpad.create_oval(35,35,65,65, fill="red")

class MyApp:
    def __init__(self,parent):
        global drawpad
        self.myParent = parent  
       	self.myContainer1 = Frame(parent)
       	self.myContainer1.pack()
       	drawpad.pack(side=RIGHT)
       
    def animate(self):
        global player
        global drawpad
        
        x1,y1,x2,y2 = drawpad.coords(player)
        if x1 == 35 and y1 == 35 and x2 == 35 and y2 == 35 and raw_input() == f:
            drawpad.move(player,100,0)
        drawpad.after(1,animate())




app = MyApp(root)
root.mainloop()