MAIN_BOARD = """   |   |  
___|___|___
   |   |   
___|___|___
   |   |  
   |   |    """

places = {"00": 1, "01": 5, "02": 9,
          "10": 24, "11": 2, "12": 32,
          "20": 48, "21": 52, "22": 56}


def insert_play(i, j, player, board):
    if player == "player 1":
        team = "X"
    else:
        team = "O"

    board_list = list(board)
    if i == 0:
        if j == 0:
            board_list[1] = team
        if j == 1:
            board_list[5] = team
        if j == 2:
            board_list[9] = team
    if i == 1:
        if j == 0:
            board_list[24] = team
        if j == 1:
            board_list[28] = team
        if j == 2:
            board_list[32] = team
    if i == 2:
        if j == 0:
            board_list[48] = team
        if j == 1:
            board_list[52] = team
        if j == 2:
            board_list[56] = team
    return "".join(board_list)


def check_for_winner(board, game_counter):
    board_list = list(board)

    if not board_list[1] == " ":
        if board_list[1] == board_list[5] == board_list[9]:
            return board_list[1]

    if not board_list[24] == " ":
        if board_list[24] == board_list[28] == board_list[32]:
            return board_list[24]

    if not board_list[48] == " ":
        if board_list[48] == board_list[52] == board_list[56]:
            return board_list[48]

    if not board_list[1] == " ":
        if board_list[1] == board_list[24] == board_list[48]:
            return board_list[1]

    if not board_list[5] == " ":
        if board_list[5] == board_list[28] == board_list[52]:
            return board_list[5]

    if not board_list[9] == " ":
        if board_list[9] == board_list[32] == board_list[56]:
            return board_list[9]

    if not board_list[1] == " ":
        if board_list[1] == board_list[28] == board_list[56]:
            return board_list[1]

    if not board_list[9] == " ":
        if board_list[9] == board_list[28] == board_list[48]:
            return board_list[9]

    if game_counter == 9:
        return "tie"
    return ""


def is_valid_input(i, j):
    try:
        val1 = int(i)
        val2 = int(j)
    except ValueError:
        return False
    return i in range(0, 3) and j in range(0, 3)


def switch_players(player):
    if player == "player 2":
        return "player 1"
    return "player 2"


def is_avilable_cell(play, board):
    board_list = list(board)
    print("print is \"" + board_list[places[play]] + "\"")
    return " " == board_list[places[play]]


# --------------------------main-------------------------------
print("Welcome to tic tac toe game!")
while True:
    game_counter = 0
    board = MAIN_BOARD
    player = "player 2"
    print("Player 1 is X , Player 2 is O")
    while check_for_winner(board, game_counter) == "":

        player = switch_players(player)

        print(board + "\n")

        print(player + "'s Turn.")

        play = input("insert row and column to play without space (exmple - 21):\n")

        i = int(play[0])
        j = int(play[1])

        while (not is_valid_input(i, j)) or (not is_avilable_cell(play, board)):
            if not is_valid_input(i, j):
                play = input("Input is not valid. enter 2 number in range 0 to 2:\n")
            if not is_avilable_cell(play, board):
                play = input("cell is alredy taken, insert different cell:\n")

        board = insert_play(i, j, player, board)
        game_counter += 1

    if check_for_winner(board, game_counter) == "X":
        print("Player 1 wins!")
    elif check_for_winner(board, game_counter) == "O":
        print("Player 2 wins!")
    else:
        print("It's a Tie!")

    print(board + "\n")

    answer = input("would you like to play again?(y/n)")
    if answer == "n" or answer == "N":
        print("thanks for playing!")
        break
