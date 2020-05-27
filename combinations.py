def get_number_of_eyes_for_number(roll, number):
    return [roll[key] for key in roll].count(number) * number


def get_aces(roll):
    return get_number_of_eyes_for_number(roll, 1)


def get_twos(roll):
    return get_number_of_eyes_for_number(roll, 2)


def get_threes(roll):
    return get_number_of_eyes_for_number(roll, 3)


def get_fours(roll):
    return get_number_of_eyes_for_number(roll, 4)


def get_fives(roll):
    return get_number_of_eyes_for_number(roll, 5)


def get_sixes(roll):
    return get_number_of_eyes_for_number(roll, 6)


def get_three_of_a_kind(roll):
    return
