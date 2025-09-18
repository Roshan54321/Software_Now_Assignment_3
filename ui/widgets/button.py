from tkinter import ttk
from ui.widgets.base_widget import BaseWidget

class Button(BaseWidget):
    def __init__(self, parent, text, command=None, **kwargs):
        super().__init__(parent)
        self.widget = ttk.Button(parent, text=text, command=command, **kwargs)