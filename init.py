import json


class Config:
    """Loads the initialising values for the game"""

    def __init__(self):
        self.data = self.load_values()
        self.max_val = self.data["max_val"]
        self.min_val = self.data["min_val"]
        self.no_questions = self.data["no_questions"]

    @staticmethod
    def load_values():
        with open('config') as file:
            return json.load(file)
