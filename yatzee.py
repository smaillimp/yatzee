import dice
import user


def play_round(player):
    print("It is {}'s turn to roll the dice.".format(player))
    rolls = list()
    for i in range(5):
        rolls.append(dice.roll_dice())
    print(rolls)


if __name__ == "__main__":
    players = user.get_player_names()
    for player in players:
        play_round(player)
