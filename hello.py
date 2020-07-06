#!/usr/bin/python3

#Two player Tic Tac Toe game

#part 1:
#introduce game by printing "Welcome to Tic Tac Toe!"
print("Welcome to Tic Tac Toe!")




#part 2:
#display the current game board by adding a dictionary 
tictac_board = {
    "1" : "." , "2" : "." , "3" : ".",
    "4" : "." , "5" : "." , "6" : ".",
    "7" : "." , "8" : "." , "9" : "."
}

#create a funtion so the board can be displayed and is able to be updated after 
#a move is made
def printGrid(grid):
    print(board["1"]) + (board["2"]) + (board["3"]) 
    print(board["4"]) + (board["5"]) + (board["6"])
    print(board["7"]) + (board["8"]) + (board["9"])  

#part 3:
#for loop will increment based on success of user choice 
count = 0 
for turn in range(9):

    #print grid 
    print ("here's the current board:")

    printGrid(grid)

    print ("Player 1 enter a number 1 to 9 to place your X or enter 'q' to give up: 1,1")

    user_input = int(input("Where would you like to make your move? "))
    #user input validation - if their move is accetable 
    #print ("Oh no, a piece is already at this place! Try again..." ) 


    
    print("Move accepted, here's the current board: ")

    printGrid(grid)

    print ("Player 2 enter a number 1 to 9 to place your X or enter 'q' to give up: 1,1")



    user_input = int(input("Where would you like to make your move? "))
    #user input validation - if their move is accetable 
    #print ("Oh no, a piece is already at this place! Try again..." ) 

    count +1






    #display instructions to player 
    #create a main function that includes a for if and else loop that takes an input and checks 
    #the move is valid. if it isnt let the player know and restart the loop. 


#examples code 
"""
def game():
    
    turn = 'X'
    count = 0
    
    for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?")

            move = input()        

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue
