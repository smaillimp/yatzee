import pytest
import builtins

import helpers
import user


def test_get_number_of_players(mocker):
    expected_result = 2
    mocker.patch.object(helpers, "game_input", lambda *args, **kw_args: expected_result)
    assert user.get_number_of_players() == expected_result


def test_get_player_names(mocker):
    expected_result = ["foo", "bar"]
    mocker.patch.object(user, "get_number_of_players", lambda: 2)
    mocker.patch.object(helpers, "game_input", side_effect=expected_result)
    assert user.get_player_names() == expected_result
