import pytest
import mock
import builtins

import user


# ToDo
def test_get_number_of_players():
    expected_result = 2
    with mock.patch.object(builtins, "input", lambda input_str: str(expected_result)):
        assert user.get_number_of_players() == expected_result
