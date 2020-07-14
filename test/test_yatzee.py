import pytest
import builtins

import helpers
import yatzee
import dice


def test_ask_user_if_he_wants_to_reroll_yes(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "yes")
    assert yatzee.ask_user_if_he_wants_to_reroll() == True


def test_ask_user_if_he_wants_to_reroll_no(mocker):
    mocker.patch.object(builtins, "input", lambda input_str: "no")
    assert yatzee.ask_user_if_he_wants_to_reroll() == False


def test_get_welcome_message(capsys):
    yatzee.print_welcome_message(authors="JJJ")
    captured = capsys.readouterr()
    assert captured.out == "Welcome to Yatzee by JJJ!\n"


@pytest.mark.parametrize("number_of_spaces", [1, 2, 3])
def test_print_vertical_spaces(number_of_spaces, capsys):
    yatzee.print_vertical_spaces(number_of_new_lines=number_of_spaces)
    captured = capsys.readouterr()
    assert captured.out == "\n" * (number_of_spaces + 1)


def test_reroll(mocker):
    rolls = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
    mocker.patch.object(yatzee, "roll_multiple_dice", lambda *args: {0: 3, 1: 4, 2: 5})
    mocker.patch.object(helpers, "game_input", lambda *args, **kw_args: [1, 2, 3])
    assert yatzee.reroll(rolls) == {0: 1, 1: 3, 2: 4, 3: 5, 4: 1}


@pytest.mark.parametrize("number_of_dice", [4, 5, 6])
def test_roll_multiple_dice(number_of_dice, mocker):
    patch = mocker.patch.object(dice, "roll_dice")
    yatzee.roll_multiple_dice(number_of_dice)
    assert patch.call_count == number_of_dice
