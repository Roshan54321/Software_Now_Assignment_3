from abc import ABC, abstractmethod

# Abstract base class for all models
class BaseModel(ABC):
    def __init__(self, name, input_type, output_type, category, description, oop_concepts):
        self._name = name       
        self._input_type = input_type
        self._output_type = output_type
        self._category = category
        self._description = description
        self._is_loaded = False
        self._oop_concepts = oop_concepts

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

    @property
    def oop_concepts(self):
        return self._oop_concepts

    @property
    def is_loaded(self):
        return self._is_loaded

    @abstractmethod
    def generate_response(self, input_data):
        pass

    @abstractmethod
    def load_model(self):
        pass

    def get_info(self):
        return {
            "name": self.name,
            "input_type": self.input_type,
            "output_type": self.output_type,
            "category": self.category,
            "description": self.description,
            "oop_concepts": self.oop_concepts
        }