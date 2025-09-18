from tkinter import ttk
from ui.widgets.base_widget import BaseWidget

class Radio(BaseWidget):
    def __init__(self, parent, text, variable, value, **kwargs):
        super().__init__(parent)
        self.widget = ttk.Radiobutton(parent, text=text, variable=variable, value=value, **kwargs)