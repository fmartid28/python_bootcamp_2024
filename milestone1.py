#!/user/bin/python3
##version 3.11.3

#TICTACTOE game play capstone

#display board
    #initialize an empty array with range of 9 digits, here its 0 to 8

#default range is 0 to 8
def board_disp(a=list(range(0,9))):
    #clear_output() #only works on jupyter notebook
    print("\n"*100)
    print("Tic Tac Toe")
    
    print(f' {a[0]}   |  {a[1]}   |  {a[2]}  ')
    print(' --------------')
    print(f' {a[3]}   |  {a[4]}   |  {a[5]}  ')
    print(' --------------')
    print(f' {a[6]}   |  {a[7]}   |  {a[8]}  ')
    board_list = a
    return board_list #i.e. spots on board corresponding to number. see print    

#user inputs (marker, and spot selection)
def marker_select():
    marker = ''
    
    while marker not in ['x','o']:  
        
        marker=input('player 1 select marker x or o: ')
        
        player1=marker
        
        if player1=='x':
            player2='o'
        else:
            player2='x'          

    print(f'player 1 is {player1}, and player 2 is {player2}')
        
    return player1,player2  

    #validation of int and range. Either within a range or "(e.g.) x in list=[1,2,3]"


def spot_select():
    #could be any variable other than the numbers in the range needed
    #initialize user input as wrong
    user_in="wrong" 

    #checks if user input is digit within range
    while user_in not in range(0,9): 
        
        
        user_in=input("choose a number between 0-8 (see board): ")
        
        #check if digit
        if user_in.isdigit()and int(user_in) in range(0,9):
            #convert input string to int if input .isdigit()
            user_in=int(user_in)
            #clear_output() #only works on jupyter notebook
            print("\n"*100)
            print(f'You\'ve selected number {user_in}')
            return user_in
        else:
            print(f'{user_in} is not a numerical input or between 0 and 8')

#board display update given selected game_in index

#board = board_disp() #returns the default list of list(range(0,9) into variable a)
#print(a)

def board_update():
    
    #selects player marker x or o. returns as tuple selection
    player1marker,player2marker=marker_select()
    
    board_list=board_disp() #reinitilizes list as variable board_list everytime
    
    #initialize empty string for current game marker ('x' or 'o'), and current round (start at 0)
    current_marker=""
    round=1
    
    while set(board_list) != {'x','o'}:        
        if round % 2 == 0:
            player='player 2'
            current_marker = player2marker
            
        else:
            player='player 1'
            current_marker = player1marker
            
        print(f'{player}, round {round}:')
        
        #call for user board spot selection
        user_input = spot_select()
        
    
        #update cell
        while board_list[user_input] in ['x','o']:
            print('selection already made here, choose another cell')
            user_input = spot_select()
        
        board_list[user_input]=current_marker
        
        board_disp(board_list)
        
        round += 1

board_update()