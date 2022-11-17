# import time


def isSafe(x, y, board):        #function that checks if new position is valid
    
    if (x<0 or x>=n or y<0 or y>=n):    #if move is out of board
        return 1   #1 is for out
    elif board[x][y] != -1:             #if square is on the chess knight has already been here
        return 2    #2 is for thread
    elif ((board[x][y] == -1) and (x >= 0) and (x <n) and (y >= 0) and (y <n)):                               #if square is on the chess and knight hasn't already been here and cell
        return 3    #3 is for ok
 
 
def printSolution(n, board):

    global counter


    print("Part 3. Results", file=os)
    print("\t 1) Path is found. Trials=" + str(counter-1) + ".", file=os)
    print("\t 2) Path graphically: \n \n", file=os)

    print("Y, V ^", file=os)


    print("\nPart 3. Results", file=ol)
    print("\t 1) Path is found. Trials=" + str(counter-1) + ".", file=ol)
    print("\t 2) Path graphically: \n \n", file=ol)

    print("Y, V ^", file=ol)


    for i in range(n):
        print("   ", file=os, end='')
        print("   ", file=ol, end='')


        if n==4:
            if i==0:
                print("4 |", file=os, end='')
                print("4 |", file=ol, end='')

            if i==1:
                print("3 |", file=os, end='')
                print("3 |", file=ol, end='')

            if i==2:
                print("2 |", file=os, end='')
                print("2 |", file=ol, end='')

            if i==3:
                print("1 |", file=os, end='')
                print("1 |", file=ol, end='')


        if n==5:
            if i==0:
                print("5 |", file=os, end='')
                print("5 |", file=ol, end='')

            if i==1:
                print("4 |", file=os, end='')
                print("4 |", file=ol, end='')

            if i==2:
                print("3 |", file=os, end='')
                print("3 |", file=ol, end='')

            if i==3:
                print("2 |", file=os, end='')
                print("2 |", file=ol, end='')

            if i==4:
                print("1 |", file=os, end='')
                print("1 |", file=ol, end='')

        if n==6:
            if i==0:
                print("6 |", file=os, end='')
                print("6 |", file=ol, end='')
            if i==1:
                print("5 |", file=os, end='')
                print("5 |", file=ol, end='')

            if i==2:
                print("4 |", file=os, end='')
                print("4 |", file=ol, end='')

            if i==3:
                print("3 |", file=os, end='')
                print("3 |", file=ol, end='')

            if i==4:
                print("2 |", file=os, end='')
                print("2 |", file=ol, end='')

            if i==5:
                print("1 |", file=os, end='')
                print("1 |", file=ol, end='')

        if n==7:
            if i==0:
                print("7 |", file=os, end='')
                print("7 |", file=ol, end='')
            if i==1:
                print("6 |", file=os, end='')
                print("6 |", file=ol, end='')

            if i==2:
                print("5 |", file=os, end='')
                print("5 |", file=ol, end='')

            if i==3:
                print("4 |", file=os, end='')
                print("4 |", file=ol, end='')

            if i==4:
                print("3 |", file=os, end='')
                print("3 |", file=ol, end='')

            if i==5:
                print("2 |", file=os, end='')
                print("2 |", file=ol, end='')

            if i==6:
                print("1 |", file=os, end='')
                print("1 |", file=ol, end='')

            


        for j in range(n):
            if board[i][j] < 9:
                print(" ", file=os, end='')
                print(" ", file=ol, end='')

            print(board[i][j]+1, "  ", end='', file=os)
            print(board[i][j]+1, "  ", end='', file=ol)

        print("", file=os)
        print("", file=ol)


    
    if n==4:
        print("     -------------------------> X, U", file=os)
        print("       1    2    3    4    ", end='', file=os)
        print("     -------------------------> X, U", file=ol)
        print("       1    2    3    4    ", end='', file=ol)
    
    
    if n==5:
        print("     -------------------------> X, U", file=os)
        print("       1    2    3    4    5  ", end='', file=os)
        print("     -------------------------> X, U", file=ol)
        print("       1    2    3    4    5  ", end='', file=ol)
    
    if n==6:
        print("     --------------------------------> X, U", file=os)
        print("       1    2    3    4    5    6  ", end='', file=os)
        print("     --------------------------------> X, U", file=ol)
        print("       1    2    3    4    5    6  ", end='', file=ol)

    if n==7:
        print("     ---------------------------------------> X, U", file=os)
        print("       1    2    3    4    5    6    7", end='', file=os)
        print("     ---------------------------------------> X, U", file=ol)
        print("       1    2    3    4    5    6    7", end='', file=ol)

    
 
 
