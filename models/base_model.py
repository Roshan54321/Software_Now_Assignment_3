from abc import ABC, abstractmethod

# Abstract base class for all models
class BaseModel(ABC):
    def __init__(self, name, input_type, output_type, category, description):
        self._name = name       
        self._input_type = input_type
        self._output_type = output_type
        self._category = category
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def input_type(self):
        return self._input_type

    @property
    def output_type(self):
        return self._output_type

    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description

    @abstractmethod
    def generate_response(self, input_data):
        # Each model must implement this
        pass

    def get_info(self):
        return {
            "name": self.name,
            "input_type": self.input_type,
            "output_type": self.output_type,
            "category": self.category,
            "description": self.description
        }