import helpers


def get_number_of_players():
    """
    This function querries the player how many people will play.
    """
    try:
        number_of_players = helpers.game_input(
            "How many players will play the game?", input_type=int
        )
        return number_of_players
    except ValueError as e:
        print("Please enter a valid number")
        return get_number_of_players()


def get_player_names():
    """
    This function asks how many players will play the game and
    what their names are.
    """

    number_of_players = get_number_of_players()
    print(number_of_players)
    players = list()
    for i in range(number_of_players):
        player_name = helpers.game_input("What is player {}'s name?".format(i + 1))
        players.append(player_name)
    print(players)
    return players


if __name__ == "__main__":
    get_player_names()
