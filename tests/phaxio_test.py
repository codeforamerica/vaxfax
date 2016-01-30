import pytest
from local_phaxio.utils import (
    create_faxio_string,
    create_header_string,
    build_string_from_dict,
    get_key_from_tuple_list,
    make_faxio_request,
    build_faxio_request,
)
import collections
import random


class TestMethod__create_faxio_string:
    def test_input_requires_dictionary(self):
        with pytest.raises(ValueError):
            string_body = create_faxio_string({})

    @pytest.mark.parametrize("removed_field", [
        "child_name", "child_dob", "school_district", "school_name",
        "school_fax", "requestor_name", "requestor_contact"
    ])
    def test_required_keys(self, removed_field, valid_fax_info):
        del valid_fax_info[removed_field]
        with pytest.raises(ValueError):
            string_body = create_faxio_string(valid_fax_info)

    def test_valid_format_is_returned(self, valid_fax_info):
        valid_return = ("Child Name: Banjo Edelman\nChild DOB: 08/01/2010\n"
                        "School District: KCP 33\nSchool Name: Faxon Elementary "
                        "School\nSchool Fax: 555-555-5556\nRequestor Name: Rachel "
                        "Edelman\nRequestor Contact Info: 555-555-5555")
        method_return = create_faxio_string(valid_fax_info)
        assert valid_return == method_return

class TestMethod__build_string_from_dict:
    def test_string_input_errors(self):
        with pytest.raises(Exception):
            build_string_from_dict("hello: World")

    def test_ordered_dict_input(self):
        tuple_list = [('hello', 'World'), ('goodbye', 'else')]
        input_dict = collections.OrderedDict(tuple_list)
        output_string = build_string_from_dict(input_dict)
        assert "hello: World" in output_string
        assert "goodbye: else" in output_string

    def test_valid_input_dict_no_map(self):
        input_dict = {"hello": "World", "goodbye": "else"}
        output_string = build_string_from_dict(input_dict)
        assert "hello: World" in output_string
        assert "goodbye: else" in output_string

    def test_valid_input_dict_with_string_map(self):
        input_dict = {"hello": "World", "goodbye": "else"}
        input_string_map = [("hello", "HI"), ("goodbye", "SEEYA")]
        output_string = build_string_from_dict(input_dict, input_string_map)
        assert "HI: World" in output_string
        assert "SEEYA: else" in output_string

    def test_valid_input_dict_with_incomplete_string_map(self):
        input_dict = {"hello": "World", "goodbye": "else"}
        input_string_map = [("hello", "HI")]
        output_string = build_string_from_dict(input_dict, input_string_map)
        assert output_string == "HI: World\ngoodbye: else"


    def test_valid_input_dict_with_too_many_string_map_values(self):
        input_dict = {"hello": "World", "goodbye": "else"}
        input_string_map = input_string_map = [
            ("hello", "HI"), ("goodbye", "SEEYA"), ("whatever", "else")
        ]
        output_string = build_string_from_dict(input_dict, input_string_map)
        assert output_string == "HI: World\nSEEYA: else"


class TestMethod__get_key_from_tuple_list:
    def test_it_finds_the_first_instance_of_the_key(self):
        tuple_list = [('hello', 'world'), ('goodbye', 'KEY')]
        key = 'goodbye'
        value = get_key_from_tuple_list(key, tuple_list)
        assert isinstance(value, tuple)
        assert len(value) == 2
        assert value[0] == 'KEY'
        assert value[1] == 1

    def test_it_returns_the_value_with_index(self):
        tuple_list = [('hello', 'world'), ('goodbye', 'KEY')]
        key = 'hello'
        value = get_key_from_tuple_list(key, tuple_list)
        assert value[0] == 'world'
        assert value[1] == 0

    def test_it_uses_the_key_value_if_no_key_is_found(self):
        tuple_list = [('hello', 'world'), ('goodbye', 'KEY')]
        key = 'notthere'
        value = get_key_from_tuple_list(key, tuple_list)
        assert value[0] == 'notthere'
        assert value[1] == -1

    def test_unfound_value_is_gives_negative_one_index(self):
        tuple_list = [('hello', 'world'), ('goodbye', 'KEY')]
        key = 'unfound'
        value = get_key_from_tuple_list(key, tuple_list)
        assert value[0] == 'unfound'
        assert value[1] == -1

    def test_it_immediately_exits_when_key_is_found(self):
        tuple_list = [('hello', 'world'), ()]
        key = 'hello'
        value = get_key_from_tuple_list(key, tuple_list)
        assert value[0] == 'world'
        assert value[1] == 0

    def test_raises_error_with_invalid_tuple_in_list(self):
        tuple_list = [('hello', 'world'), (), ('something', 'wonthit')]
        key = 'something'
        with pytest.raises(Exception):
            get_key_from_tuple_list(key, tuple_list)


class TestSimpleUtils:
    def test_create_header_text(self):
        string_body = create_header_string()
        assert ("Youth Application for Vaccination Records") in string_body


class TestMethod__make_faxio_request:
    def test_it_makes_a_valid_call(self, valid_info_dict):
        info_dict = valid_info_dict
        response = make_faxio_request(info_dict)
        assert response['success'] == True
        assert isinstance(response['faxId'], int)


class TestMethod__build_faxio_request:
    def test_it_builds_valid_dictionary(self, valid_fax_info):
        fax_info_dict = valid_fax_info
        faxio_request_dict = build_faxio_request(fax_info_dict)
        assert faxio_request_dict['string_data'] == (
            "This is a fax generated by the Kansas City, "
            "Missouri Health Department's FaxVax Service. "
            "If you have any questions fulfiling it, "
            "please contact us at __________.\n\n"
            "Request Information:\n"
            "Child Name: Banjo Edelman\n"
            "Child DOB: 08/01/2010\nSchool District: "
            "KCP 33\nSchool Name: Faxon Elementary "
            "School\nSchool Fax: 555-555-5556\n"
            "Requestor Name: Rachel Edelman\nRequestor "
            "Contact Info: 555-555-5555"
        )
        faxio_request_dict['header_text'] == (
            "Youth Application for Vaccination Records"
        )
        assert isinstance(faxio_request_dict['tag[request_id]'], str)



# test_fail	string	When using a test API key, this will simulate a sending failure at Phaxio.
# The contents of this parameter should be one of the Phaxio error types which will dictate how
# the fax will "fail".
