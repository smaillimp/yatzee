def game_input(question, input_type=None):
    value = input("{} ".format(question))
    return input_type(value) if input_type is not None else value


if __name__ == "__main__":
    number_of_players = game_input(
        "How many players will play the game?", input_type=int
    )
    print(number_of_players)
    players = list()
    for i in range(number_of_players):
        player_name = game_input("What is player {}'s name?".format(i + 1))
        players.append(player_name)
    print(players)
