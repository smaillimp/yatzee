import random


def roll_dice():
    """
This function rolls a dice and return a random result between 1 and 6.
    """
    return random.randint(1, 6)


if __name__ == "__main__":
    roll = roll_dice()
    print(roll)
