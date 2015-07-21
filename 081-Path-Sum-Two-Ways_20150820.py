if __name__ == "__main__":

    fp = open("081-Path-Sum-Two-Ways.txt")
    m = []
    while True:
        line = str( fp.readline() ).strip()
        if line == "":
            break
        #print(line)
        #input()
        m.append( [int(x) for x in line.split(",")] )

    #print(m)

    for j in range( 1 , len(m[0]) ):
        m[0][j] += m[0][j-1]

    for i in range( 1 , len(m) ):
        m[i][0] += m[i-1][0]

    for i in range( 1 , len(m) ):
        for j in range( 1 , len(m[i]) ):
            m[i][j] += min( m[i-1][j] , m[i][j-1] )

    print( m[-1][-1] )
    
