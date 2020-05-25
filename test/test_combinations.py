import pytest
import combinations


def test_get_aces():

    roll = {0: 1, 1: 2, 2: 6, 3: 1, 4: 1}

    assert combinations.get_aces(roll) == 3


def test_get_twos():

    roll = {0: 2, 1: 2, 2: 2, 3: 2, 4: 2}

    assert combinations.get_twos(roll) == 10


def test_get_threes():

    roll = {0: 2, 1: 5, 2: 4, 3: 6, 4: 6}

    assert combinations.get_threes(roll) == 0


def test_get_fours():

    roll = {0: 4, 1: 5, 2: 4, 3: 6, 4: 6}

    assert combinations.get_fours(roll) == 8


def test_get_fives():

    roll = {0: 2, 1: 5, 2: 4, 3: 6, 4: 6}

    assert combinations.get_fives(roll) == 5


def test_get_sixes():

    roll = {0: 2, 1: 5, 2: 4, 3: 6, 4: 6}

    assert combinations.get_sixes(roll) == 12
