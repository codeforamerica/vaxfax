# content of conftest.py
import pytest
from api import create_app

@pytest.fixture
def app(request):
    create_app('flask_config.TestingConfig')
    return app
