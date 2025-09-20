import tkinter as tk
from ui.pages.main import MainPage
from ui import theme

class App:
    def __init__(self):
        # Create our main window
        self.root = tk.Tk()
        self.root.title("AI Models Simulation")
        self.root.geometry("800x600")

        # Set up the menu bar
        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu, bg=theme.BG_COLOR)

        # Add all those dropdown menus at the top
        self.add_menubar()

        # Load up our main page
        self.main_window = MainPage(self.root)
        self.main_window.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
    
    def add_menubar(self):
        # File menu
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Close Window", command=self.root.quit)  # Quit application
    
        # Models menu
        models_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Models", menu=models_menu)
        models_menu.add_command(label="Model 1")
        models_menu.add_command(label="Model 2")

        # Help menu
        help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About") 