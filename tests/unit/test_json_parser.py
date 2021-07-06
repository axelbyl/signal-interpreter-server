# pylint: disable=missing-docstring
import pytest
from src.json_parser import JsonParser, NotInDatabaseError


def test_load_file():
    json_parser = JsonParser()
    assert json_parser.data is None
    json_parser.load_file(r'signal_database.json')
    assert json_parser.data is not None


@pytest.mark.parametrize("id_number, expected_result", [
    ("11", "ECU Reset"),
    ("12", "ECU Start"),
])
def test_get_signal_title(id_number, expected_result, json_parser_instance):
    assert json_parser_instance.get_signal_title(id_number) == expected_result


def test_get_signal_title_no_data(json_parser_instance):
    with pytest.raises(NotInDatabaseError):
        json_parser_instance.get_signal_title('13')
