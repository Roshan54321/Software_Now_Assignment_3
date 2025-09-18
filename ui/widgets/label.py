from tkinter import ttk
from ui.widgets.base_widget import BaseWidget

class Label(BaseWidget):
    def __init__(self, parent, text, **kwargs):
        super().__init__(parent)
        self.widget = ttk.Label(parent, text=text, **kwargs)