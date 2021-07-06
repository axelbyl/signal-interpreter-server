"""This module declares the JsonParser class"""
import json
from src.xml_parser import NotInDatabaseError


class JsonParser:
    """Jsonparser class"""

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """Method for loading a Json-file and adding it to self.data"""
        with open(file_path) as f:
            self.data = json.load(f)

    def get_signal_title(self, identifier):
        """Returns title of signal with id "identifier" """

        for entry in self.data["services"]:
            if entry["id"] == identifier:
                title = entry["title"]
                return title
        raise NotInDatabaseError("The requested id is not present in database")
