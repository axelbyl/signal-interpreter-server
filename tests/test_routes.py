from unittest.mock import patch
from src.routes import signal_interpreter_app, json_parser



#@patch.object(json_parser, "get_signal_title", return_value="ECU Reset")
def test_my_routes_function():
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    signal_interpreter_app.testing = True
    signal_interpreter_app_instance = signal_interpreter_app.test_client()

    with signal_interpreter_app_instance as client:
        my_payload = {"signal": "11"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "ECU Reset"

