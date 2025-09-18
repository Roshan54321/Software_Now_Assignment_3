import tkinter as tk
from ui.widgets.base_widget import BaseWidget

class TextArea(BaseWidget):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.widget = tk.Text(parent, **kwargs)

    def get(self):
        return self.widget.get("1.0", tk.END).strip()

    def set(self, text):
        self.widget.delete("1.0", tk.END)
        self.widget.insert(tk.END, text)