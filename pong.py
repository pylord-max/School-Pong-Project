#importing required modules
from tkinter import *
import time
import random

#making main window and canvas
tk=Tk()
tk.title('Pong!')
#preventing users from resizing as most of our code is based on position
tk.resizable(0,0)
#making our window show above others
tk.wm_attributes('-topmost',1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg='black')
canvas.pack()
tk.update()

#making the middle line using canvas.create_line(x1,y1,x2,y2.fill='color')
canvas.create_line(250,0,250,400,fill='white')

counter=0
counter2=0


class Ball:


    
    def __init__(self,canvas,color,paddle,paddle2):
        self.canvas=canvas
        self.paddle=paddle
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,233,185)
        starts=[-3,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        



    def draw(self):

        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
            self.score(True)
        if pos[2]>=self.canvas_width:
            self.x=-3
            self.score(False)
        if self.hit_paddle(pos)==True:
            self.x=3
        if self.hit_paddle2(pos)==True:
            self.x=-3
            





    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False



        
    def hit_paddle2(self,pos):
        paddle_pos=self.canvas.coords(self.paddle2.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[2]>=paddle_pos[0] and pos[2]<=paddle_pos[2]:
                return True
            return False






    def score(self,val):
        global counter
        global counter2


        if val==True:
            a=self.canvas.create_text(125,40,text=counter,font=("Arial",60),fill='white')
            canvas.itemconfig(a,fill='black')
            counter+=1
            a=self.canvas.create_text(125,40,text=counter,font=("Arial",60),fill='white')


            
        if val==False:
             
             a=self.canvas.create_text(375,40,text=counter2,font=("Arial",60),fill='white')
             canvas.itemconfig(a,fill='black')
             counter2+=1
             a=self.canvas.create_text(375,40,text=counter2,font=("Arial",60),fill='white')
            




        

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,30,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('a',self.turn_left)
        self.canvas.bind_all('d',self.turn_right)




    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0

    def turn_left(self,evt):
        self.y=-3

    def turn_right(self,evt):
        self.y=3

    
        




class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(470,150,500,250,fill=color)
        self.y=0
        self.canvas_height=400
        self.canvas_width=500
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)


    def draw(self):
            self.canvas.move(self.id,0,self.y)
            pos=self.canvas.coords(self.id)
            if pos[1]<=0:
                self.y=0
            if pos[3]>=400:
                self.y=0



    def turn_left(self,evt):
            self.y=3

    def turn_right(self,evt):
            self.y=-3
            
paddle=Paddle(canvas,'blue')
paddle2=Paddle2(canvas,'pink')
ball=Ball(canvas,'orange',paddle,paddle2)


while 1:
    ball.draw()
    paddle.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if counter==10:
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle2.y=0
        canvas.create_text(250,200,text='congrats player1! you won!!',font=32,fill='red')
        canvas.create_text(250,215,text='score is '+str(counter2) + '-' + str(counter),font=32,fill='red')

    if counter2==10:
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle2.y=0
        canvas.create_text(250,200,text='congrats player2! you won!!',font=32,fill='red')
        canvas.create_text(250,215,text='score is '+str(counter2) + '-' +str(counter),font=32,fill='red')

    if counter==10 or counter2==10:
        break

    



    


root.mainloop()
