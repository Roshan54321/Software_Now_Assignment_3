from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch
from .base_model import BaseModel
from .mixins import TimerMixin

class BLIPCaptioner(BaseModel, TimerMixin):
    def __init__(self):
        super().__init__(
            name="BLIP Image Captioning Model",
            input_type="image",
            output_type="text",
            category="Image-to-Text",
            description="Generates captions for images.",
            oop_concepts = [
                "Encapsulation – hides image preprocessing and decoding behind generate_response",
                "Polymorphism – same generate_response interface as other models, behaves differently for images",
                "Inheritance – uses a common base structure for AI models",
                "Multiple Inheritance – combines base class and metadata mixins without code duplication"
            ]
        )
    
    @TimerMixin.time_execution
    def load_model(self):
        self.processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
        self.model = AutoModelForImageTextToText.from_pretrained("Salesforce/blip-image-captioning-base")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        self._is_loaded = True

    @TimerMixin.time_execution
    def generate_response(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs)
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption