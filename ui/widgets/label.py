import tkinter as tk
from ui.widgets.base_widget import BaseWidget
from ui import theme

class Label(BaseWidget):
    def __init__(self, parent, text, **kwargs):
        kwargs.setdefault("bg", theme.BG_COLOR)
        kwargs.setdefault("fg", theme.TEXT_COLOR)
        super().__init__(parent)
        self.widget = tk.Label(parent, text=text, **kwargs)