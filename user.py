def game_input(question, input_type):
    value = input("{} ".format(question))
    return_value = input_type(value)
    return return_value


if __name__ == "__main__":
    number_of_players = game_input("How many players will play the game?", int)
    print(number_of_players)
