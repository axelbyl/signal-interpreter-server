import pytest
from src.routes import signal_interpreter_app


@pytest.fixture
def signal_interpreter_app_instance():
    signal_interpreter_app.testing = True
    return signal_interpreter_app.test_client()

