from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from .base_model import BaseModel
from .mixins import TimerMixin

class TextGenModel(BaseModel, TimerMixin):  # Inheritance: derives from BaseModel and TimerMixin
    def __init__(self):
        super().__init__(
            name="GPT2 Model",
            input_type="text",
            output_type="text",
            category="Text-to-Text",
            description="Generates text based on input prompts.",
            oop_concepts=[
                "Encapsulation – wraps tokenization, text generation, and decoding in one method",
                "Polymorphism – shares generate_response API with BLIP model, but works for text",
                "Inheritance – consistent base structure for easy GUI and model integration",
                "Abstraction – exposes only high-level API to GUI, hides inner workings",
                "Method Overriding – load_model overrides BaseModel to customize loading",
                "Decorators – uses @property and custom decorators for clean design and structure"
            ]
        )
        self._is_loaded = False
        self._device = None

    @property  # Decorator: provides a property for device
    def device(self):
        # Abstraction: hides device selection logic from outside
        if self._device is None:
            if torch.cuda.is_available():
                self._device = "cuda"
            elif torch.backends.mps.is_available():
                self._device = "mps"
            else:
                self._device = "cpu"
        return self._device

    @TimerMixin.time_execution  # Decorator
    def load_model(self):  # Method Overriding: overrides BaseModel.load_model
        try:
            self.tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
            self.model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")
            self.model.to(self.device)
            self._is_loaded = True
        except Exception as e:
            self._is_loaded = False
            print(f"[ERROR] Failed to load text generation model: {e}")
            raise RuntimeError(f"Model loading failed: {e}")

    @TimerMixin.time_execution  # Decorator
    def generate_response(self, prompt, max_tokens=50):
        # Encapsulation: wraps tokenization, text generation, and decoding
        # Polymorphism: same API as BLIP model, different implementation for text
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
        except Exception as e:
            print(f"[ERROR] Failed to generate text: {e}")
            return f"Error: Failed to generate text. {e}"