board = [" " for i in range(9)]

def print_board():
    # row1 ="|{}|{}|{}|".format(board[0], board[1], board[2])
    # row2 ="|{}|{}|{}|".format(board[3], board[4], board[5])
    # row3 ="|{}|{}|{}|".format(board[6], board[7], board[8])

    # print()
    # print(row1)
    # print(row2)
    # print(row3)
    # print()
    con = 0
    for i in range(3):
        for j in range(3):
            print("|"+board[con]+"|",end='')
            con += 1
        print()
def is_win(icon):
    # if(board[0]== icon[0] and board[1]== icon and board[2]== icon) or\
    # (board[3]==icon and board[4]== icon and board[5]== icon) or\
    # (board[6]==icon and board[7]== icon and board[8]== icon) or\
    # (board[0]==icon and board[3]== icon and board[6]== icon) or\
    # (board[1]==icon and board[4]== icon and board[7]== icon) or\
    # (board[2]==icon and board[5]== icon and board[8]== icon) or\
    # (board[0]==icon and board[4]== icon and board[8]== icon) or\
    # (board[2]==icon and board[4]== icon and board[6]== icon) :
    #     return True
    # else:
    #     return False

    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for combo in win_combinations:
        if all(board[i] == icon for i in combo):
            return True
    return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False


     
def player_move(icon):
    if icon == "X":
        number = 1
    if icon == "O":
        number = 2
    # print ("your turn: {}".format(number))


    # choice = int(input("Enter your move (1-9): ").strip())

    # if board[choice -1] == " ":
    #     board[choice -1 ] = icon
    # else:
    #     print()
    #     print("That space is taken!")
    

    while True:
        try:
            print ("your turn: {}".format(number))
            choice = int(input("Enter your move (1-9): ").strip())
            if 1 <= choice <= 9:
                if board[choice - 1] == " ":
                    board[choice - 1] = icon
                    break
                else:
                    print("That space is taken! Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    print_board()
    player_move("X")
    if is_win("X"):
        print("player 1 is win or X is win!!!")
        print_board()
        break
    elif is_draw():
        print("draw !! no one wins!")
        print_board()
        break
    print_board()
    player_move("O")
    if is_win("X"):
        print("player 2 is win or O is win!!!")
        print_board()
        break
    elif is_draw():
        print("draw !! no one wins!")
        print_board()
        break
    
   

