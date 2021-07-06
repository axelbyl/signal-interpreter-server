# pylint: disable=missing-docstring
from src.routes import parser_factory


def test_routes_valid(json_parser_instance, signal_interpreter_app_instance):
    parser_factory.set_signal_database_format("json")
    parser = parser_factory.get_parser()
    parser.data = json_parser_instance.data

    with signal_interpreter_app_instance as client:
        my_payload = {"signal": "11"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "ECU Reset"


def test_routes_bad_request(json_parser_instance, signal_interpreter_app_instance):
    parser_factory.set_signal_database_format("json")
    parser = parser_factory.get_parser()
    parser.data = json_parser_instance.data

    with signal_interpreter_app_instance as client:
        my_payload = {"sign": "11"}
        assert client.post("/", json=my_payload).status_code == 404


def test_routes_request_out_of_bounds(json_parser_instance, signal_interpreter_app_instance):
    parser_factory.set_signal_database_format("json")
    parser = parser_factory.get_parser()
    parser.data = json_parser_instance.data

    with signal_interpreter_app_instance as client:
        my_payload = {"signal": "111"}
        assert client.post("/", json=my_payload).status_code == 400
