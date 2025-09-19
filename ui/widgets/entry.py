import tkinter as tk
from ui.widgets.base_widget import BaseWidget
from ui import theme
class Entry(BaseWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        kwargs.setdefault("bg", theme.BG_COLOR)
        kwargs.setdefault("fg", theme.TEXT_COLOR)
        self.widget = tk.Entry(parent, **kwargs)

    def get(self):
        return self.widget.get()

    def set(self, text):
        self.widget.delete(0, "end")
        self.widget.insert(0, text)