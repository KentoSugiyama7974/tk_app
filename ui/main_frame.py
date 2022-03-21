import tkinter as tk

class MainFrame:
    def __init__(self, master):
        self.master = master
        self.main_canvas()
        self.create_scrollbar()

    def main_canvas(self):
        self.canvas = tk.Canvas(
            self.master,
            width=400,
            height=300,
            scrollregion=(-200, -100, 800, 600)
        )
        self.canvas.pack()

    def create_scrollbar(self):
        self.ybar = tk.Scrollbar(
            self.master,
            orient=tk.VERTICAL,
        )
        self.ybar.pack()

if __name__ == "__main__":
    master = tk.Tk()
    MainFrame(master)
    master.mainloop()