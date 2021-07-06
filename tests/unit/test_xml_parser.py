# pylint: disable=missing-docstring
import pytest
from src.xml_parser import XmlParser, NotInDatabaseError


def test_load_file():
    xml_parser = XmlParser()
    assert xml_parser.data is None
    xml_parser.load_file(r'signal_database.xml')
    assert xml_parser.data is not None


@pytest.mark.parametrize("id_number, expected_result", [
    ("11", "ECU Reset"),
    ("12", "ECU Start"),
])
def test_get_signal_title(id_number, expected_result, xml_parser_instance):
    assert xml_parser_instance.get_signal_title(id_number) == expected_result


def test_get_signal_title_no_data(xml_parser_instance):
    with pytest.raises(NotInDatabaseError):
        xml_parser_instance.get_signal_title('13')
