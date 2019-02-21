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

#This Function that return Tru if the Board is empty
def is_empty (board, n, p):
    empty = True 
    for i in range (n):
        for j in range (p):
            empty = empty and board[i][j] == 0
    return empty

#This Function print the hardcoe version of the board 
def print_board (board, n, p):
    border = "+" + "-"*p + "+"
    print(border)
    for i in range (n):
        line = "|"
        for j in range (p):
            cell = ""
            if board[i][j] == 1:
                cell = "X"
            else:
                cell = " "
            line += cell + ""
        print(line + "|")
    print(border)

#This Function make the game start with a n*p board
def start(n, p):
    Board = create_board(n, p)

    #Here you can hardcode a starting state or call existing starts
    Board[25][60] = 1
    Board[25][61] = 1
    Board[25][62] = 1
    Board[24][61] = 1
    Board[26][62] = 1

    print_board(Board, n, p)
    return Board

"""
def run(board, n, p, canvas):
    #We make the program run as long as the board is not empty (we can look for oscillating paterns in the future)
    while not is_empty(board, n, p):

        #We wait 0.1 ms before itering to the next turn and display it
        display_board(board, n, p, canvas)
        time.sleep(.1)
        board = next_turn(board, n, p)
"""
"""
This section contains all the visual effects such as the creation of the window
or interactions with the user
"""

#This function get the inputs form the use and starts the simulation
def get_input(input1, input2):

    #We get the inputs here and starts the game
    n = int(input2.get())
    p = int(input1.get())

    create_canvas(n,p)

def create_canvas(n,p):
    window = Tk()
    #Button that closes the window
    bouton=Button(window, text="Close", command=window.destroy)
    bouton.pack(side = BOTTOM)
    
    height = n*10
    width = p*10

    
    #We create the canvas that will display our board so we need to create some cells
    canvas = Canvas(window, width=width, height=height, background="white")
    for i in range (height):
        for j in range (width):
            if i%10 == 0 and j%10 ==0:
                canvas.create_rectangle(j, i, j + 10, i + 10)
    canvas.pack()

    #We create a new board and display it on the canvas
    board = start(n, p)
    canvas = display_board(board, n, p, canvas)
    canvas.pack()
    
    #We make the program run as long as the board is not empty (we can look for oscillating paterns in the future)
    while not is_empty(board, n, p):
        canvas = display_board(board, n, p, canvas)
        canvas.pack()
        board = next_turn(board, n, p)
        window.update()

        
#The function display the current board on a new window
def display_board (Board, n, p, canvas):    

    for i in range (n):
        for j in range (p):
            color = ""
            if Board[i][j] == 1:
                color = "black"
            else:
                color = "white"
            canvas.create_rectangle(10*j, 10*i, 10*j + 10, 10*i + 10, fill=color)
    return canvas

#This function create a window that could get input from the user
def create_window():

    #Creation of the window and the head title
    window = Tk()
    label = Label(window, text = "Welcome to the Game Of Life")
    label.pack(side = TOP) 

    #We create two input fields
    inp1_label = Label(window, text = "Enter the height of your board")
    inp1_label.pack()
    input1 = Entry(window, width=30)
    input1.pack()

    inp2_label = Label(window, text = "Enter the width of your board")
    inp2_label.pack()
    input2 = Entry(window, width=30)
    input2.pack()

    #Button that call the command to get the inputs
    bouton = Button(window, text="Enter", command=lambda:get_input(input1,input2))
    bouton.pack()

    #Button that closes the window
    bouton=Button(window, text="Quit", command=window.quit)
    bouton.pack(side = BOTTOM)

    window.mainloop()

""" Here you can call any function in order to test if they work """

#We call the window
create_window()