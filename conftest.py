# content of conftest.py
import pytest
import os
from local_phaxio.utils import (
    api,
)
import random


@pytest.fixture(autouse=True)
def setup_of_environment_variables():
    api.api_key = "4c9ab7cf10c609b0943deec6793825e89fb19a4c"
    api.api_secret = "c41b4eff5dce1573b3d925214de66b24ee73b83e"
    api.health_fax_number = "415-789-4127"
    return


@pytest.fixture()
def valid_fax_info():
    return {
        "child_name": "Banjo Edelman",
        "child_dob": "08/01/2010",
        "school_district": "KCP 33",
        "school_name": "Faxon Elementary School",
        "school_fax": "555-555-5556",
        "requestor_name": "Rachel Edelman",
        "requestor_contact": "555-555-5555"
    }


@pytest.fixture()
def valid_info_dict():
    info_dict = {}
    info_dict['string_data'] = ("Child Name: Banjo Edelman\n"
                                "Child DOB: 08/01/2010\nSchool District: "
                                "KCP 33\nSchool Name: Faxon Elementary "
                                "School\nSchool Fax: 555-555-5556\n"
                                "Requestor Name: Rachel Edelman\nRequestor "
                                "Contact Info: 555-555-5555")
    info_dict['header_text'] = ("Youth Application for Vaccination Records")
    info_dict['tag[request_id]'] = str(random.randint(1, 1000))
    return info_dict


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
