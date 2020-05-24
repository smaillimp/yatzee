LIST_OF_INT = "list_of_int"


def convert_to_list_of_int(value):
    return [int(v) for v in value.split()]


_SPECIAL_TYPES = {LIST_OF_INT: convert_to_list_of_int}


def game_input(question, input_type=None):
    value = input("{} ".format(question))
    if input_type is None:
        return_value = value
    elif input_type in _SPECIAL_TYPES:
        return_value = _SPECIAL_TYPES[input_type](value)
    else:
        return_value = input_type(value)
    return return_value
