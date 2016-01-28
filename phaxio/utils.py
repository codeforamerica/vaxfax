

def create_header_string():
    return ("This is a fax generated by the Kansas City, "
            "Missouri Health Department's FaxVax Service. "
            "If you have any questions fulfiling it, "
            "please contact us at __________.")

def get_key_from_tuple_list(key: str, string_map: list=[]) -> tuple:
    return_tuple = next(
        (
            (value[1], index)
            for index, value
            in enumerate(string_map)
            if value[0]==key
        ),
        None
    )
    if return_tuple is None:
        return_tuple = (key, -1)
    return return_tuple


def build_string_from_dict(input_data: dict, string_map: list=[]) -> str:
    ordered_list   = []
    unordered_list = []
    for key, value in input_data.items():
        key_tuple = get_key_from_tuple_list(key, string_map) + (value,)
        if key_tuple[1] is not -1:
            ordered_list.append(key_tuple)
        else:
            unordered_list.append(key_tuple)
    ordered_list = sorted(ordered_list, key=lambda x: x[1])
    final_list = ordered_list + unordered_list[::-1]
    final_string_list = ["{0}: {1}".format(item[0], item[2])
                         for item in final_list]
    final_string = "\n".join(final_string_list)
    return final_string


def create_faxio_string(input_data: dict) -> str:
    required_fields = [
    "child_name", "child_year", "child_month",
    "child_day", "school_district", "school_name",
    "school_fax", "requestor_name", "requestor_phone"
    ]
    missing_fields = [field for field in required_fields
                      if field not in input_data]
    if any(missing_fields):
        raise ValueError("The input was missing the following fields: {0}"
            .format(missing_fields))
    ("Child's Name: {0}\nChild's DOB: {1}/{2}/{3}\n"
     "School District: {4}\nSchool Name: {5}\n"
     "School Fax: {6}\nRequestor Name: {7}\n"
     "Requestor Phone: {8}").format()
    return ''
