from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch
from .base_model import BaseModel
from .mixins import TimerMixin

class BLIPCaptioner(BaseModel, TimerMixin):
    @TimerMixin.time_execution
    def __init__(self):
        super().__init__(
            name="BLIP Image Captioning Model",
            input_type="image",
            output_type="text",
            category="Image-to-Text",
            description="Generates captions for images."
        )
        self.processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = AutoModelForImageTextToText.from_pretrained("Salesforce/blip-image-captioning-base")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    @TimerMixin.time_execution
    def generate_response(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        output = self.model.generate(**inputs)
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption