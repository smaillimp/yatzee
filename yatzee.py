import dice
import user
import helpers
import combinations

__author__ = "Smaillim and Andy"

REROLLS = 2
NUMBER_OF_DICE = 5


def print_welcome_message(authors=__author__):
    """
    This function returns a welcome message.
    """
    print(f"Welcome to Yatzee by {authors}!")


def print_vertical_spaces(number_of_new_lines=3):
    print("\n" * number_of_new_lines)


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


def print_possible_results(rolls, players):
    print("These are the options you have...")
    for bracket in combinations.playable_brackets:
        print(bracket)
        print_results_nicely(combinations.brackets[bracket], rolls, players)


def print_results_nicely(combs, rolls, players):
    playable_combinations = [
        combination
        for combination in combs
        if combination in combinations.get_selectable_combinations(players)
    ]
    for combination in playable_combinations:
        print(f"{combination: <{20}}{combs[combination](rolls)}")


def print_end_scores(players):
    scores = get_scores(players)
    print_vertical_spaces()
    for rank, (player, score) in enumerate(scores):
        print(f"{rank+1}. rank with a score of {score}: {player}")


def get_scores(players):
    scores = list()
    for player in players:
        scores.append([player, combinations.get_sum(players[player])])
    sorted_scores = sorted(scores, key=lambda x: x[1])
    return sorted_scores


def get_selected_combination(rolls, players):
    try:
        selected_combination = helpers.game_input(
            "which combination would you like to select?: ",
            input_type=str,
            allowed_values=combinations.get_selectable_combinations(players),
        )
        return selected_combination
    except RuntimeError as e:
        print(e)
        print("Please enter a valid combination.")
        return get_selected_combination(rolls, players)


def print_rolls_and_possible_results(rolls, players):
    print_rolls_nicely(rolls)
    print_possible_results(rolls, players)


def roll_a_round(players):
    rolls = roll_multiple_dice(NUMBER_OF_DICE)
    print_rolls_and_possible_results(rolls, players)
    for i in range(REROLLS):
        print("You can reroll {} times...".format(REROLLS - i))
        if ask_user_if_he_wants_to_reroll():
            rolls = reroll(rolls)
            print_rolls_and_possible_results(rolls, players)
        else:
            break
    return rolls


def play_round(player, players):
    """
    This function tells us which user should play and 
    how many times can roll the dices again.
    """
    print("It is {}'s turn to roll the dice.".format(player))
    rolls = roll_a_round(players)
    selected_combination = get_selected_combination(rolls, players)
    players = combinations.update_result(rolls, selected_combination, players)


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
    except RuntimeError:
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
    except (RuntimeError, ValueError):
        print("Please write a valid number")
        return reroll(rolls)
    rerolls = roll_multiple_dice(len(reroll_dice))
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


def get_line_format(players):
    return "".join(["{: <20}"] * (1 + len(list(players.keys()))))


def print_score_line(*args, line_format=""):
    print(line_format.format(*args))


def print_scores(players):
    line_format = get_line_format(players)
    print_score_line("", *list(players.keys()), line_format=line_format)
    player_0 = list(players.keys())[0]
    for bracket in players[player_0]:
        print(bracket)
        for combination in players[player_0][bracket]:
            print_score_line(
                combination,
                *get_score_for_combination(bracket, combination, players),
                line_format=line_format,
            )
        print_vertical_spaces(number_of_new_lines=1)
    print_score_line("Sum", *get_sum_for_players(players), line_format=line_format)


def get_score_for_combination(bracket, combination, players):
    return [str(players[player][bracket][combination]) for player in players]


def get_sum_for_players(players):
    return [combinations.get_sum(players[player]) for player in players]


def set_up_players():
    return {
        player: combinations.get_empty_results() for player in user.get_player_names()
    }


def get_numbers_of_rounds_to_play(players):
    return len(
        combinations.get_selectable_combinations(players[list(players.keys())[0]])
    )


def play_game(players):
    while get_numbers_of_rounds_to_play(players) > 0:
        for player in players:
            print_vertical_spaces()
            print_scores(players)
            print_vertical_spaces()
            play_round(player, players[player])


if __name__ == "__main__":
    print_welcome_message()
    players = set_up_players()
    play_game(players)
    print_end_scores(players)

