from hangman_utils import HANGMAN_WORDS, HANGMAN_PICS
import random

"""
ISSUES:

Elizabeth, add 2-3 features (use your imagination!) and fix the bug

OPEN BUGS:

* user can guess a number

OPEN FEATURE/ENHANCEMENTS:

* when starting, have game pick from multiple word banks
* allow phrases as well as single words, like "code rocks"
* offer multiple hints (maybe at 3 wrong guesses)
* offer to fill in one letter for a user at wrong guess X

CLOSED ISSUES:

FIXED!! can make same guess twice
FIXED!! can guess more than a letter
FIXED!! blank inputs allowed
FIXED!! add hint for almost losers!

"""


def display_board(display_word, wrong_guesses):
    print()
    print(HANGMAN_PICS[wrong_guesses])
    print()
    print(' '.join(display_word))
    print()


def get_guess(guesses):
    while True:
        guess = input("Choose a letter: ").upper()

        # check guess
        if len(guess) == 0:
            print("Cannot have blank letter")
        elif len(guess) > 1:
            print("Too long! Only choose a letter")
        elif guess in guesses:
            print("You already guessed this!")
        else:
            return guess


def show_hint():
    show_hint = input("would you like a hint [Y/n]: ")
    if show_hint in ['Y', 'y', 'yes']:
        print("hint: animal")
    else:
        pass


def play_game():

    game_over = False
    hint_shown = False
    wrong_guesses = 0
    guesses = []

    # choose a word
    word = random.choice(HANGMAN_WORDS).upper()

    check_word = list(word)
    print(check_word)

    display_word = []  # this is the board

    for i in range(len(check_word)):
        display_word.append('_')

    # set up the board

    # game loop!
    while not game_over:
        display_board(display_word, wrong_guesses)

        # choose letter
        guess = get_guess(guesses)
        guesses.append(guess)

        # check to see if correct
        if guess in check_word:
            # it's here! add the letter to the board if they are there
            for index in range(len(check_word)):
                if guess == check_word[index]:
                    display_word[index] = guess
        else:
            # it's wrong!!!
            wrong_guesses += 1

        # check to see if game over
        if '_' not in display_word:
            # game over!
            game_over = True
            display_board(check_word, wrong_guesses)
            print("Game over you win, you're a champion!")

        if wrong_guesses == 5:
            if not hint_shown:
                show_hint()
                hint_shown = True
        if wrong_guesses == 6:
            game_over = True
            display_board(check_word, wrong_guesses)
            print("Game over you lose, sucker")


if __name__ == "__main__":
    play_game()
