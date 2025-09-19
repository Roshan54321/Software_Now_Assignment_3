import tkinter as tk
from ui.widgets.base_widget import BaseWidget
from ui import theme

class Radio(BaseWidget):
    def __init__(self, parent, text, variable, value, **kwargs):
        kwargs.setdefault("bg", theme.BG_COLOR)
        kwargs.setdefault("fg", theme.TEXT_COLOR)
        super().__init__(parent)
        self.widget = tk.Radiobutton(parent, text=text, variable=variable, value=value, **kwargs)