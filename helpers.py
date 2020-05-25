class _SpecialDataType:
    @staticmethod
    def convert():
        pass

    @staticmethod
    def check_allowed_values():
        pass


class _ListOfInt(_SpecialDataType):
    @staticmethod
    def convert(value):
        return [int(v) for v in value.split()]

    @staticmethod
    def check_allowed_values(value, allowed_values):
        for item in value:
            check_in_list(item, allowed_values)


LIST_OF_INT = _ListOfInt


def game_input(question, input_type=None, allowed_values=None):
    """
    This function gets input from the console.
    Optionally, the function converts the value into a desired type and runs checks.
    """

    value = input("{} ".format(question))
    if input_type is None:
        return_value = value
    elif issubclass(input_type, _SpecialDataType):
        return_value = input_type.convert(value)
    else:
        return_value = input_type(value)
    if allowed_values is not None:
        check_allowed_values(return_value, input_type, allowed_values)
    return return_value


def check_allowed_values(return_value, input_type, allowed_values):
    if issubclass(input_type, _SpecialDataType):
        input_type.check_allowed_values(return_value, allowed_values)
    else:
        check_in_list(return_value, allowed_values)


def check_in_list(value, allowed_values):
    if value not in allowed_values:
        raise RuntimeError("{} is not in {}.".format(value, allowed_values))