def solveKT(n):
    global initx 
    global inity

    
    board = [[-1 for i in range(n)]for i in range(n)]   # Initialization of Board matrix
 
    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    # Since the Knight is initially at the first block
    board[initx][inity] = 0
    print(initx, inity)
 
    # Step counter for knight's position
    pos = 1
 
    # Checking if solution exists or not
    if(not solveKTUtil(n, board, initx, inity, move_x, move_y, pos)):
        print("PART 3. Results", file=os)
        print("Solution does not exist. Trials =" + str(counter-1), file=os)
        print("\nPART 3. Results", file=ol)
        print("Solution does not exist. Trials =" + str(counter-1), file=ol)
    else:
        printSolution(n, board)
 
 
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):


    
    global os
    global ol
    global counter
    if(pos == n**2):
        return True
 
    # Try all next moves from the current coordinate x, y
    for rc in range(8):
        new_x = curr_x - move_y[rc]
        new_y = curr_y + move_x[rc]

        sSafe = isSafe(new_x, new_y, board)

        if sSafe == 1:
            # print('' if counter>1000000 else '', ' ' if counter >=100000 else'', '  ' if counter>=10000 else '', '   ' if counter>=1000 else'', '    ' if counter>=100 else '', '     ' if counter >=10 else '', '      ' if counter <10 else'', counter, ")  ", sep='', end='' )
            print('' if counter >=10000000 else '',' ' if (counter>=1000000 and counter<10000000) else '', '  ' if (counter>=100000 and counter<1000000) else'', '   ' if (counter>=10000 and counter<100000) else '', '    ' if (counter>=1000 and counter<10000) else'', '     ' if (counter>=100 and counter<1000) else '', '      ' if (counter>=10 and counter<100) else '', '       ' if counter <10 else'', counter, ")  ", sep='', end='', file=ol )
            
            counter=counter+1
            for i in range(pos-1):
                print("-",end='', file=ol)
            print("R", rc, sep='', end='.   ', file=ol)
            print("U=" , new_x ,",  V=" , new_y , ".  L=" , pos , ".  Out. ", "Backtrack." if rc==7 else "", sep="", file=ol)
            # time.sleep(3)

        elif sSafe == 2:
            # print('' if counter>1000000 else '', ' ' if counter >=100000 else'', '  ' if counter>=10000 else '', '   ' if counter>=1000 else'', '    ' if counter>=100 else '', '     ' if counter >=10 else '', '      ' if counter <10 else'', counter, ")  ", sep='', end='' )
            print('' if counter>10000000 else '',' ' if counter>1000000 else '', '  ' if (counter>=100000 and counter<1000000) else'', '   ' if (counter>=10000 and counter<100000) else '', '    ' if (counter>=1000 and counter<10000) else'', '     ' if (counter>=100 and counter<1000) else '', '      ' if (counter>=10 and counter<100) else '', '       ' if counter <10 else'', counter, ")  ", sep='', end='', file=ol )
            counter=counter+1
            for i in range(pos-1):
                print("-",end='', file=ol)
            print("R", rc, sep='', end='.   ', file=ol)
            print("U=" , new_x ,",  V=" , new_y , ".  L=" , pos , ".  Thread. ", "Backtrack." if rc==7 else"", sep="", file=ol)
            # time.sleep(3)

        
        elif sSafe == 3:
            # print('' if counter>1000000 else '', ' ' if counter >=100000 else'', '  ' if counter>=10000 else '', '   ' if counter>=1000 else'', '    ' if counter>=100 else '', '     ' if counter >=10 else '', '      ' if counter <10 else'', counter, ")  ", sep='', end='' )
            print('' if counter>10000000 else '' ,' ' if (counter>=1000000 and counter<10000000) else '', '  ' if (counter>=100000 and counter<1000000) else'', '   ' if (counter>=10000 and counter<100000) else '', '    ' if (counter>=1000 and counter<10000) else'', '     ' if (counter>=100 and counter<1000) else '', '      ' if (counter>=10 and counter<100) else '', '       ' if counter <10 else'', counter, ")  ", sep='', end='', file=ol )
            counter=counter+1
            for i in range(pos-1):
                print("-",end='', file=ol)
            print("R", rc, sep='', end='.   ', file=ol)
            print("U=" , new_x ,",  V=" , new_y , ".  L=" , pos , ".  Free. ", "BOARD[", new_x, ",", new_y, "]:=", pos, sep="", file=ol)
            board[new_x][new_y] = pos
            # time.sleep(3)

            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
                # Backtracking
            board[new_x][new_y] = -1
    
    return False
 


