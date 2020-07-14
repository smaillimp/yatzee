import pytest
import helpers
import builtins
import types


def test_game_input_returns_int(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "22")
    expected_type = int
    return_value = helpers.game_input("What is 11+11?", expected_type)
    assert isinstance(
        return_value, expected_type
    ), "`game_input` did not return expected type {} but {}.".format(
        expected_type, return_type
    )


def test_game_input_returns_str(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "22")
    expected_type = str
    return_value = helpers.game_input("What is 11+11?", expected_type)
    assert isinstance(
        return_value, expected_type
    ), "`game_input` did not return expected type {} but {}.".format(
        expected_type, return_type
    )


def test_game_input_returns_str_default(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "22")
    expected_type = str
    return_value = helpers.game_input("What is 11+11?")
    assert isinstance(
        return_value, expected_type
    ), "`game_input` did not return expected type {} but {}.".format(
        expected_type, return_type
    )


def test_game_input_returns_list_of_int(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "2 2 4")
    expected_type = str
    return_value = helpers.game_input("Question?", helpers.LIST_OF_INT)
    assert isinstance(
        return_value, list
    ), "`game_input` did not return expected type {} but {}.".format(
        expected_type, return_type
    )
    for item in return_value:
        assert isinstance(item, int)


def test_value_in_allowed_values(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "123")
    with pytest.raises(RuntimeError):
        helpers.game_input(
            "Which dice do you want to roll again?",
            input_type=helpers.LIST_OF_INT,
            allowed_values=[0, 1, 2, 3, 4],
        )
