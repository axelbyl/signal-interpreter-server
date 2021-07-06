# pylint: disable=missing-docstring
import pytest
from src.parser_factory import ParserFactory


def test_load_file():
    parser_factory = ParserFactory()
    with pytest.raises(ValueError):
        parser_factory.get_parser()
