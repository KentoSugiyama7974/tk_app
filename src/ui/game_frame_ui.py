import tkinter as tk

class GameFrameUI:
    def __init__(self,master,N):
        self.master = master
        self.create_frame()
        self.create_buttons(N)

    def create_frame(self):
        self.frame = tk.Frame(
            self.master,
            width=300,
            height=300,
            name="frame",
        )
        self.frame.pack()

    def create_buttons(self,N=3):
        for y in range(N):
            for x in range(N):
                buttons = tk.Button(
                    self.frame,
                    width=10,
                    height=10,
                    text="",
                    fg="SystemButtonFace",
                    font=("",20),
                    name=str(x)+" "+str(y)
                )
                buttons.grid(column=x, row=y)
        
if __name__ == "__main__":
    master = tk.Tk()
    GameFrameUI(master)
    master.mainloop()