import pytest
import mock
import builtins

import yatzee


def test_ask_user_if_he_wants_to_reroll_yes():
    with mock.patch.object(builtins, "input", lambda input_str: "yes"):
        assert yatzee.ask_user_if_he_wants_to_reroll() == True


def test_ask_user_if_he_wants_to_reroll_no():
    with mock.patch.object(builtins, "input", lambda input_str: "no"):
        assert yatzee.ask_user_if_he_wants_to_reroll() == False


def test_get_welcome_message():
    assert yatzee.get_welcome_message() == "Welcome to Yatzee by Smaillim and Andy!"
