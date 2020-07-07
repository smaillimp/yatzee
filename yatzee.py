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


def print_possible_results(rolls, spacing=20):
    print("These are the options you have...")
    ucombs = combinations.upper_bracket_combinations
    lcombs = combinations.lower_bracket_combinations
    print("Upper Bracket")
    print_results_nicely(ucombs, rolls)
    print()
    print("Lower Bracket")
    print_results_nicely(lcombs, rolls)


def print_results_nicely(var, rolls, spacing=20):
    for combination in var:
        print(f"{combination: <{spacing}}{var[combination](rolls): <{spacing}}")


def get_selected_combination(rolls):
    
    try:
        seletect_combination = helpers.game_input(
            "which combination would you like to select?: ", input_type=str,
             allowed_values = list(combinations.upper_bracket_combinations.keys())
              + list(combinations.lower_bracket_combinations.keys())
        )
        return combinations
    except RuntimeError as e:
        print(e)
        print("Please enter a valid combination.")
        return get_selected_combination(rolls)



    """
    1. ask player to input which combination he'd like to use.
    2. confirm that it actually is a valid combination
    3. display points for combination and ask for confimation.
    """
    pass


def play_round(player):
    """
    This function tells us which user should play and 
    how many times can roll the dices again.
    """
    print("It is {}'s turn to roll the dice.".format(player))
    rolls = roll_multiple_dice(5)
    print_rolls_nicely(rolls)
    print_possible_results(rolls)
    rerolls = 2
    for i in range(2):
        print("You can reroll {} times...".format(2 - i))
        if ask_user_if_he_wants_to_reroll():
            rolls = reroll(rolls)
            print_rolls_nicely(rolls)
            print_possible_results(rolls)
        else:
            break
    get_selected_combination(rolls)


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


if __name__ == "__main__":

    print(get_welcome_message())

    players = user.get_player_names()

    for player in players:
        play_round(player)