n = int(input("chess dimension: "))   #chessboard size
initx = int(input("x starting position: "))
inity = int(input("y starting position: "))



if n==3:
    if initx == 1 :
        fy=0
    if initx == 2:
        fy=1
    if initx == 3:
        fy=2
    if inity == 1:
        fx=2
    if inity == 2:
        fx = 1
    if inity == 3:
        fx = 0


if n==4:
    if initx == 1 :
        fy=0
    if initx == 2:
        fy=1
    if initx == 3:
        fy=2
    if initx == 4:
        fy=3
    if inity == 1:
        fx=3
    if inity == 2:
        fx = 2
    if inity == 3:
        fx = 1
    if inity == 4:
        fx = 0



if n==5:
    if initx == 1:
        fy=0
    if initx == 2:
        fy=1
    if initx == 3:
        fy=2
    if initx == 4:
        fy=3
    if initx == 5:
        fy=4
    if inity == 1:
        fx=4
    if inity == 2:
        fx = 3
    if inity == 3:
        fx = 2
    if inity == 4:
        fx = 1
    if inity == 5:
        fx = 0

if n==6:
    if initx == 1:
        fy=0
    if initx == 2:
        fy=1
    if initx == 3:
        fy=2
    if initx == 4:
        fy=3
    if initx == 5:
        fy=4
    if initx == 6:
        fy=5
    if inity == 1:
        fx=5
    if inity == 2:
        fx = 4
    if inity == 3:
        fx = 3
    if inity == 4:
        fx = 2
    if inity == 5:
        fx = 1
    if inity == 6:
        fx = 0
    

if n==7:
    if initx == 1:
        fy=0
    if initx == 2:
        fy=1
    if initx == 3:
        fy=2
    if initx == 4:
        fy=3
    if initx == 5:
        fy=4
    if initx == 6:
        fy=5
    if initx == 7:
        fy=6
    if inity == 1:
        fx=6
    if inity == 2:
        fx=5
    if inity == 3:
        fx=4
    if inity == 4:
        fx=3
    if inity == 5:
        fx=2
    if inity == 6:
        fx=1
    if inity == 7:
        fx=0


initx = fx
inity = fy


counter = 1 #global moves counter

os = open("out-short8.txt","w")
ol = open("out-long8.txt","w")




print("PART 1. DATA \n", file=os)
print("1) BOARD: " + str(n) + "x" + str(n) + ".", file=os)
print("2) Initial Position: X=" + str(initx+1) + ", Y=" + str(inity+1) +". L=" + str(counter) + "\n", file=os)




print("PART 1. DATA \n", file=ol)
print("1) BOARD: " + str(n) + "x" + str(n) + ".", file=ol)
print("2) Initial Position: X=" + str(initx+1) + ", Y=" + str(inity+1) +". L=" + str(counter) + "\n", file=ol)
print("PART 2. Trace", file=ol)


solveKT(n)


os.close()
ol.close()





