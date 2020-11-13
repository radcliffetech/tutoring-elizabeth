from hangman_utils import HANGMAN_PICS, HANGMAN_WORDS
import random


def get_guess(choices):
    """Get a guess"""
    while True:
        guess = input("Guess a letter: ").upper()
        if guess in choices:
            print("you've already guessed this. Try again")
        else:
            return guess


def show_board(count_wrong_guesses, word_display):
    """Show the game board"""
    print(count_wrong_guesses, "wrong guesses")
    print("")
    print(HANGMAN_PICS[count_wrong_guesses])
    print("")
    print(' '.join(word_display))
    print("")


def play_game():

    game_over = False
    max_count_wrong_guesses = len(HANGMAN_PICS) - 1
    count_wrong_guesses = 0
    guesses = []
    word_display = []

    # choose a word
    word = random.choice(HANGMAN_WORDS).upper()
    # construct the guess list
    word_split = list(word)

    # set up the word for display
    for char in word_split:
        word_display.append('_')

    # main game loop
    while not game_over:
        show_board(count_wrong_guesses, word_display)

        # get an input and see if it's right. If not, it's a wrong guess
        guess = get_guess(guesses)

        # check to see if our guess is correct
        if guess in word_split:
            # we got it right! update
            for index in range(len(word_split)):
                if word[index] == guess:
                    word_display[index] = guess
        else:
            # wrong guess
            print("Nope!")
            guesses.append(guess)
            count_wrong_guesses += 1

        # check to see if we won!
        if '_' not in word_display:
            game_over = True
            show_board(count_wrong_guesses, word_display)
            print("You won!")
            print("")

        # check to see if the game is over
        elif count_wrong_guesses == max_count_wrong_guesses:
            game_over = True
            show_board(count_wrong_guesses, word_split)
            print("You lose. Game over!")
            print("")


if __name__ == "__main__":
    play_game()
