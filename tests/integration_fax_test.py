# content of conftest.py
import pytest
from api import create_app
from conftest import (
    valid_fax_info,
)
import json
from unittest.mock import patch


@pytest.fixture
def app(request):
    app = create_app('flask_config.TestingConfig')
    app = app.test_client()
    return app


class TestFaxResource:
    def test_valid_call_returns_result(self, app, valid_fax_info):
        valid_fax_info = json.dumps(valid_fax_info)
        response = app.post("/fax", data=valid_fax_info)
        response_body = json.loads(response.data.decode())
        assert response.status_code == 200
        assert response_body['status'] == 'Success!'
        assert isinstance(response_body['fax_id'], int)

    @pytest.mark.parametrize("removed_field", valid_fax_info().keys())
    def test_invalid_call_missing_important_data(
        self, removed_field, app, valid_fax_info):
            del valid_fax_info[removed_field]
            valid_fax_info = json.dumps(valid_fax_info)
            response = app.post("/fax", data=valid_fax_info)
            response_body = json.loads(response.data.decode())
            assert response.status_code == 400
            assert response_body['status'] == "Failed"

    @patch('fax.resources.build_faxio_request')
    def test_phaxio_failure(
        self, mock_build_function, app, valid_fax_info, valid_info_dict
    ):
        valid_fax_info = json.dumps(valid_fax_info)
        valid_info_dict['header_text'] = ('This is going to be super long'
                                          'so that I am able to test a failure'
                                          '. Header text cannot be as long as '
                                          'I am making this. Therefore, I am '
                                          'unsure what will happen but I am '
                                          'hoping the failure will be handled')
        mock_build_function.return_value = valid_info_dict
        response = app.post("/fax", data=valid_fax_info)
        response_body = json.loads(response.data.decode())
        print(response_body)
