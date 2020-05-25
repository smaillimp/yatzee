import pytest
import dice


def test_roll_dice_in_range():
    assert 1 <= dice.roll_dice() <= 6
