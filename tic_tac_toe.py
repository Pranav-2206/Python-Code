board = ["-","-","-",
         "-","X","-",
         "-","-","-",]
cnt = 0
ok = True
def print_board():
    
    
    print(board[0] + " | ", board[1] + " | ", board[2])
    
    print(board[3] + " | ", board[4] + " | ", board[5])
    
    print(board[6] + " | ", board[7] + " | ", board[8])
    

def computer():
    global cnt 
    import random
    y = random.randint(0, 8)
    print("number by computer is", y+1)
    if board[y] == "0" or board[y] == "X":
        print("Let me think !!")
    else:
        board[y] = "X"
        print_board()
        cnt+=1


def turn():
    global cnt
    if (cnt%2 == 0):
        pos = int(input("enter 1-9"))
        pos-=1
        if board[pos] == "0" or board[pos] == "X":
            print("This box is already taken!!")
        else:
            board[pos] = "0"
            print_board()
        cnt+=1
    
    else:
         computer()
         
def check_for_winr():
    global ok 
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        ok = False 
    if row1:
        print(board[0],"Won the game")
        
    elif row2:
        print(board[3],"Won the game")
         
    elif row3:
        print(board[6],"Won the game")
    else:
        return
        
    


def check_for_winc():
    global ok 
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        ok = False 
    if col1:
         print(board[0],"Won the game")
    elif col2:
         print(board[1],"Won the game")
    elif col3:
         print(board[2],"Won the game")
    else:    
        return
    
def check_for_wind():
    global ok 
    d1 = board[0] == board[4] == board[8] != "-"
    d2 = board[2] == board[4] == board[6] != "-"
    if d1 or d2:
        ok = False 
    if d1:
        print(board[0],"Won the game")
    elif d2:
        print(board[2],"Won the game")
    else:
        return 
    
def check_for_tie():
    global ok 
    if "-" not in board:
        print("TIED")
        ok = False
    else:
        return
    
        

def play():
    global ok 
    print_board()
    while ok:
        turn()
        check_for_winr()
        check_for_winc()
        check_for_wind()
        check_for_tie()
        
        
print("Welcome to the tic tac toe game. You will be playing against the computer")        
play()


