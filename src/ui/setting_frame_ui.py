import tkinter as tk

class SettingFrameUi:
    def __init__(self, master):
        self.master = master
        self.create_frame()
        self.create_button()

    def create_frame(self):
        self.frame = tk.Frame(
            self.master,
        )
        self.frame.pack()

    def create_button(self):
        self.button = tk.Button(
            self.frame,
        )
        self.button.pack()

if __name__ == "__main__":
    master = tk.Tk()
    SettingFrameUi(master)
    master.mainloop()