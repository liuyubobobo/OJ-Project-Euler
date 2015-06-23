import time

def solve( x , y , dp ):
    if dp[x][y] != -1:
        return dp[x][y]
    if x == 0 or y == 0:
        return 1
    
    dp[x][y] = solve( x-1 , y , dp ) + solve( x , y-1 , dp )
    return dp[x][y]

def solve2( x , y , dp ):
    for j in range(y+1):
        dp[0][j] = 1

    for i in range(1,x+1):
        dp[i][0] = 1
        for j in range(1,y+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[x][y]

def solve3( x , y ):
    return C(x+y,x)

def C( m , n ):
    if m-n < n:
        return C(m,m-n)

    upper = 1
    lower = 1
    for i in range(1,n+1):
        upper *= m - (i-1)
        lower *= n - (i-1)
    return upper//lower

  
if __name__ == "__main__":

    tM = 100
    tN = 100
    
    #################################
    ## Thinking 1: Recursive Solution
    #################################
    t1 = time.time()
    dp = [ [-1]*(tN+1) for i in range(tM+1)]
    print( solve( tM , tN , dp ) )
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")
    print("="*50)


    #################################
    ## Thinking 2: Iterative Solution
    #################################
    t1 = time.time()
    dp = [ [-1]*(tN+1) for i in range(tM+1)]
    print( solve2( tM , tN , dp ) )
    t2 = time.time()
    print("Thinking 2, time:",t2-t1,"s")
    print("="*50)


    #####################################
    ## Thinking 3: Combinatorial Solution
    #####################################
    t1 = time.time()

    print( solve3( tM , tN ) )
    t2 = time.time()
    print("Thinking 3, time:",t2-t1,"s")
    print("="*50)
