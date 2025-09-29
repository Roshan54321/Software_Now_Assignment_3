import tkinter as tk
from tkinter import messagebox
from ui.pages.main import MainPage
from ui import theme
from models import MODELS

class App:
    def __init__(self):
        # Create our main window
        self.root = tk.Tk()
        self.root.title("AI Models Simulation")
        self.root.geometry("800x800")
        
        # Set minimum window size to prevent layout issues
        self.root.minsize(1024, 768)
        
        # Configure window closing behavior
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Load up our main page
        self.main_window = MainPage(self.root)
        self.main_window.pack(fill="both", expand=True)

        # Set up the menu bar
        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu, bg=theme.BG_COLOR)

        # Add all those dropdown menus at the top
        self.add_menubar()
        
        # Center the window on screen
        self.center_window()

    def run(self):
        # Start the application main loop
        self.root.mainloop()
    
    def center_window(self):
        # Center the window on the screen
        try:
            self.root.update_idletasks()
            
            # Get screen dimensions
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            # Get window dimensions
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            
            # Calculate center position
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)
            
            # Set window position
            self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        except Exception as e:
            print(f"Could not center window: {e}")
    
    def on_closing(self):
        # Handle window closing with confirmation
        try:
            # Check if any models are currently loaded
            loaded_models = [
                name for name, model in self.main_window.instantiated_models.items()
                if hasattr(model, 'is_loaded') and model.is_loaded
            ]
            
            if loaded_models:
                response = messagebox.askyesno(
                    "Confirm Exit",
                    f"You have {len(loaded_models)} model(s) loaded.\n"
                    "Are you sure you want to exit?"
                )
                if response:
                    self.root.destroy()
            else:
                self.root.destroy()
        except Exception as e:
            print(f"Error during closing: {e}")
            self.root.destroy()
    
    def add_menubar(self):
        # Create and configure the menu bar
        # File menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear All", command=self.clear_all)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing, accelerator="Alt+F4")
    
        # Models menu
        models_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Models", menu=models_menu)
        
        # Add "Load All Models" option
        models_menu.add_command(
            label="Load All Models",
            command=self.load_all_models
        )
        models_menu.add_separator()
        
        for key in self.main_window.instantiated_models.keys():
            model_menu = tk.Menu(models_menu, tearoff=0)
            model_menu.add_command(
                label="Load Model",
                command=lambda k=key: self.main_window.load_model(k)
            )
            model_menu.add_command(
                label="Run Model",
                command=lambda k=key: self.main_window.run_model(k)
            )
            models_menu.add_cascade(label=key, menu=model_menu)

        # View menu
        view_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(
            label="Reset Window Size",
            command=lambda: self.root.geometry("800x800")
        )
        view_menu.add_command(
            label="Center Window",
            command=self.center_window
        )

        # Help menu
        help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Model Info", command=self.show_model_info)

    def clear_all(self):
        # Clear all input and output fields
        try:
            response = messagebox.askyesno(
                "Clear All",
                "This will clear all input and output fields.\nContinue?"
            )
            if response:
                self.main_window.clear_input()
        except Exception as e:
            messagebox.showerror("Error", f"Could not clear fields: {str(e)}")

    def load_all_models(self):
        # Load all available models
        try:
            response = messagebox.askyesno(
                "Load All Models",
                f"This will load all {len(MODELS)} models.\n"
                "This may take some time and use significant memory.\nContinue?"
            )
            if response:
                success_count = 0
                failed_models = []
                
                for model_name in self.main_window.instantiated_models.keys():
                    try:
                        self.main_window.load_model(model_name)
                        success_count += 1
                    except Exception as e:
                        failed_models.append(f"{model_name}: {str(e)}")
                
                # Show results
                if failed_models:
                    messagebox.showwarning(
                        "Models Loaded with Errors",
                        f"Successfully loaded {success_count} model(s).\n\n"
                        f"Failed models:\n" + "\n".join(failed_models)
                    )
                else:
                    messagebox.showinfo(
                        "Success",
                        f"Successfully loaded all {success_count} models!"
                    )
        except Exception as e:
            messagebox.showerror("Error", f"Could not load models: {str(e)}")

    def show_model_info(self):
        # Display information about available models
        try:
            model_list = []
            for name, model_class in MODELS.items():
                try:
                    model_instance = self.main_window.instantiated_models.get(name)
                    if model_instance:
                        status = "✓ Loaded" if hasattr(model_instance, 'is_loaded') and model_instance.is_loaded else "○ Not loaded"
                        model_list.append(f"{name}: {status}")
                    else:
                        model_list.append(f"{name}: Available")
                except Exception as e:
                    model_list.append(f"{name}: Error - {str(e)}")
            
            info_text = "Available Models:\n\n" + "\n".join(model_list)
            messagebox.showinfo("Model Information", info_text)
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve model info: {str(e)}")

    def show_about(self):
        # Display application information
        messagebox.showinfo(
            "About This Application",
            "AI Models Simulation\n"
            "Version: 1.0\n\n"
            "This application allows you to load and run different AI models dynamically.\n\n"
            "Features:\n"
            "• Multiple AI model support\n"
            "• Text and image input\n"
            "• Dynamic model switching\n"
            "• Educational OOP concepts\n\n"
            "Built with Python, Tkinter, and Hugging Face Transformers.\n\n"
            "© 2025 Software Now Assignment 3"
        )