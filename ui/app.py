import tkinter as tk
from tkinter import messagebox
from ui.pages.main import MainPage
from ui import theme
from models import MODELS

class App:
    def __init__(self):
        # Create our main window
        self.root = tk.Tk()
        self.root.title("AI Models Simulation")
        self.root.geometry("800x600")

        # Load up our main page
        self.main_window = MainPage(self.root)
        self.main_window.pack(fill="both", expand=True)

        # Set up the menu bar
        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu, bg=theme.BG_COLOR)

        # Add all those dropdown menus at the top
        self.add_menubar()

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
        for key in self.main_window.instantiated_models.keys():
            model_menu = tk.Menu(models_menu)
            model_menu.add_command(label="Load Model", command=lambda k=key: self.main_window.load_model(k))
            model_menu.add_command(label="Run Model", command=lambda k=key: self.main_window.run_model(k))
            models_menu.add_cascade(label=key, menu=model_menu)

        # Help menu
        help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about) 

    def show_about(self):
        messagebox.showinfo(
            "About This Application",
            "AI Models Simulation\n\n"
            "This application allows you to load and run different AI models dynamically.\n\n"
            "Built with Python, Tkinter, and Hugging Face Transformers.\n"
        )