from tkinter import *
from random import randrange
# from PIL import Image, ImageTk

class Kinder:
    def __init__(self,can):
        self.id = []
        self.x = 50
        self.can = can
        self.y = 50
        self.man = None
        self.draw_man()
        self.speed = 5
    def draw_bag(self,x,y):
        num = 40
        num2 = num//12
        b1=self.can.create_rectangle(x,y,x+num,y+num,fill='white')
        b2=self.can.create_polygon(x+num/2-num2,y,x+num/2-num2,y+num/2-num2,x,y+num/2-num2, 
                           x,y+num/2+num2,x+num/2-num2,y+num/2+num2,x+num/2-num2,y+num,
                           x+num/2+num2,y+num,x+num/2+num2,y+num/2+num2,x+num,y+num/2+num2,
                           x+num,y+num/2-num2,x+num/2+num2,y+num/2-num2,x+num/2+num2,y,
                           x+num/2, y,x+2*num/3,y-num//4,x+num,y-num//4,
                           x+num/2, y, x+num/3, y-num//4, x, y-num//4,
                           x+num/2, y,fill='red',outline='purple')
        # b2=self.can.create_polygon(x+25,y,x+25,y+25,x,y+25, 
        #                    x,y+35,x+25,y+35,x+25,y+60,
        #                    x+35,y+60,x+35,y+35,x+60,y+35,
        #                    x+60,y+25,x+35,y+25,x+35,y,
        #                    x+30, y,x+40,y-15,x+60,y-15,
        #                    x+30, y, x+20, y-15, x, y-15,
        #                    x+30, y,fill='red',outline='purple')
        self.id.append([x,y,b1,b2])
    def draw_man(self):
        # pil_image = Image.open('pakman.png')
        # image = ImageTk.PhotoImage(pil_image)
        # self.man = self.can.create_image(30,30,image = image)
        # python_image = PhotoImage(file="pakman.png")
 
        # self.can.create_image(10, 10, image=python_image)
        self.man = self.can.create_arc(30,30,90,90,start=300,extent=310,fill='yellow')
    def move(self,event):
        x1,y1,x2,y2 = self.can.coords(self.man)
        if event.keysym == 'Down':
            self.can.delete(self.man)
            self.man = self.can.create_arc(x1,y1,x2,y2,start=300,extent=310,fill='yellow')
            self.can.move(self.man,0,self.speed)
        elif event.keysym == 'Up':
            self.can.delete(self.man)
            self.man = self.can.create_arc(x1,y1,x2,y2,start=120,extent=310,fill='yellow')
            self.can.move(self.man,0,-self.speed)
        elif event.keysym == 'Left':
            self.can.delete(self.man)
            self.man = self.can.create_arc(x1,y1,x2,y2,start=200,extent=310,fill='yellow')
            self.can.move(self.man,-self.speed,0)
        elif event.keysym == 'Right':
            self.can.delete(self.man)
            self.man = self.can.create_arc(x1,y1,x2,y2,start=20,extent=310,fill='yellow')
            self.can.move(self.man,self.speed,0)
        x,y,x1,y1 = self.can.coords(self.man)
        for bag in self.id:
            if bag[0]+60>=x >= bag[0] and bag[1]+60>=y>=bag[1] :
                self.can.delete(bag[2])
                self.can.delete(bag[3])
                self.id.remove(bag)
                
            if (bag[0]+60>=x1 >=bag[0] and bag[1]+60>=y1>=bag[1]):
                self.can.delete(bag[2])
                self.can.delete(bag[3])
                self.id.remove(bag)
        if len(self.id) == 0 :
            self.can.create_text(450,350,text='Игра окончена!', font=('Algerian',50))        
                
root = Tk()
root.geometry('1000x800')
root.title('Собиралка')

can = Canvas(root,width=1000, height=800,bg='LightBlue')

sp = Kinder(can)

for x in range(3):
    for y in range(3):
        if x==0 and y==0:
            continue
        sp.draw_bag(x*310+randrange(0,320),y*240+randrange(0,230))
#print(sp.id)
can.pack()
root.bind_all('<KeyPress>',sp.move)
    
root.mainloop()