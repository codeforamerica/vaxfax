# content of conftest.py
import pytest
import os
from local_phaxio.utils import (
    api,
)

@pytest.fixture(autouse=True)
def setup_of_environment_variables():
    api.api_key = "4c9ab7cf10c609b0943deec6793825e89fb19a4c"
    api.api_secret = "c41b4eff5dce1573b3d925214de66b24ee73b83e"
    api.health_fax_number = "415-789-4127"
    return
#
# @pytest.fixture(autouse=True)
# def setup_of_environment_variables(request):
#     phaxio_api_key    = os.environ.get('PHAXIO_API_KEY', "")
#     phaxio_api_secret = os.environ.get('PHAXIO_API_SECRET', "")
#     health_fax_number = os.environ.get('HEALTH_FAX_NUMBER', "")
#     os.environ['PHAXIO_API_KEY']    = "4c9ab7cf10c609b0943deec6793825e89fb19a4c"
#     os.environ['PHAXIO_API_SECRET'] = "c41b4eff5dce1573b3d925214de66b24ee73b83e"
#     os.environ['HEALTH_FAX_NUMBER'] = "415-789-4127"
#     def reset_to_orig_api_keys():
#         os.environ['PHAXIO_API_KEY']    = phaxio_api_key
#         os.environ['PHAXIO_API_SECRET'] = phaxio_api_secret
#         os.environ['HEALTH_FAX_NUMBER'] = health_fax_number
#     request.addfinalizer(reset_to_orig_api_keys)
#     return None
