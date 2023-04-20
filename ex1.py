import sys 
import pygame as pg

class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0,c1=0,c2=0,c3=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.c1 = c1
        self.c2 = c2
        self.c3 = c2
    def draw(self,screen):
        pg.draw.rect(screen,(self.c1,self.c2,self.c3),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,c1=0,c2=0,c3=0):
        Rectangle.__init__(self, x, y, w, h,c1,c2,c3)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c1 = c1
        self.c2 = c2
        self.c3 = c2
    def isMouseOn(self):
        if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[0] <= self.w+self.x:
            if pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[1] <= self.h+self.y:
                # print ("check")
                return True
        else:
            return False
    def isMouseClick(self):
        if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[0] <= self.w+self.x:
            if pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[1] <= self.h+self.y:
                if pg.mouse.get_pressed() == (1,0,0):
                    return True
        else:
            return False

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,254,87,87) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)

    if btn.isMouseOn  and btn.isMouseClick():
        btn.c1 = 165
        btn.c2 = 48
        btn.c3 = 186

    elif btn.isMouseOn():
        btn.c1 = 190
        btn.c2 = 190
        btn.c3 = 190
    else:
        btn.c1 = 254
        btn.c2 = 87
        btn.c3 = 87
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False