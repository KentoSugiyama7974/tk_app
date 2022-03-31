import tkinter as tk

class GameFrameUI:
    def __init__(self,master,N=3):
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

    def create_buttons(self,N):
        for y in range(N):
            for x in range(N):
                buttons = tk.Button(
                    self.frame,
                    width=10,
                    height=10,
                    bg="#EEE",
                    text="",
                    font=("",8),
                    name=str(x)+" "+str(y)
                )
                buttons.grid(column=x, row=y)
        
if __name__ == "__main__":
    master = tk.Tk()
    GameFrameUI(master,3)
    master.mainloop()