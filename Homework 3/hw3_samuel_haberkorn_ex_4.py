"""
Assignment: Homework 3, Exercise 4
Name: Samuel Haberkorn
Date: Sept 28, 2020
Description: This is a command line tic tac toe game complete with winner validation
"""


#Simple way to print the board with lines above.
def print_board(board):
    print("---------")
    for line in board:
        print(" | ".join(line))
        print("---------")
    print("\n\n")

#This function handles the player's move
def play_move(board, char):
    print(f"{char} - It is your turn")
    row = None
    col = None
    #Keep asking unit there is an open cell. There is no data validation
    while row is None or col is None or board[row][col] != " ":
        if row is not None:
            print("That is an invalid cell. Try again")
        row = int(input("Select your row: ")) -1
        col = int(input("Select your column: ")) -1

    board[row][col] = char


#handles the checking
def check_win(board):
    #check rows
    for row in board:
        if row[0] != " " and row[0] == row[1] and row[0] == row[2]:
            return row[0]

    #check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            return board[0][col]

    #check the two diagonals
    if board[0][0] != " " and board[0][0]== board[1][1] and board[0][0]== board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2]== board[1][1] and board[0][2]== board[2][0]:
        return board[0][2]


def main():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    print_board(board)

    #9 times is the most amount of turns
    for play in range(9):
        play_move(board, "x" if play%2==0 else 'o')
        print_board(board)
        #Has anyone won? No. continue
        if (winner := check_win(board)) is None:
            continue

        #Anounce winner and quit
        print(f"Wahooo! {winner} won!")
        return

    #This was a cat game
    print("Too bad. The game ended in a tie ://")




if __name__ == '__main__':
    main()