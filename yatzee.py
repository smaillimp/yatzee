import dice
import user
import helpers


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


def play_round(player):
    """
    This function tells us which user should play and 
    how many times can roll the dices again.
    """
    print("It is {}'s turn to roll the dice.".format(player))
    rolls = roll_multiple_dice(5)
    print_rolls_nicely(rolls)
    rerolls = 2
    for i in range(2):
        print("You can reroll {} times...".format(2 - i))
        if ask_user_if_he_wants_to_reroll():
            rolls = reroll(rolls)
            print_rolls_nicely(rolls)
        else:
            break


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
    except RuntimeError as e:
        print(e)
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
    players = user.get_player_names()

    for player in players:
        play_round(player)
