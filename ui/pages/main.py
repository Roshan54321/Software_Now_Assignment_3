import tkinter as tk
from tkinter import ttk
from ui.widgets import Button, Label, Combobox, TextArea, Radio

def top_frame(self):
    top_frame = ttk.Frame(self)
    top_frame.pack(fill="x", pady=5, padx=5)

    Label(top_frame, text="Model Selection:").pack(side="left", padx=5)

    self.model_select = Combobox(top_frame, values=["Text-to-Image", "Text-to-Text", "Image-to-Text"])
    self.model_select.pack(side="left", padx=5)

    Button(top_frame, text="Load Model", command=self.load_model).pack(side="left", padx=5)

def middle_frame(self):
    middle_frame = ttk.Frame(self)
    middle_frame.pack(fill="both", expand=True, padx=5, pady=5)

    # Left panel (input)
    input_frame = ttk.LabelFrame(middle_frame, text="User Input Section")
    input_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    self.input_mode = tk.StringVar(value="Text")
    Radio(input_frame, "Text", self.input_mode, "Text").pack(side="left", padx=5)
    Radio(input_frame, "Image", self.input_mode, "Image").pack(side="left", padx=5)

    Button(input_frame, "Browse", command=self.browse_file).pack(side="left", padx=5)

    self.text_input = TextArea(input_frame, height=6, width=40)
    self.text_input.pack(pady=10, padx=5, fill="both", expand=True)

    btn_frame = ttk.Frame(input_frame)
    btn_frame.pack(pady=5)
    Button(btn_frame, "Run Model 1", command=lambda: self.run_model(1)).pack(side="left", padx=5)
    Button(btn_frame, "Run Model 2", command=lambda: self.run_model(2)).pack(side="left", padx=5)
    Button(btn_frame, "Clear", command=self.clear_input).pack(side="left", padx=5)

    # Right panel (output)
    output_frame = ttk.LabelFrame(middle_frame, text="Model Output Section")
    output_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    Label(output_frame, text="Output Display:").pack(anchor="w", padx=5, pady=5)
    self.output_display = TextArea(output_frame, height=10, width=40)
    self.output_display.pack(fill="both", expand=True, padx=5, pady=5)

def bottom_frame(self):
    bottom_frame = ttk.LabelFrame(self, text="Model Information & Explanation")
    bottom_frame.pack(fill="both", expand=True, padx=5, pady=5)

    info = ttk.Frame(bottom_frame)
    info.pack(side="left", fill="both", expand=True, padx=5)

    Label(info, text="Selected Model Info:\n• Model Name\n• Category (Text, Vision, Audio)\n• Short Description").pack(anchor="w", padx=5, pady=5)

    oop = ttk.Frame(bottom_frame)
    oop.pack(side="right", fill="both", expand=True, padx=5)

    Label(oop, text="OOP Concepts Explanation:\n• Where Multiple Inheritance are used\n• Why Encapsulation was applied\n• How Polymorphism and Method Overriding are shown\n• Where Multiple Decorators are applied").pack(anchor="w", padx=5, pady=5)

    Label(self, text="Notes  Extra notes, instructions, or references.").pack(anchor="w", padx=5, pady=5)

class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        top_frame(self)
        middle_frame(self)
        bottom_frame(self)

    def on_submit(self):
        """Handles the button click."""
        name = self.entry.get().strip()
        if name:
            self.status.config(text=f"Hello, {name}! 👋")
        else:
            self.status.config(text="⚠️ Please enter a name.")

    def load_model(self):
        self.output_display.set("Model Loaded...")

    def run_model(self, n):
        self.output_display.set(f"Running Model {n} with input: {self.text_input.get()}")

    def clear_input(self):
        self.text_input.set("")
        self.output_display.set("")

    def browse_file(self):
        self.output_display.set("Browse file clicked...")