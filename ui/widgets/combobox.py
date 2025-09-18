from tkinter import ttk
from ui.widgets.base_widget import BaseWidget

class Combobox(BaseWidget):
    def __init__(self, parent, values, **kwargs):
        super().__init__(parent)
        self.widget = ttk.Combobox(parent, values=values, state="readonly", **kwargs)

    def get(self):
        return self.widget.get()

    def set(self, value):
        self.widget.set(value)