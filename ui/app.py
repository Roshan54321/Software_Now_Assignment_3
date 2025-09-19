import tkinter as tk
from ui.pages.main import MainPage
from ui import theme

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Models Simulation")
        self.root.geometry("800x600")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu, bg=theme.BG_COLOR)

        self.add_menubar()

        self.main_window = MainPage(self.root)
        self.main_window.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
    
    def add_menubar(self):
        models_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Models", menu=models_menu)
        models_menu.add_command(label="Model 1")
        models_menu.add_command(label="Model 2")
        models_menu.add_separator()
        models_menu.add_command(label="Exit")

        help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")