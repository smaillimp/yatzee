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


def test_get_three_of_a_kind_with_3_2s():

    roll = {0: 2, 1: 2, 2: 2, 3: 3, 4: 4}

    assert combinations.get_three_of_a_kind(roll) == 6


def test_get_three_of_a_kind_with_3_4s():

    roll = {0: 3, 1: 4, 2: 4, 3: 5, 4: 4}

    assert combinations.get_three_of_a_kind(roll) == 12


def test_get_three_of_a_kind_with_no_triple():

    roll = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4}

    assert combinations.get_three_of_a_kind(roll) == 0


def test_get_four_of_a_kind_with_4_6s():

    roll = {0: 6, 1: 6, 2: 6, 3: 3, 4: 6}

    assert combinations.get_four_of_a_kind(roll) == 24


def test_get_four_of_a_kind_with_no_quadruple():

    roll = {0: 6, 1: 6, 2: 2, 3: 3, 4: 6}

    assert combinations.get_four_of_a_kind(roll) == 0


def test_get_pairs_of_6():

    roll = {0: 6, 1: 6, 2: 2, 3: 3, 4: 1}

    assert combinations.get_pairs(roll) == 12


def test_get_pairs_with_two_pairs():

    roll = {0: 6, 1: 6, 2: 5, 3: 5, 4: 1}

    assert combinations.get_pairs(roll) == 12


def test_get_pairs_with_no_pair():

    roll = {0: 6, 1: 5, 2: 4, 3: 3, 4: 1}

    assert combinations.get_pairs(roll) == 0


def test_get_pairs_with_yatzee():

    roll = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}

    assert combinations.get_pairs(roll) == 2


def test_get_yatzee():

    roll = {0: 6, 1: 6, 2: 6, 3: 6, 4: 6}

    assert combinations.get_yatzee(roll) == 50


def test_get_just_two_pairs():

    roll = {0: 6, 1: 6, 2: 5, 3: 5, 4: 2}

    assert combinations.get_two_pairs(roll) == 22


def test_get_two_pairs_in_a_yatzee():

    roll = {0: 6, 1: 6, 2: 6, 3: 6, 4: 6}

    assert combinations.get_two_pairs_in_a_yatzee(roll) == 24


def test_get_two_pairs_in_four_of_a_kind():

    roll = {0: 4, 1: 4, 2: 4, 3: 4, 4: 6}

    assert combinations.get_two_pairs_in_four_of_a_kind(roll) == 16
