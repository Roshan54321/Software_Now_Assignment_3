# Base widget class for reusable components
class BaseWidget:
    def __init__(self, parent, **kwargs):
        self.parent = parent # The parent container (like a frame or window)
        self.widget = None

    # we don't have to type "my_widget.widget.pack()" everywhere
    def pack(self, **kwargs):
        self.widget.pack(**kwargs)