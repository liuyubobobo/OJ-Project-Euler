from copy import deepcopy


def getCons( board , i , j ):

    masks = [True] * 10

    #horizontal
    for k in range(9):
        masks[ board[i][k] ] = False

    #vertical
    for k in range(9):
        masks[ board[k][j] ] = False

    istart = (i//3)*3
    jstart = (j//3)*3
    for k1 in range(istart,istart+3):
        for k2 in range(jstart,jstart+3):
            masks[ board[k1][k2] ] = False
            
    res = []
    for i in range(1,10):
        if masks[i]:
            res.append(i)
    return res


def solve( board , deepness = 0 ):

    res = deepcopy(board)
    while True:
        signal = explore( res )
            
        if signal == -1:
            return None
        elif signal == 0:
            break

    if not completeBoard(res):

        i,j = leastTrackbackPosition(res)
        possibleList = getCons(res,i,j)
        
        for x in possibleList:
            #print("Deepness:",deepness,"try",x,"in",possibleList)
            res[i][j] = x
            
            deepres = solve( res , deepness + 1 )
            if deepres != None:
                #print("Deepness:",deepness," Got solution!!!")
                #printBoard(deepres)
                #print("return True in deepness",deepness)
                return deepres

        #print("Deepness:",deepness," Failed!!!")
        return None

    else:
        #print("complete!!")
        return res


def leastTrackbackPosition( board ):
    resi , resj = 0 , 0
    minNum = 9
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                tMinNum = len(getCons( board , i , j ))
                if tMinNum == 2:
                    return i,j
                elif tMinNum < minNum:
                    minNum = tMinNum
                    resi,resj = i,j
    return resi,resj


def explore( board ):

    # 0 - no more unity solution
    # 1 - could explore more
    # -1 - no solution
    resCode = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:

                #print("explore",i,j)
                possibleList = getCons( board , i , j )
                if len(possibleList) == 1:
                    board[i][j] = possibleList[0]
                    resCode = 1
                elif len(possibleList) == 0:
                    return -1
                    
    return resCode


def completeBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def printBoard(board,debug=True):
    for i in range(9):
        print( " ".join([str(x) for x in board[i]]) )
    if debug:
        print("=================")


def solveSudoku( numBoard ):
    
    numBoard = solve( numBoard )

    return numBoard[0][0]*100 + numBoard[0][1]*10 + numBoard[0][2]

                    
if __name__ == "__main__":

    fp = open("096-Sudoku.txt")
    res = 0
    for _ in range(50):
        title = fp.readline().strip()   #for title
        #print( title )
        numBoard = []
        for _ in range(9):
            numBoard.append( [int(x) for x in fp.readline().strip()] )
        #printBoard( numBoard )
        res += solveSudoku( numBoard )
        #print( title , "completed." )
    print( res )

    fp.close()

