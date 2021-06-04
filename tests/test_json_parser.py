from unittest.mock import patch
from src.json_parser import JsonParser


def test_load_file():
    json_parser = JsonParser()
    assert json_parser.data == None
    json_parser.load_file(r'..\signal_database.json')
    assert json_parser.data != None


def test_get_signal_title():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_signal_title('11') == "ECU Reset"