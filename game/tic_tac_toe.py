"""

A refreshing game of tic tac toe!

"""

# 9 squares, 3x3 grid
# 2 playings
# 9 possible moves

board = {
    7: ' ', 8: ' ', 9: ' ',
    4: ' ', 5: ' ', 6: ' ',
    1: ' ', 2: ' ', 3: ' ',
}


def show_rules():
    # show the rules
    print("""

How to play: type in the number where you want your mark

7|8|9
-+-+-
4|5|6
-+-+-
1|2|3""")


def show_board(board):
    # do something!
    print()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print()


def play_game():
    # describe rules
    show_rules()

    playing_1 = 'X'
    playing_2 = 'O'

    playing = playing_1
    # TODO: randomly assign first playing!

    round = 1
    game_over = False
    winner = ''

    while not game_over:
        # loop
        print("round " + str(round))
        show_board(board)

        # get input
        move = int(input("It's your turn, " + playing + ". Choose a place: "))

        # check to see if move is valid!
        if board[move] == ' ':
            # this is a good move
            board[move] = playing
            round += 1
        else:
            # this is a bad move!
            print("That place is already filled.")
            continue

        # check to see if there's a winner!
        # check each possibility! (of 8)
        if board[7] == board[8] == board[9] != ' ':
            game_over = True
            winner = playing
        elif board[4] == board[5] == board[6] != ' ':
            game_over = True
            winner = playing
        elif board[1] == board[2] == board[3] != ' ':
            game_over = True
            winner = playing
        elif board[7] == board[4] == board[1] != ' ':
            game_over = True
            winner = playing
        elif board[8] == board[5] == board[2] != ' ':
            game_over = True
            winner = playing
        elif board[9] == board[6] == board[3] != ' ':
            game_over = True
            winner = playing
        elif board[7] == board[5] == board[3] != ' ':
            game_over = True
            winner = playing
        elif board[9] == board[5] == board[1] != ' ':
            game_over = True
            winner = playing

        if round == 10:
            game_over = True
            winner = "nobody. It is a Tie!"

        # game over! show winner or tie
        if game_over:
            show_board(board)
            print("Game over! Winner is " + winner)
        else:
            # end of turn! switch playings
            if playing_1 == playing:
                playing = playing_2
            else:
                playing = playing_1


if __name__ == "__main__":
    play_game()
