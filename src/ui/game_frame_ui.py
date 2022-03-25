import tkinter as tk

class GameFrameUI:
    def __init__(self,master):
        self.master = master
        self.create_frame()
        self.create_buttons()

    def create_frame(self):
        self.frame = tk.Frame(
            self.master,
            width=300,
            height=300,
        )
        self.frame.pack()

    def create_buttons(self,N=3):
        for y in range(N):
            for x in range(N):
                buttons = tk.Button(
                    self.frame,
                    width=10,
                    height=10,
                    text=str(x)+" "+str(y),
                    fg="SystemButtonFace",
                    font=("",20)
                )
                buttons.grid(column=x, row=y)
        
if __name__ == "__main__":
    master = tk.Tk()
    GameFrameUI(master)
    master.mainloop()