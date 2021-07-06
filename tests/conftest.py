# pylint: disable=missing-docstring
import pytest
from src.routes import signal_interpreter_app
from src.json_parser import JsonParser
from src.xml_parser import XmlParser


@pytest.fixture
def signal_interpreter_app_instance():
    signal_interpreter_app.testing = True
    return signal_interpreter_app.test_client()


@pytest.fixture
def json_parser_instance():
    json_parser = JsonParser()
    json_parser.data =\
        {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "ECU Start", "id": "12"}]}
    return json_parser


@pytest.fixture
def xml_parser_instance():
    xml_parser = XmlParser()
    xml_parser.data = {"services": {"service": [{"title": "ECU Reset", "@id": "11"}, {"title": "ECU Start", "@id": "12"}]}}
    return xml_parser
