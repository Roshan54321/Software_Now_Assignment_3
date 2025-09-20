from .image_to_text_model import BLIPCaptioner
from .text_to_text_model import TextGenModel

# Each model is stored with metadata and its class
MODELS = {
    "Image-to-text": BLIPCaptioner,
    "Text-to-Text": TextGenModel
}