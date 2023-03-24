"""Guess the number game. Provide number and try to guess the number"""
from random import randint


def game(number_) -> bool:
    """

    :param number_: Drawn number
    :return: bool -> Do player win = True,
                            not yet = False
    """
    try:
        guessed_number = float(input("Guess the number: "))
    except ValueError:
        print("It's not a number!")
        return False

    if guessed_number < number_:
        print("Too small!")
        return False
    if guessed_number > number_:
        print("Too big!")
        return False

    print("You win!")
    return True


def main() -> None:
    """
    Draw number.
    Open loop until the player guesses the number
    :return: None -> It's just main
    """
    lucky_number = randint(1, 100)
    while not game(lucky_number):
        pass


main()
