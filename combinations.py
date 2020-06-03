# Aces, Twos, Threes, Fours, fives and Sixes


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


# Pair, Trio, Quad and Yatzee


def get_number_of_a_kind(roll, number, recursive=0):
    number_of_hits = dict()
    for i in range(6, 0, -1):
        number_of_hits[i] = get_number_of_hits_for_number(roll, i)
        if number_of_hits[i] >= number:
            if number == 5:
                return 50
            if recursive > 0:
                return number * i + get_number_of_a_kind(
                    remove_dice_from_roll(roll, [i] * number),
                    number,
                    recursive=recursive - 1,
                )
            else:
                return number * i
    else:
        return 0


def remove_dice_from_roll(roll, dice_to_remove):
    values = list(roll.values())
    for eyes in dice_to_remove:
        if eyes in values:
            values.remove(eyes)
        else:
            raise ValueError("Value not in list and therefore can not be removed.")
    return {index: value for index, value in enumerate(values)}


def get_pairs(roll):
    return get_number_of_a_kind(roll, 2)


def get_three_of_a_kind(roll):
    return get_number_of_a_kind(roll, 3)


def get_four_of_a_kind(roll):
    return get_number_of_a_kind(roll, 4)


def get_yatzee(roll):
    return get_number_of_a_kind(roll, 5)


def get_two_pairs(roll):
    return get_number_of_a_kind(roll, number=2, recursive=1)
