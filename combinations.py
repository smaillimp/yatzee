import copy

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


def get_number_of_kind_resursively(roll, number_of_kinds, number_of_kind, eyes):
    recursive_n_of_kinds = remove_element(number_of_kinds, number_of_kind)
    recurisve_roll = remove_dice_from_roll(roll, [eyes] * number_of_kind)
    return get_points_for_number_of_a_kinds(recurisve_roll, recursive_n_of_kinds)


def remove_element(number_of_kinds, number_of_kind):
    recursive_n_of_kinds = copy.copy(number_of_kinds)
    recursive_n_of_kinds.remove(number_of_kind)
    return recursive_n_of_kinds


def get_points_for_number_of_a_kinds(roll, number_of_kinds):
    number_of_kind = sorted(number_of_kinds)[-1]
    for eyes in range(6, 0, -1):
        number_of_hits = get_number_of_hits_for_number(roll, eyes)
        if number_of_hits >= number_of_kind:
            points = number_of_kind * eyes
            if len(number_of_kinds) > 1:
                recursive_points = get_number_of_kind_resursively(
                    roll, number_of_kinds, number_of_kind, eyes
                )
                return points + recursive_points if recursive_points != 0 else 0
            else:
                return points
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
    return get_points_for_number_of_a_kinds(roll, [2])


def get_three_of_a_kind(roll):
    return get_points_for_number_of_a_kinds(roll, [3])


def get_four_of_a_kind(roll):
    return get_points_for_number_of_a_kinds(roll, [4])


def get_yatzee(roll):
    return 50 if get_points_for_number_of_a_kinds(roll, [5]) != 0 else 0


def get_two_pairs(roll):
    return get_points_for_number_of_a_kinds(roll, [2, 2])


def get_full_house(roll):
    return 25 if get_points_for_number_of_a_kinds(roll, [3, 2]) != 0 else 0
