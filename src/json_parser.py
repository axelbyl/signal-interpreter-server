import json

class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        with open(file_path) as f:
            self.data = json.load(f)

    def get_signal_title(self, identifier):
        for entry in self.data["services"]:
            if entry["id"] == identifier:
                return entry["title"]
