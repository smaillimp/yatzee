import helpers


def get_player_names():
    """
    This function asks how many players will play the game and
    what are their names.
    """
    number_of_players = helpers.game_input(
        "How many players will play the game?", input_type=int
    )
    print(number_of_players)
    players = list()
    for i in range(number_of_players):
        player_name = helpers.game_input("What is player {}'s name?".format(i + 1))
        players.append(player_name)
    print(players)
    return players


if __name__ == "__main__":
    get_player_names()
