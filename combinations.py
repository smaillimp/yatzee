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
    This function returns four of the same kind
    """
    return get_points_for_number_of_a_kinds(roll, [4])


def get_yatzee(roll):
    """
    This function returns five of the same kind.
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


def get_big_straight(roll):
    return get_straights(roll, [2, 3, 4, 5, 6], 40)


def get_small_straight(roll):
    return get_straights(roll, [1, 2, 3, 4, 5], 30)


def get_straights(roll, straight, points):
    for e in straight:
        if not e in roll.values():
            return 0
    else:
        return points


def get_all_combinations():
    return list(upper_bracket_combinations.keys()) + list(
        lower_bracket_combinations.keys()
    )


def get_empty_results():
    return {
        bracket: {combination: None for combination in brackets[bracket]}
        for bracket in brackets
    }


def get_selectable_combinations(result):
    selectable = list()
    for bracket in playable_brackets:
        for combination in result[bracket]:
            if result[bracket][combination] is None:
                selectable.append(combination)
    return selectable


def get_bracket_by_combination_name(combination):
    for bracket in brackets:
        for comb in brackets[bracket]:
            if comb == combination:
                return bracket
    else:
        raise KeyError(f"{combination} is not a valid combination.")


def update_result(roll, combination, player_result):
    bracket = get_bracket_by_combination_name(combination)
    points = brackets[bracket][combination](roll)
    player_result[bracket][combination] = points
    player_result = check_and_apply_bonus(player_result)
    return player_result


def check_and_apply_bonus(player_result, threshold=63):
    if get_sum(player_result, brackets=["Upper Bracket"]) >= threshold:
        player_result["Middle Bracket"]["bonus"] = 35
    return player_result


def get_sum(player_result, brackets=None):
    points = 0
    if brackets is None:
        brackets = player_result.keys()
    for bracket in brackets:
        for combination in player_result[bracket]:
            cp = player_result[bracket][combination]
            points += cp if cp is not None else 0
    return points


upper_bracket_combinations = {
    "aces": get_aces,
    "twos": get_twos,
    "threes": get_threes,
    "fours": get_fours,
    "fives": get_fives,
    "sixes": get_sixes,
}

middle_bracket_combinations = {
    "bonus": None,
}

lower_bracket_combinations = {
    "pairs": get_pairs,
    "two pairs": get_two_pairs,
    "three of a kind": get_three_of_a_kind,
    "four of a kind": get_four_of_a_kind,
    "full house": get_full_house,
    "small straight": get_small_straight,
    "big straight": get_big_straight,
    "yatzee": get_yatzee,
}

playable_brackets = {
    "Upper Bracket": upper_bracket_combinations,
    "Lower Bracket": lower_bracket_combinations,
}

brackets = {
    "Upper Bracket": upper_bracket_combinations,
    "Middle Bracket": middle_bracket_combinations,
    "Lower Bracket": lower_bracket_combinations,
}
