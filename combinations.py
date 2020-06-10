# Aces, Twos, Threes, Fours, fives and Sixes


def get_number_of_eyes_for_number(roll, number):
    return get_number_of_hits_for_number(roll, number) * number


def get_number_of_hits_for_number(roll, number):
    return [roll[key] for key in roll].count(number)

def get_aces(roll):
    """
    This function returns the aces we got.
    """
    return get_number_of_eyes_for_number(roll, 1)


def get_twos(roll):
    """
    This function returns the twos we got.
    """
    return get_number_of_eyes_for_number(roll, 2)


def get_threes(roll):
    """
    This function returns the threes we got.
    """
    return get_number_of_eyes_for_number(roll, 3)


def get_fours(roll):
    """
    This function returns the fours we got.
    """
    return get_number_of_eyes_for_number(roll, 4)


def get_fives(roll):
    """
    This function returns the fives we got.
    """
    return get_number_of_eyes_for_number(roll, 5)


def get_sixes(roll):
    """
    This function returns the sixes we got.
    """
    return get_number_of_eyes_for_number(roll, 6)


def get_points_for_number_of_a_kinds(roll, number_of_kinds, points=0):
    number_of_kind = sorted(number_of_kinds)[-1]
    number_of_kinds.remove(number_of_kind)
    points = get_points_for_number_of_a_kind(
        roll, number_of_kind, number_of_kinds, points
    )
    return points


def get_points_for_number_of_a_kind(roll, number_of_kind, number_of_kinds, points):
    for eyes in range(6, 0, -1):
        number_of_hits = get_number_of_hits_for_number(roll, eyes)
        if number_of_hits >= number_of_kind:
            points += number_of_kind * eyes
            if len(number_of_kinds) > 0:
                points = get_points_for_number_of_a_kinds(
                    remove_dice_from_roll(roll, [eyes] * number_of_kind),
                    number_of_kinds,
                    points,
                )
            break
    else:
        points = 0
    return points


def remove_dice_from_roll(roll, dice_to_remove):
    """
    This function remove the dice we got in a round if we got an existing combination.
    """
    values = list(roll.values())
    for eyes in dice_to_remove:
        if eyes in values:
            values.remove(eyes)
        else:
            raise ValueError("Value not in list and therefore can not be removed.")
    return {index: value for index, value in enumerate(values)}


def get_pairs(roll):
    """
    This function returns two of the same kind/ a pair.
    """
    return get_points_for_number_of_a_kinds(roll, [2])


def get_three_of_a_kind(roll):
    """
    This function returns three of the same kind.
    """
    return get_points_for_number_of_a_kinds(roll, [3])


def get_four_of_a_kind(roll):
    """
    This function returns five of the same kind
    """
    return get_points_for_number_of_a_kinds(roll, [4])


def get_yatzee(roll):
    """
    This function returns four of the same kind.
    """
    return 50 if get_points_for_number_of_a_kinds(roll, [5]) != 0 else 0


def get_two_pairs(roll):
    """
    This function returns two pairs.
    """
    return get_points_for_number_of_a_kinds(roll, [2, 2])


def get_full_house(roll):
    """
    This function returs 25 if we have three of a kind and a pair.
    """
    return 25 if get_points_for_number_of_a_kinds(roll, [3, 2]) != 0 else 0


def get_small_straight(roll):
    return 30 if


def get_large_straight(roll):
    retur 40 if 

def sort_dices_from_roll():
    