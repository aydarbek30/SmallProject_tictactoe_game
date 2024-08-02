import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

gameWinner = None
gameRunning = True
currentPlayer = "X"



#print the gameboard
def printBoard (board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


#take player input
def playerInput (board):
    while True:
        if currentPlayer == "X":
            inp = int(input("Enter number 1-9: "))
        else:
            inp = int(input("Enter number 1-9: "))
        if inp >= 1 and inp <=9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print("Ooopps spot busy! ")
            else:
                print("Ooopps spot busy! ")
            printBoard(board)


#check for win or tie
def checkHorizontal(board):
    global gameWinner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        gameWinner = currentPlayer
        return True

def checkRow(board):
    global gameWinner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        gameWinner = currentPlayer
        return True
def checkDiagon(board):
    global gameWinner
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        gameWinner = currentPlayer
        return True

def checkTie (board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie")
        gameRunning = False

def checkWin():
    if checkDiagon(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is: {gameWinner} ")

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def compt (board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#check for win or tie again
while gameRunning:
    printBoard(board)
    if gameWinner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    compt(board)
    checkWin()
    checkTie(board)


