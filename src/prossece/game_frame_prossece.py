from ui.game_frame_ui import GameFrameUI

import tkinter as tk
from tkinter import messagebox
import random

class GameFrameProcess:
    def __init__(self,master,size=3, bomb_num=2):
        self.master = master
        self.ui = GameFrameUI(master,size)
        self.ui.frame.bind_all("<1>", self.push_buttons)
        self.set_bomb(size,bomb_num)
        self.coordinate = set()

    def set_bomb(self,size,bomb_num):
        self.bomb = [[0 for i in range(size)] for j in range(size)]
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        for _ in range(bomb_num):
            while self.bomb[y][x] == 1:
                x = random.randint(0,size-1)
                y = random.randint(0,size-1)
            self.bomb[y][x] = 1
        print(self.bomb)

    def push_buttons(self,event):
        if event.widget.cget("state") != "disabled":
            text = str(event.widget.winfo_name())
            x,y = [int(d) for d in text.split()]
            self.bomb_check(x,y)

    def change_text(self,x,y,a):
        button = self.master.nametowidget("frame."+str(x)+" "+str(y))
        button.config(state="disable", text=str(a))
    
    def bomb_check(self,x,y):
        if 1 == self.bomb[y][x]:
            messagebox.showinfo('bomb!','あなたの負けです')
        else:
            around, coordinate = self.around_check(x,y)
            self.change_text(x,y,around)
            self.coordinate = self.coordinate | set([(x,y)])
            if 0 == around:
                coordinate = coordinate - self.coordinate
                for _x,_y in coordinate:
                    self.bomb_check(_x,_y)
                self.coordinate = self.coordinate | coordinate
            

    def around_check(self,x,y):
        x_min,x_max,y_min,y_max = [False,False,False,False]
        N = len(self.bomb)-1
        around = 0
        coordinate = list()
        if 0 < x:
            around += self.bomb[y][x-1]
            x_min = True
            coordinate.append((x-1,y))

        if x < N:
            around += self.bomb[y][x+1]
            x_max = True
            coordinate.append((x+1,y))

        if 0 < y:
            around += self.bomb[y-1][x]
            y_min = True
            coordinate.append((x,y-1))

        if y < N:
            around += self.bomb[y+1][x]
            y_max = True
            coordinate.append((x,y+1))

        if x_min and y_min:
            around += self.bomb[y-1][x-1]
            coordinate.append((x-1,y-1))

        if x_min and y_max:
            around += self.bomb[y+1][x-1]
            coordinate.append((x-1,y+1))

        if x_max and y_min:
            around += self.bomb[y-1][x+1]
            coordinate.append((x+1,y-1))

        if x_max and y_max:
            around += self.bomb[y+1][x+1]
            coordinate.append((x+1,y+1))

        return around, set(coordinate)