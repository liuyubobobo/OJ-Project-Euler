#######################
## Thinking 1: Basic DP
#######################
def solve1( N ):
    res = [ [0]*(N+1) for i in range(N+1) ]

    for i in range( N + 1 ):
        res[0][i] = 1
        res[1][i] = 1
        res[i][0] = 1
        
    for i in range( 2 , N + 1 ):
        for j in range( 1 , N+1 ):
            res[i][j] = res[i-1][j] + ( res[i][j-i] if j-i >= 0 else 0 )

    print( res[5][5] - 1 )
    return res[N][N] - 1


###################################
## Thinking 2: Using just one array
###################################
def solve2( N ):
    res = [1]*(N+1)
        
    for i in range( 2 , N + 1 ):
        for j in range( 1 , N+1 ):
            res[j] += ( res[j-i] if j-i >= 0 else 0 )

    print( res[5] - 1 )
    return res[N] - 1


if __name__ == "__main__":

    print( solve2( 100 ))
