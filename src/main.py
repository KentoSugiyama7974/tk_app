from telnetlib import GA
from prossece.game_frame_prossece import GameFrameProcess

import tkinter as tk

class Main:
    def __init__(self, master):
        self.game_frame = GameFrameProcess(master)

if __name__ == "__main__":
    master = tk.Tk()
    Main(master)
    master.resizable(width=False, height=False)
    master.mainloop()