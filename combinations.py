def get_number_of_eyes_for_number(roll, number):
    return get_number_of_hits_for_number(roll, number) * number


def get_number_of_hits_for_number(roll, number):
    return [roll[key] for key in roll].count(number)


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
    number_of_hits = dict()
    for i in range(1, 7):
        number_of_hits[i] = get_number_of_hits_for_number(roll, i)
        if number_of_hits[i] == 3:
            return number_of_hits[i] * i
    else:
        return 0
