# import random
from random import randint
 
board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
 
 
def output():  # Shows board neatly
    for i in range(3):
        print(f"{board[i][0]} {board[i][1]} {board[i][2]}")
 
 
def player():  # Takes coords like (x,y) and then moves the player
    while True:
        q = input("Coord of your turn: (x,y)\n").split(",")
        if len(q) == 2:
            try:
                x = int(q[0])-1
                y = int(q[1])-1
 
                if 0 <= x < 3 and 0 <= y < 3 and board[y][x] == ".":
                    if isCross:
                        board[y][x] = "X"
                    else:
                        board[y][x] = "O"
                    break
 
            except TypeError:
                pass
 
        print("Invalid Coords")
 
 
def winner():  # Checks for a winner - Not draws yet... :(
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] != ".":
            print(board[x][0] + " Wins!")
            return board[x][0]
 
    for y in range(3):
        if board[0][y] == board[1][y] == board[2][y] != ".":
            print(board[0][y] + " Wins!")
            return board[0][y]
 
    if board[0][0] == board[1][1] == board[2][2] != ".":
        print(board[1][1] + " Wins!")
        return board[1][1]
 
    if board[0][2] == board[1][1] == board[2][0] != ".":
        print(board[1][1] + " Wins!")
        return board[1][1]
 
    # if no winner, return true - no print tho
    return False
 
 
def smart():  # Makes computer block winning moves
    for x in range(3):
        if board[x][0] == board[x][1] and board[x][2] == "."!= board[x][1]:
            if isCross:
                board[x][2] = "O"
            else:
                board[x][2] = "X"
            return
 
        if board[x][2] == board[x][1] and board[x][0] == "."!= board[x][1]:
            if isCross:
                board[x][0] = "O"
            else:
                board[x][0] = "X"
            return
 
        if board[x][2] == board[x][0] and board[x][1] == "."!= board[x][0]:
            if isCross:
                board[x][1] = "O"
            else:
                board[x][1] = "X"
            return
 
    for y in range(3):
        if board[0][y] == board[1][y] and board[2][y] == "." != board[1][y]:
            if isCross:
                board[2][y] = "O"
            else:
                board[2][y] = "X"
            return
 
        if board[2][y] == board[1][y] and board[0][y] == "."!= board[1][y]:
            if isCross:
                board[0][y] = "O"
            else:
                board[0][y] = "X"
            return
 
        if board[2][y] == board[0][y] and board[1][y] == "."!= board[0][y]:
            if isCross:
                board[1][y] = "O"
            else:
                board[1][y] = "X"
            return
    computer()
 
 
def computer():  # Computer Plays Random Move
    x = randint(0, 2)
    y = randint(0, 2)
    if board[y][x] == ".":
        if isCross:
            board[y][x] = "O"
        else:
            board[y][x] = "X"
    else:
        computer()
 
 
isCross = False  # Boolean for whether main player is isCross
 
output()
while True:
    q = input("Welcome!\nX or O\n").lower()
    if q == "x":
        isCross = True
        break
    elif q == "o":
        break
    print("Invalid Value")
 
while True:  # Main game loop.
    player()
    output()
    if winner():
        break
 
    print()
 
    smart()
    output()
    if winner():
        break