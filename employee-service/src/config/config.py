import json
import os


class Config:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), "application.json")
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def get(self, key: str):
        return self.config.get(key)


config = Config()
