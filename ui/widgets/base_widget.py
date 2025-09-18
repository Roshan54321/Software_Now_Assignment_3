# Base widget class for reusable components
class BaseWidget:
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.widget = None

    def pack(self, **kwargs):
        self.widget.pack(**kwargs)