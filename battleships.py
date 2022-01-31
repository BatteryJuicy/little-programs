from random import randint, randrange
from time import sleep

board = []
board_ship = board
ship_small = [[], []]
ship_mid = [[], [], []]
ship_big = [[], [], [], []]
ships = [ship_small, ship_mid, ship_big]
for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    board_num = 1
    print("   A B C D E")
    print("")
    for row in board:
        print(board_num, end="  ")
        print(" ".join(row), end="  ")
        print(board_num)
        board_num += 1
    print("")
    print("   A B C D E")


def rand_num():
    rand_row = randint(-1, 2)
    if rand_row == 2:
        rand_row = 1
    rand_col = 0
    if rand_row == 0 or rand_row == 1:
        rand_col = randint(0, 1)
        if rand_col == 0:
            rand_col = -1
    return (rand_row, rand_col)


def make_ship_small(board):
    num_row = randint(1, len(board) - 2)
    num_col = randint(1, len(board) - 2)
    rand_cords = rand_num()

    num = 1
    for i in range(0, 2):
        if i == 1:
            ship_small[1].append(num_row + int(rand_cords[0]))
            ship_small[1].append(num_col + int(rand_cords[1]))
        if i == 0:
            ship_small[0].append(num_row)
            ship_small[0].append(num_col)
        num -= 1


def make_ship_mid(board):
    board_left = board
    for i in board_left:
        for j in i:
            if j != "O":
                board_left.remove(j)


def make_ship(board):
    make_ship_small(board)
    make_ship_mid(board)


make_ship_small(board)
print("-------------------RULES----------------------")
print("To win you have to sink all of the battleships")
print("type the row and then the col of the location")
print("you want to try(row = 1-5, col = A-E) you have")
print("7 turns in total, if you run out of turns, you lose.")
print("WHEN you L O S E, the '^' will be where the ship was.")
print("But, if you hit or sink a ship your try is spared")
print("-------------------RULES----------------------")
print("")
print("welcome to battleships! starting soon...")

guessed_wrong_right = False
turn = 1
# sleep(4) for testing it's off
letters = ["A", "B", "C", "D", "E"]
while turn < 8:
    guessed_wrong_right = False
    sleep(2)
    print("")
    print("TURN ", turn)
    print("")
    sleep(1)
    print_board(board)
    print("")
    sleep(1)
    guess_row = input("Guess Row: ")
    if guess_row.isdigit() == False:
        print("invalid character. Try Again")
        continue
    guess_row_num = int(guess_row) - 1
    guess_col_let = str(input("Guess Col: "))
    guess_col_let = guess_col_let.upper()
    if guess_col_let not in letters:
        print("invalid character. Try Again")
        continue
    guess_col_num = letters.index(guess_col_let)
    guess = [guess_row_num, guess_col_num]
    print("")
    sleep(2)
    if board[guess_row_num][guess_col_num] == "X" or board[guess_row_num][guess_col_num] == "+":
        print("You guessed that one already.")
        guessed_wrong_right = True
    if board[guess_row_num][guess_col_num] == "O":

        if guess_row_num not in range(5) or guess_col_num not in range(5):
            print("Oops, that's not even in the ocean. Try Again")
            guessed_wrong_right = True
        elif (guess == ship_small[0] or guess == ship_small[1]) and guessed_wrong_right == False:
            print("You hit a part of my battleship.")
            board[guess_row_num][guess_col_num] = "+"
            guessed_wrong_right = True
        else:
            print("You missed!")
            board[guess_row_num][guess_col_num] = "X"
    if board[ship_small[0][0]][ship_small[0][1]] == "+" and board[ship_small[1][0]][ship_small[1][1]] == "+":
        print_board(board)
        print("Congrats! you sank my ship!")
        sleep(1)
        print("hooray")
        sleep(1)
        print("hooray")
        sleep(1)
        print("hooray")
        sleep(2)
        break
    if guessed_wrong_right == False:
        turn += 1

    if turn == 5 and board[ship_small[0][0]][ship_small[0][1]] != "+" and board[ship_small[1][0]][ship_small[1][1]] != "+":
        sleep(2)
        print("You know what, I'm feeling generous today...")
        sleep(5)
        print("I will reveal ONE part of my ship!")
        ship_selected = randint(0, 1)
        if ship_selected == 0:
            board[ship_small[0][0]][ship_small[0][1]] = "+"
        else:
            board[ship_small[1][0]][ship_small[1][1]] = "+"

if turn == 8:
    sleep(2)
    print("Game Over!")
    sleep(1)
    print(":(")
    sleep(1)
    board[ship_small[0][0]][ship_small[0][1]] = "^"
    board[ship_small[1][0]][ship_small[1][1]] = "^"
    print_board(board)


input("Press any key to exit: ")
