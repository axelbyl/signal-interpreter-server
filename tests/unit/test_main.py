# pylint: disable=missing-docstring
import os
from unittest.mock import patch
from src.main import parse_arguments, main, ArgumentParser, signal_interpreter_app, init, read_database, parser_factory


class MockArgs:
    file_path = "path/to/file"


class MockParser:
    def load_file(self, path):
        pass


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file-path")


@patch.object(parser_factory, "get_parser")
@patch.object(parser_factory, "set_signal_database_format", return_value=MockParser)
def test_read_database(mock_parser_factory_set_signal, mock_parser_factory_get_parser):
    dummy_path = os.path.join("..", "fixture", "test_basic.json")
    read_database(dummy_path)
    mock_parser_factory_set_signal.assert_called_with("json")
    mock_parser_factory_get_parser.assert_called_once()


@patch.object(signal_interpreter_app, "run")
@patch("src.main.read_database")
@patch("src.main.parse_arguments", return_value=MockArgs)
def test_main(mock_parse_arguments, mock_read_database, mock_run):
    main()
    mock_parse_arguments.assert_called_once()
    mock_read_database.assert_called_with(MockArgs.file_path)
    mock_run.assert_called_once()


@patch("src.main.main")
@patch("src.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
