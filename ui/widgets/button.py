import tkinter as tk
from ui.widgets.base_widget import BaseWidget
from ui import theme

class Button(BaseWidget):
    def __init__(self, parent, text, command=None, **kwargs):
        super().__init__(parent)

        kwargs.setdefault("bg", theme.BUTTON_COLOR)
        kwargs.setdefault("fg", theme.TEXT_COLOR)
        kwargs.setdefault("highlightbackground", theme.BG_COLOR)
        kwargs.setdefault("activebackground", theme.BUTTON_COLOR)
        kwargs.setdefault("relief", "raised")

        self.widget = tk.Button(parent, text=text, command=command, **kwargs)
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        

    def on_enter(self, event):
        self.widget['background'] = "#808080"  # or any color you like for hover
        

    def on_leave(self, event):
        self.widget['background'] = theme.BUTTON_COLOR
        
