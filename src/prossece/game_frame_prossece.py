from re import T
from ui.game_frame_ui import GameFrameUI

import tkinter as tk

class GameFrameProcess:
    def __init__(self,master):
        self.ui = GameFrameUI(master)
        self.ui.frame.bind_all("<ButtonPress>", self.push_buttons)
        self.bomb = [[0,1,0],[0,1,0],[0,0,0]]

    def push_buttons(self,event):
        if event.widget.cget("state") != "disabled":
            text = event.widget.cget("text")
            c,a = self.bomb_check(text)
            print(c)
            event.widget.config(fg="red",state="disable",text=str(a))

    def bomb_check(self,text):
        x_min,x_max,y_min,y_max = [False,False,False,False]
        x,y = [int(d) for d in text.split()]
        N = len(self.bomb)-1
        center = self.bomb[y][x]
        around = 0

        if 0 < x:
            around += self.bomb[y][x-1]
            x_min = True
        if x < N:
            around += self.bomb[y][x+1]
            x_max = True
        if 0 < y:
            around += self.bomb[y-1][x]
            y_min = True
        if y < N:
            around += self.bomb[y+1][x]
            y_max = True
        if x_min and y_min:
            around += self.bomb[y-1][x-1]
        if x_min and y_max:
            around += self.bomb[y+1][x-1]
        if x_max and y_min:
            around += self.bomb[y-1][x+1]
        if x_max and y_max:
            around += self.bomb[y+1][x+1]
        
        return center, around