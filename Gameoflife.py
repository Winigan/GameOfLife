from Tkinter import *
import time

"""
This section contains all the function that make hte virtual game works
We're focusing on the mathematical and logical functionment of the game
"""

#Function that create an empty board with the dimensions n*p
def create_board (n, p):
    board = []
    for i in range (n):
        row = []
        for j in range (p):
            row.append(0)
        board.append(row)
    return board

#Count the number of neighbors for the cell (x,y)
def neighbors (x, y, board, n, p):
    neighbor = 0
    for i in range (-1,2):
        for j in range (-1,2):

            #We check if the (x,y) cell is close to the edges or not
            if (x + i) >= 0 and (x + i) < n:
                if (y + j) >= 0 and (y + j) < p:

                    #Now we need to know if the cell is empty or not and if it's the original cell
                    if board[x + i][y + j] == 1 and not(i == 0 and j == 0):
                        neighbor += 1
    return neighbor

#Function that apply the game's rules to the board
def next_turn (board, n , p):

    #We create a new empty board
    next_board = create_board(n,p)
    
    for i in range (n):
        for j in range (p):
            
            #Counting the number of neighbors
            neighbor = neighbors(i, j, board, n, p)
            #Rule for existing cell
            if board[i][j] == 1:
                
                #Dying Rule : if a living cell have less than 2 or more than 3 neighbors she dies
                if neighbor > 3 or neighbor < 2:
                    next_board[i][j] = 0

                #Staying Alive Rule : if a living cell have at less 2 and at most 3 neighbors she stays alive
                else:
                    next_board[i][j] = 1
            
            #Born Rule : if a dead cell have exactly 3 neighbors then a cell born there
            else:
                if neighbor == 3:
                    next_board[i][j] = 1

    #We return the new board that will be our new current board
    return next_board

# Function that return Tru if the Board is empty
def is_empty (board, n, p):
    empty = True 
    for i in range (n):
        for j in range (p):
            empty = empty and board[i][j] == 0
    return empty

def print_board (board, n, p):
    border = "+" + "-"*p + "+"
    print(border)
    for i in range (n):
        line = "|"
        for j in range (p):
            cell = ""
            if board[i][j] == 1:
                cell = "1"
            else:
                cell = " "
            line += cell + ""
        print(line + "|")
    print(border)

"""
This section contains all the visual effects such as the creation of the window
or interactions with the user
"""

def start (n, p):
    Board = create_board(n, p)

    #Here you can hardcode a starting state or call existing starts

    print_board(Board, n, p)
    #We make the program run as long as the board is not empty (we can look for oscillating paterns in the future)
    while not is_empty(Board, n, p):
        #We wait 0.1 ms before itering to the next turn and display it
        time.sleep(.1)
        Board = next_turn(Board, n, p)
        print_board(Board, n, p)

#Here is the call with a 50 * 120 board
start(50,120)

"""
Here some code in order to display a window

window = Tk()
label = Label(window, text = "Welcome to the Game Of Life")
label.pack()
window.mainloop 

Creating an input field in a window

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
top.mainloop()
"""