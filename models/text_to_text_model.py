from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from .base_model import BaseModel
from .mixins import TimerMixin

class TextGenModel(BaseModel, TimerMixin):
    def __init__(self):
        super().__init__(
            name="GPT2 Model",
            input_type="text",
            output_type="text",
            category="Text-to-Text",
            description="Generates text based on input prompts.",
            oop_concepts = [
                "Encapsulation – wraps tokenization, text generation, and decoding in one method",
                "Polymorphism – shares generate_response API with BLIP model, but works for text",
                "Inheritance – consistent base structure for easy GUI and model integration",
                "Decorators – uses @property and custom decorators for clean design and structure"
            ]
        )

    @TimerMixin.time_execution
    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
        self.model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")
        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
        self.model.to(self.device)
        self._is_loaded = True

    @TimerMixin.time_execution
    def generate_response(self, prompt, max_tokens=50):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response