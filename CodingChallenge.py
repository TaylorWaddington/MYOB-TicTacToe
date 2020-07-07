#!/usr/bin/python3

#Two player Tic Tac Toe game

#part 1:
#introduce game by printing "Welcome to Tic Tac Toe!"
print("Welcome to Tic Tac Toe!")

player = "1"

#part 2:
#display the current game board by adding a dictionary 
tictac_board = {
    "1": "." , "2": "." , "3": "." ,
    "4": "." , "5": "." , "6": "." ,
    "7": "." , "8": "." , "9": "."
}

board_keys = []
for key in tictac_board:
    board_keys.append(key)

#create a funtion so the board can be displayed and is able to be updated after 
#a move is made
def printGrid(grid):
    print(grid["1"] + grid["2"] + grid["3"]) 
    print(grid["4"] + grid["5"] + grid["6"])
    print(grid["7"] + grid["8"] + grid["9"])  

#part 3:
#for loop will increment based on success of user choice 
move = "X"
count = 0 

print ("here's the current board:")
printGrid(tictac_board)

for turn in range(9):

    print ("Player "+player+" enter a number 1 to 9 to place your X or enter 'q' to give up: ")

    user_input = input("Where would you like to make your move? ")
    
    #user input validation - if their move is accetable 
    if tictac_board[user_input] == ".":
        tictac_board[user_input] = move
        count + 1 
        print("Move accepted, here's the current board: ")
        printGrid(tictac_board) 
    else:
        print("Oh no, a piece is already at this place! Try again..." ) 
        continue

    #validation on winning user moves across
    if count <= 5:
        if tictac_board["1"] == tictac_board["2"] == tictac_board["3"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break
        elif tictac_board["4"] == tictac_board["5"] == tictac_board["6"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break
        elif tictac_board["7"] == tictac_board["8"] == tictac_board["9"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break   
    #validation on winning user moves down  
        elif tictac_board["1"] == tictac_board["4"] == tictac_board["7"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break
        elif tictac_board["2"] == tictac_board["5"] == tictac_board["8"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break    
        elif tictac_board["3"] == tictac_board["6"] == tictac_board["9"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break
    #validation on winning user moves diagonal  
        elif tictac_board["1"] == tictac_board["5"] == tictac_board["9"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break
        elif tictac_board["3"] == tictac_board["5"] == tictac_board["7"] != ".": 
            printGrid(tictac_board)
            print("Move accepted, well done you've won the game! ")                           
            break   

    if count == 9: 
        print("draw")
                
    else:
        print()


        #changes between players 
    if move == "X":
        move = "O"
        player = "2"
    else:
        move = "X"
        player = "1"



    
    




