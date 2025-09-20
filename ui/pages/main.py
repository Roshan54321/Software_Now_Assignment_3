import tkinter as tk
from ui.widgets import Button, Label, TextArea, Radio, Entry, Frame, LabelFrame, DropdownMenu
from ui import theme

class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Build our UI from top to bottom - like stacking blocks!
        self.top_frame()
        self.middle_frame()
        self.bottom_frame()

    def on_submit(self):
        # Grab whatever the user typed and clean it up
        name = self.entry.get().strip()
        if name:
            self.status.config(text=f"Hello, {name}!")
        else:
            self.status.config(text="Please enter a name.")

    def load_model(self):
        # Show the user we're doing something)
        self.output_display.set("Model Loaded...")

    def run_model(self, n):
        # Let them know which model they picked and what they're feeding it
        self.output_display.set(f"Running Model {n} with input: {self.text_input.get()}")

    def clear_input(self):
        # clear all the input and output fields
        self.text_input.set("")
        self.output_display.set("")

    def browse_file(self):
        # Placeholder for now - this would open a file dialog in real life
        self.output_display.set("Browse file clicked...")

    def top_frame(self):
        # leave some space at the top
        Frame(self, height=10).pack(fill="x")

        # Main controls go here - model picker and load button
        top_frame = Frame(self).widget
        top_frame.pack(fill="x")

        Label(top_frame, text="Model Selection:").pack(side="left", padx=5)

        # Dropdown with the different AI model types
        DropdownMenu(top_frame, options=["Text-to-Image", "Text-to-Text", "Image-to-Text"]).pack(side="left", padx=5, pady=2)  

        Button(top_frame, text="Load Model", command=self.load_model).pack(side="left", padx=5)

        # Add some space above the horizontal line
        padding_frame = Frame(self, height=20).widget
        padding_frame.pack(fill="x")

        # This creates a thin horizontal line to separate sections
        Frame(padding_frame, bg=theme.NEUTRAL_COLOR, height=1).widget.pack(fill="x", pady=10) 

    def middle_frame(self):
        middle_frame = Frame(self).widget
        middle_frame.pack(fill="both", expand=True)

        input_frame = LabelFrame(middle_frame).widget
        input_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        Label(input_frame, text="User Input Section").pack(anchor="w", padx=5, pady=5)

        # Radio buttons to choose between text or image input
        mode_frame = Frame(input_frame).widget
        mode_frame.pack(fill="x", padx=5, pady=5)

        self.input_mode = tk.StringVar(value="Text")  # Default to text mode
        Radio(mode_frame, "Text", self.input_mode, "Text").pack(side="left", padx=5)
        Radio(mode_frame, "Image", self.input_mode, "Image").pack(side="left", padx=5)
        Button(mode_frame, "Browse", command=self.browse_file).pack(side="left", padx=5)

        # Text box for typing prompts
        self.text_input = TextArea(input_frame, height=6, width=40)
        self.text_input.pack(pady=10, padx=5, fill="both", expand=True)

        # Run and Clear buttons
        btn_frame = Frame(input_frame).widget
        btn_frame.pack(pady=5)
        Button(btn_frame, "Run Model 1", command=lambda: self.run_model(1)).pack(side="left", padx=5)
        Button(btn_frame, "Run Model 2", command=lambda: self.run_model(2)).pack(side="left", padx=5)
        Button(btn_frame, "Clear", command=self.clear_input).pack(side="left", padx=5)

        # Right side: where the AI shows off its work
        output_frame = LabelFrame(middle_frame).widget
        output_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        Label(output_frame, text="Model Output Section").pack(anchor="w", padx=5, pady=5)
        Label(output_frame, text="Output Display:").pack(anchor="w", padx=5, pady=5)
        self.output_display = TextArea(output_frame, height=10, width=40)
        self.output_display.pack(fill="both", expand=True, padx=5, pady=5)

    def bottom_frame(self):
        # Info section at the bottom
        bottom_frame = LabelFrame(self).widget
        bottom_frame.pack(side="left", fill="both", expand=True)
        Label(bottom_frame, text="Model Information & Explanation").pack(anchor="w", padx=5, pady=5)

        # Left side: tell them about their selected model
        info_frame = Frame(bottom_frame).widget
        info_frame.pack(side="left", fill="both", expand=True, padx=5)

        Label(info_frame, text="Selected Model Info:\n• Model Name\n• Category (Text, Vision, Audio)\n• Short Description").pack(anchor="w", padx=5, pady=5)

        # Right side: educational content about the code structure
        oop_frame = Frame(bottom_frame).widget
        oop_frame.pack(side="right", fill="both", expand=True, padx=5)

        Label(oop_frame, text="OOP Concepts Explanation:\n• Where Multiple Inheritance are used\n• Why Encapsulation was applied\n• How Polymorphism and Method Overriding are shown\n• Where Multiple Decorators are applied").pack(anchor="w", padx=5, pady=5)