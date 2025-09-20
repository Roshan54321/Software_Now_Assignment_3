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

        self.widget = tk.Button(parent, text=text, command=command, **kwargs)