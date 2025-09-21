import tkinter as tk
from tkinter import filedialog
from ui.widgets import Button, Label, TextArea, Radio, Frame, LabelFrame, DropdownMenu
from ui import theme
from PIL import Image, ImageTk
from models import MODELS

class MainPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Dynamically instantiate all models
        self.instantiated_models = {
            key: value() for key, value in MODELS.items()
        }
        
        # Build our UI from top to bottom
        self.top_frame()
        self.middle_frame()
        self.bottom_frame()

        # Set default model info
        self.current_model = list(MODELS.keys())[0]
        self.on_model_change(self.current_model)

        # Load placeholder thumbnail icon
        img_icon = Image.open("resources/images/placeholder-image.jpg")
        img_icon.thumbnail((200, 200))  # small placeholder size
        self.placeholder_icon = ImageTk.PhotoImage(img_icon)  # keep reference

    def on_submit(self):
        # Grab whatever the user typed and clean it up
        name = self.entry.get().strip()
        if name:
            self.status.config(text=f"Hello, {name}!")
        else:
            self.status.config(text="Please enter a name.")

    # call load_model on the selected model instance
    def load_model(self, model=None):
        model_name = model if model else self.current_model
        self.set_output(f"Loading {model_name} model...", "text")
        self.update_idletasks()
        model_instance = self.instantiated_models[model_name]
        model_instance.load_model()
        self.set_output(f"{model_name} Model has been loaded successfully. You can now run the model.", "text")


    def clear_input(self):
        # Clear input
        if hasattr(self.text_input, "set"):
            self.text_input.set("")
        elif hasattr(self.text_input, "widget"):
            # If it's an image Label, remove image and path
            # Just reuse the already loaded placeholder
            self.text_input.widget.config(
                image=self.placeholder_icon,
                text="",
                compound="center"
            )
            self.text_input.image_ref = self.placeholder_icon
            self.text_input.image_path = None

        # Clear output
        if hasattr(self.output_display, "set"):
            self.output_display.set("")
        elif hasattr(self.output_display, "widget"):
            self.output_display.widget.config(image=None, text="")
            if hasattr(self.output_display, "image_ref"):
                self.output_display.image_ref = None
    
    def update_input_display(self):
        # Switch input display between text and image based on radio button
        mode = self.input_mode.get()
        # Remove current widget
        self.text_input.widget.pack_forget()
        
        if mode == "text":
            # Replace with TextArea
            self.text_input = TextArea(self.text_input.widget.master, width=30, height=10)
            self.text_input.pack(pady=10, padx=5, fill="both", expand=True)
        elif mode == "image":
            # Replace with Label showing the placeholder icon
            self.text_input = Label(
                self.text_input.widget.master,
                text="",
                bg=theme.TEXTBOX_COLOR,
                width=30,
                height=10
            )
            self.text_input.widget.config(
                image=self.placeholder_icon,
                text="",
                compound="center"
            )
            self.text_input.pack(pady=10, padx=5, fill="both", expand=True)
            self.text_input.image_ref = self.placeholder_icon  # keep reference
            self.text_input.image_path = None

    def browse_file(self):
        if self.input_mode.get() == "text":
            filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
            file_path = filedialog.askopenfilename(title="Select Text File", filetypes=filetypes)
            if file_path:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    self.text_input.set(content)
                except Exception as e:
                    self.text_input.set(f"Error reading file: {e}")
        elif self.input_mode.get() == "image":
            filetypes = (("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*"))
            file_path = filedialog.askopenfilename(title="Select Image File", filetypes=filetypes)
            if file_path:
                # Load image
                img = Image.open(file_path)
                img.thumbnail((200, 200))  # resize to fit the box
                photo = ImageTk.PhotoImage(img)
                self.text_input.widget.config(image=photo, text="")
                self.text_input.image_ref = photo  # keep reference
                self.text_input.image_path = file_path  # keep image path

    def top_frame(self):
        # leave some space at the top
        Frame(self, height=10).pack(fill="x")

        # Main controls go here - model picker and load button
        top_frame = Frame(self).widget
        top_frame.pack(fill="x")

        Label(top_frame, text="Model Selection:").pack(side="left", padx=5)

        # Dropdown with the different AI model types
        DropdownMenu(
            top_frame,
            options=list(MODELS.keys()),
            default=list(MODELS.keys())[0],
            command=self.on_model_change
        ).pack(side="left", padx=5)

        Button(top_frame, text="Load Model", command=self.load_model).pack(side="left", padx=5)
        Button(top_frame, "Clear", command=self.clear_input).pack(side="right", padx=5)

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
        mode_frame.pack(fill="x", padx=5)

        self.input_mode = tk.StringVar(value="text")  # Default to text mode
        self.input_mode.trace_add("write", lambda *args: self.update_input_display())
        Radio(mode_frame, "Text", self.input_mode, "text").pack(side="left", padx=5)
        Radio(mode_frame, "Image", self.input_mode, "image").pack(side="left", padx=5)
        Button(mode_frame, "Browse", command=self.browse_file).pack(side="left", padx=5)

        # Text box for typing prompts
        self.text_input = TextArea(input_frame, height=5, width=40)
        self.text_input.pack(pady=10, padx=5, fill="both", expand=True)

        # Right side: where the AI shows off its work
        output_frame = LabelFrame(middle_frame).widget
        output_frame.pack(side="right", fill="both",expand=True, padx=5, pady=5)
        Label(output_frame, text="Model Output Section").pack(anchor="w", padx=5, pady=5)
        Button(output_frame, "Run Model", command=lambda: self.run_model()).pack(anchor="w", padx=5)
        self.output_display = TextArea(output_frame, height=5, width=40)
        self.output_display.pack(pady=10, padx=5, fill="both", expand=True)

    def bottom_frame(self):
        bottom_frame = LabelFrame(self).widget
        bottom_frame.pack(fill="both", expand=True)

        # Left side: model info
        self.info_frame = Frame(bottom_frame).widget
        self.info_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Right side: educational content (static)
        self.oop_frame = Frame(bottom_frame).widget
        self.oop_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    def on_model_change(self, model_name):
        self.current_model = model_name
        model_instance = self.instantiated_models.get(model_name)
        if not model_instance:
            return

        # Set bottom frame info dynamically from registry
        self.update_bottom_frame(
            model_name=model_instance.name,
            category=model_instance.category,
            description=model_instance.description,
            oop_concepts=model_instance.oop_concepts
        )

    def update_bottom_frame(self, model_name, category, description, oop_concepts):
        # Clear old info
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        for widget in self.oop_frame.winfo_children():
            widget.destroy()

        # Add new model info
        info_text = f"• Model Name: {model_name}\n• Category: {category}\n• Description: {description}"
        oop_concepts_text = f"{'\n'.join(oop_concepts)}"

        Label(self.info_frame, text="Selected Model Info:", justify="left", wraplength=450).pack(anchor="w")
        Label(self.info_frame, text=info_text, justify="left", wraplength=300).pack(anchor="w", padx=5, pady=5)
        Label(self.oop_frame, text="OOP Concepts Explanation:", justify="left", wraplength=450).pack(anchor="w")
        Label(self.oop_frame, text=oop_concepts_text, justify="left", wraplength=450).pack(anchor="w", padx=5, pady=5)

    def set_output(self, content, content_type="text"):
        # Update the output display based on content type
        self.output_type = content_type
        self.output_display.widget.pack_forget()  # remove previous widget
        
        if content_type == "text":
            # Show TextArea
            self.output_display = TextArea(self.output_display.widget.master, height=10, width=40)
            self.output_display.set(content)
            self.output_display.pack(fill="both", expand=True, padx=5, pady=5)
        elif content_type == "image":
            # Show image
            self.output_display = Label(self.output_display.widget.master, bg=theme.TEXTBOX_COLOR)
            img = Image.open(content)
            img.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(img)
            self.output_display.widget.config(image=photo)
            self.output_display.image_ref = photo
            self.output_display.widget.pack(fill="both", expand=True, padx=5, pady=5)

    def run_model(self, model=None):
        self.set_output("Running the model...", "text")
        self.update_idletasks()
        
        model_name = model if model else self.current_model
        model_instance = self.instantiated_models[model_name]

        if not model_instance.is_loaded:
            self.set_output("Please load the model first.", "text")
            return

        # check if input type matches model input type
        if self.input_mode.get() != model_instance.input_type:
            self.set_output(f"Please provide {model_instance.input_type} input for this model.", "text")
            return

        input_content = self.text_input.get() if model_instance.input_type == "text" else getattr(self.text_input, "image_path", None)
        if not input_content:
            self.set_output("Please provide valid input.", "text")
            return

        output = model_instance.generate_response(input_content)

        self.set_output(output, model_instance.output_type)