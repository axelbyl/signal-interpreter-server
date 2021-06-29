import sys
import os
import pytest
from unittest.mock import patch
from src.main import main
from src.routes import signal_interpreter_app


CURR_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURE_path = os.path.join(CURR_DIR, "fixtures", "test_basic.json")

@pytest.mark.parametrize("payload, expected_status_code, expected_response", [
    ({"signal": "11"}, 200, "ECU Reset"),
    ({"signal": "99"}, 400, None),
    ({"DUMMY": "27"}, 404, None)
])
@patch.object(sys, "argv", ["main", "--file-path", FIXTURE_path])
def test_call_response(payload, expected_status_code, expected_response, signal_interpreter_app_instance):
    with patch.object(signal_interpreter_app, "run"):
        with signal_interpreter_app_instance as client:
            main()
            response = client.post("/", json=payload)
            assert response.get_json() == expected_response
            assert response.status_code == expected_status_code




