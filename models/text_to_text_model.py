from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from .base_model import BaseModel
from .mixins import TimerMixin

class TextGenModel(BaseModel, TimerMixin):
    @TimerMixin.time_execution
    def __init__(self):
        super().__init__(
            name="GPT2 Model",
            input_type="text",
            output_type="text",
            category="Text-to-Text",
            description="Generates text based on input prompts."
        )
        self.tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
        self.model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")
        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
        self.model.to(self.device)

    @TimerMixin.time_execution
    def generate_response(self, prompt, max_tokens=50):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response