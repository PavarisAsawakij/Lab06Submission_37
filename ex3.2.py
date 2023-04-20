import sys
import pygame as pg
import string

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
state = False

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0,c1=0,c2=0,c3=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
    def draw(self,screen):
        pg.draw.rect(screen,(self.c1,self.c2,self.c3),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,c1=0,c2=0,c3=0):
        Rectangle.__init__(self, x, y, w, h,c1,c2,c3)
        # self.x = x
        # self.y = y
        # self.w = w
        # self.h = h
        # self.c1 = c1
        # self.c2 = c2
        # self.c3 = c3
    def isMouseOn(self):
        if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[0] <= self.w+self.x:
            if pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[1] <= self.h+self.y:
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
        
class InputBox:

    def __init__(self,mode, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.mode = mode
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.mode == 'text' and event.unicode in string.ascii_letters or event.unicode == ' ':
                    self.text += event.unicode
                elif self.mode == 'number' and event.unicode.isnumeric():
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

FirstName_font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
FirstName_text = FONT.render('Name', True, (COLOR_ACTIVE), (255,255,255)) # (text,is smooth?,letter color,background color)
FirstName_textRect = FirstName_text.get_rect() # text size
FirstName_textRect.topleft = (100,70)

LastName_font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
LastName_text = FONT.render('Last Name', True, (COLOR_ACTIVE), (255,255,255)) # (text,is smooth?,letter color,background color)
LastName_textRect = LastName_text.get_rect() # text size
LastName_textRect.topleft = (100,170)

Age_font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
Age_text = FONT.render('Age', True, (COLOR_ACTIVE), (255,255,255)) # (text,is smooth?,letter color,background color)
Age_textRect = Age_text.get_rect() # text size
Age_textRect.topleft = (100,270)

input_box1 = InputBox('text',100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox('text',100, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBox('number',100, 300, 140, 32)

submit = Button((win_x//2)-50 , 400 ,100, 50,175,240,130)
submit_font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
submit_text = FONT.render('Submit', True, (COLOR_ACTIVE), (175,240,130)) # (text,is smooth?,letter color,background color)
submit_textRect = submit_text.get_rect() # text size
submit_textRect.center = (win_x//2,425)


Answer_font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
Answer_text = FONT.render(f'Hello {input_box1.text} {input_box2.text}! You are {input_box3.text} years old.', True, (COLOR_ACTIVE), (255,255,255)) # (text,is smooth?,letter color,background color)
Answer_textRect = Answer_text.get_rect() # text size
Answer_textRect.center = (win_x//2 , 270)

input_boxes = [input_box1, input_box2,input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(FirstName_text,FirstName_textRect)
    screen.blit(LastName_text,LastName_textRect)
    screen.blit(Age_text,Age_textRect)
    submit.draw(screen)
    screen.blit(submit_text,submit_textRect)
    Answer_text = FONT.render(f'Hello {input_box1.text} {input_box2.text}! You are {input_box3.text} years old.', True, (COLOR_ACTIVE), (255,255,255)) # (text,is smooth?,letter color,background color)


    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    if submit.isMouseClick():
        state = True
    if state == True:
        screen.blit(Answer_text,Answer_textRect)

    
    pg.time.delay(1)
    pg.display.update()

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
