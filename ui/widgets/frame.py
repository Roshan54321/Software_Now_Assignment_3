import tkinter as tk
from ui.widgets.base_widget import BaseWidget
from ui import theme

class Frame(BaseWidget):
    def __init__(self, parent, **kwargs):
        kwargs.setdefault("bg", theme.BG_COLOR)
        super().__init__(parent)
        self.widget = tk.Frame(parent, **kwargs)