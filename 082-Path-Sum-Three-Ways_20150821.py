if __name__ == "__main__":

    fp = open("082-Path-Sum-Three-Ways.txt")
    #fp = open("082-Path-Sum-Three-Ways-test.txt")
    m = []
    while True:
        line = str( fp.readline() ).strip()
        if line == "":
            break
        #print(line)
        #input()
        m.append( [int(x) for x in line.split(",")] )

    #m = [[0]*len(m[0])] + m
    #m = m + [[0]*len(m[0])]
    print("%d * %d matrix" % ( len(m) , len(m[0]) ) )
    #print(m)

    
    res = [ [0]*len(m[0]) for i in range(len(m)) ]
    for i in range( len(res) ):
        res[i][0] = m[i][0]

    for j in range( 1 , len(m[0]) ):

        colUp = [0]*len(m)
        colDown = [0]*len(m)
        
        colDown[0] = res[0][j-1] + m[0][j]
        for i in range( 1 , len(m) ):
            colDown[i] = min( res[i][j-1] , colDown[i-1] ) + m[i][j]
            
        colUp[-1] = res[-1][j-1] + m[-1][j] 
        for i in range( len(m) - 2 , -1 , -1 ):
            colUp[i] = min( colUp[i+1] , res[i][j-1] ) + m[i][j]

        for i in range( 0 , len(m) ):
            res[i][j] = min( colUp[i] , colDown[i] )
            
    
    ans = res[0][-1]
    for i in range( 1 , len(m) ):
        ans = min( ans , res[i][-1] )
    print( ans )
    
