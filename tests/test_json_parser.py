from unittest.mock import patch
import pytest
from src.json_parser import JsonParser


def test_load_file():
    json_parser = JsonParser()
    assert json_parser.data is None
    json_parser.load_file(r'signal_database.json')
    assert json_parser.data is not None


@pytest.mark.parametrize("id_number, expected_result", [
    ("11", "ECU Reset"),
    ("12", "ECU Start"),
    ("15", None),
])
def test_get_signal_title(id_number, expected_result):
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "ECU Stop", "id": "14"}, {"title": "ECU Start", "id": "12"}]}
    assert json_parser.get_signal_title(id_number) == expected_result


def test_get_signal_title_no_data():
    json_parser = JsonParser()
    assert json_parser.get_signal_title('11') == None
