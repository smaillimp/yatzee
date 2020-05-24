import dice
import user
import helpers


def print_rolls_nicely(rolls):
    def format_roll(name, values):
        return "{: <10} {}".format(name, " | ".join([str(item) for item in values]))

    print(format_roll("Index", rolls.keys()))
    print(format_roll("Values", rolls.values()))


def play_round(player):
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
    user_input = helpers.game_input(
        "Would you like to roll again? Write 'yes' or 'no'\n>", input_type=str
    )
    if user_input == "yes":
        return True
    elif user_input == "no":
        return False
    else:
        return ask_user_if_he_wants_to_reroll()


def reroll(rolls):
    reroll = helpers.game_input(
        "Which dice do you want to roll again?", input_type=helpers.LIST_OF_INT
    )
    rerolls = roll_multiple_dice(len(reroll))
    print_rolls_nicely(rerolls)
    for i, dice_index in enumerate(reroll):
        rolls[dice_index] = rerolls[i]
    return rolls


def roll_multiple_dice(number_of_dice):
    rolls = dict()
    for i in range(number_of_dice):
        rolls[i] = dice.roll_dice()
    return rolls


if __name__ == "__main__":
    players = user.get_player_names()

    for player in players:
        play_round(player)
