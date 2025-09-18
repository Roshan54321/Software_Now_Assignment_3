import tkinter as tk
from ui.pages.main import MainPage

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Models Simulation")
        self.root.geometry("800x600")

        self.main_window = MainPage(self.root)
        self.main_window.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()