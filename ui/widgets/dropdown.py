import tkinter as tk
from ui.widgets.base_widget import BaseWidget
from ui import theme

class DropdownMenu(BaseWidget):
    def __init__(self, parent, options, default=None, command=None, **kwargs):
        super().__init__(parent)

        self.var = tk.StringVar(value=default if default is not None else options[0])
        self.widget = tk.OptionMenu(parent, self.var, *options, command=command)

        self.widget.config(
            bg=kwargs.get("bg", theme.BG_COLOR),
            fg=kwargs.get("fg", theme.TEXT_COLOR),
            activeforeground=kwargs.get("activeforeground", theme.TEXT_COLOR),
            highlightthickness=0            
        )

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)