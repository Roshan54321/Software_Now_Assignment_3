# AI Models Simulation

A user-friendly desktop application built with **Tkinter** that allows users to interact with multiple AI models (text-to-text, image-to-text) from a single interface. The app demonstrates modular design, object-oriented programming concepts, and python fundamentals.

---
  

## Features

- **Model Selection:** Easily choose between multiple pre-registered AI models.

- **Dynamic Model Loading:** Load models on-demand without restarting the app.

- **Input Modes:** Support for both text and image inputs.

- **File Browsing:** Import text or image files directly.

- **Output Display:** View results in a text box or as images.

- **OOP Concepts:** Encapsulation, inheritance, polymorphism, and multiple decorators demonstrated in the code structure.

- **Responsive Layout:** Input, output, and model info sections adjust dynamically.

- **Placeholder Images:** Displays thumbnail placeholders for image input.

---


## Installation

1. **Clone the repository:**

	```bash
	git clone https://github.com/Roshan54321/Software_Now_Assignment_3
	```

2. **Create a virtual environment:**

	```bash
	python -m venv env
	source env/bin/activate # Linux / macOS
	```

3. **Configure VSCode Python path**

	- Open VSCode in your project root directory
	- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
	- Type "Python: Select Interpreter"
	- Choose the Python interpreter you're using
	- Make sure the workspace folder is set to your project root
  

4. **Install dependencies:**

	```bash
	pip install -r requirements.txt
	```


5. **Application folder structure (related):**

	```
	project_root/
	├─ resources/
	├─ models/
	├─ ui/
	└─ main.py
	```
---


## Usage

  

1. Run the application:

	```bash
	python main.py
	```

3. Select a model from the dropdown in the top panel.

4. Choose input mode:

	-  **Text:** Type your prompt in the text area or upload a `.txt` file.

	-  **Image:** Browse or drop an image file. A placeholder thumbnail will appear if no image is selected.

4. Click **Load Model** to initialize the selected AI model.

5. Click **Run Model** to generate output. Output will appear in the right-hand panel.

6. Click **Clear** to reset input and output fields.

---