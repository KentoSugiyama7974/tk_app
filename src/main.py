from prossece.game_frame_prossece import GameFrameProcess

import tkinter as tk

class Main:
    def __init__(self, master):
        master.iconphoto(False, tk.PhotoImage(file="./graphics/kunio.png"))
        self.game_frame = GameFrameProcess(master,3,1)

if __name__ == "__main__":
    master = tk.Tk()
    Main(master)
    master.resizable(width=False, height=False)
    master.mainloop()