from tkinter import ttk
from ui.widgets.base_widget import BaseWidget

class Entry(BaseWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.widget = ttk.Entry(parent, **kwargs)

    def get(self):
        return self.widget.get()

    def set(self, text):
        self.widget.delete(0, "end")
        self.widget.insert(0, text)