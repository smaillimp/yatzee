import dice
import user
import helpers
import combinations


def get_welcome_message():
    """
    This function returns a welcome message.
    """
    return "Welcome to Yatzee by Smaillim and Andy!"


def print_rolls_nicely(rolls):
    """
    This function prints the rolls in a more understandable way.
    """

    def format_roll(name, values):
        """
        This function prints a line in a prefined way.
        """

        return "{: <10} {}".format(name, " | ".join([str(item) for item in values]))

    print(format_roll("Index", rolls.keys()))
    print(format_roll("Values", rolls.values()))


def print_possible_results(rolls, player_result):
    print("These are the options you have...")
    for bracket in combinations.playable_brackets:
        print(bracket)
        print_results_nicely(combinations.brackets[bracket], rolls, player_result)


def print_results_nicely(combs, rolls, player_result):
    playable_combinations = [
        combination
        for combination in combs
        if combination in combinations.get_selectable_combinations(player_result)
    ]
    for combination in playable_combinations:
        print(f"{combination: <{20}}{combs[combination](rolls)}")


def get_selected_combination(rolls, player_result):
    try:
        selected_combination = helpers.game_input(
            "which combination would you like to select?: ",
            input_type=str,
            allowed_values=combinations.get_selectable_combinations(player_result),
        )
        return selected_combination
    except RuntimeError as e:
        print(e)
        print("Please enter a valid combination.")
        return get_selected_combination(rolls, player_result)

    """
    1. ask player to input which combination he'd like to use.
    2. confirm that it actually is a valid combination
    3. display points for combination and ask for confimation.
    """
    pass


def play_round(player, player_result):
    """
    This function tells us which user should play and 
    how many times can roll the dices again.
    """
    print("It is {}'s turn to roll the dice.".format(player))
    rolls = roll_multiple_dice(5)
    print_rolls_nicely(rolls)
    print_possible_results(rolls, player_result)
    rerolls = 2
    for i in range(2):
        print("You can reroll {} times...".format(2 - i))
        if ask_user_if_he_wants_to_reroll():
            rolls = reroll(rolls)
            print_rolls_nicely(rolls)
            print_possible_results(rolls, player_result)
        else:
            break
    selected_combination = get_selected_combination(rolls, player_result)
    player_result = combinations.update_result(
        rolls, selected_combination, player_result
    )


def ask_user_if_he_wants_to_reroll():
    """
    This function asks the users if they want to roll the dices again.
    """
    try:
        user_input = helpers.game_input(
            "Would you like to roll again?",
            input_type=str,
            allowed_values=["yes", "no"],
        )
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
    except RuntimeError as e:
        print("Please write 'yes' or 'no'")
        return ask_user_if_he_wants_to_reroll()


def reroll(rolls):
    """
    This function asks users which dice they want to roll again.
    """
    try:
        reroll_dice = helpers.game_input(
            "Which dice do you want to roll again?",
            input_type=helpers.LIST_OF_INT,
            allowed_values=[0, 1, 2, 3, 4],
        )
    except (RuntimeError, ValueError) as e:
        print("Please write a valid number")
        return reroll(rolls)
    rerolls = roll_multiple_dice(len(reroll_dice))
    print_rolls_nicely(rerolls)
    for i, dice_index in enumerate(reroll_dice):
        rolls[dice_index] = rerolls[i]
    return rolls


def roll_multiple_dice(number_of_dice):
    """
    This function lets us roll several dices at the same time.
    """
    rolls = dict()
    for i in range(number_of_dice):
        rolls[i] = dice.roll_dice()
    return rolls


def print_results_for_all_players(player_result):
    line_fomat = "".join(["{: <20}"] * (1 + len(list(player_result.keys()))))
    print(line_fomat.format("", *list(player_result.keys())))
    player_0 = list(player_result.keys())[0]
    for bracket in player_result[player_0]:
        print(bracket)
        for combination in player_result[player_0][bracket]:
            print(
                line_fomat.format(
                    combination,
                    *[
                        str(player_result[player][bracket][combination])
                        for player in player_result
                    ],
                )
            )
        print("\n")
    print(
        line_fomat.format(
            "Sum",
            *[combinations.get_sum(player_result[player]) for player in player_result],
        )
    )


if __name__ == "__main__":

    print(get_welcome_message())

    players = user.get_player_names()
    player_results = {player: combinations.get_empty_results() for player in players}

    while (
        len(
            combinations.get_selectable_combinations(
                player_results[list(player_results.keys())[0]]
            )
        )
        > 0
    ):
        for player in player_results:
            print("\n\n\n")
            print_results_for_all_players(player_results)
            print("\n\n\n")
            play_round(player, player_results[player])

