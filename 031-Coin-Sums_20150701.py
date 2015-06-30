import time

########################################
## Thinking 1: Recursive DP
## -- The Time complexity is O(MN)
## ---- M is len(coins)
## -- The space complexity is also O(MN)
########################################
def solve1( N , coins ):
    
    dp = [ [0]*(N+1) for i in range(len(coins)) ]
    return __solve1( len(coins)-1 , N , coins , dp )

def __solve1( index , n , coins , dp ):

    if n < 0:
        return 0
    if n == 0:
        return 1
    if dp[index][n] != 0:
        return dp[index][n]

    res = 0
    if index > 0:
        res += __solve1( index - 1 , n , coins , dp )
    res += __solve1( index , n-coins[index] , coins , dp )

    dp[index][n] = res
    return res


#########################################################################
## Thinking 2: Non-Recursive DP
## -- The time complexity and space complexity is both O(MN)
## -- In python, recursive is the most time efficeient
## -- but seems can not use the recursive solution to deal with N >= 1000
## -- It seems the stack space in python is small...
#########################################################################
def solve2( N , coins ):
    
    dp = [ [0]*(N+1) for i in range(len(coins)) ]

    for j in range(N+1):
        dp[0][j] = 1

    for i in range( 1 , len(coins) ):
        dp[i][0] = 1
        for j in range( 1 , N+1 ):
            dp[i][j] = dp[i-1][j] + ( dp[i][j-coins[i]] if j-coins[i] >= 0 else 0 )

    return dp[len(coins)-1][N]


#################################################################################
## Thinking 3: Non-Recursive DP
## -- Using scroll array to optimize the space complexity
## -- The time complexity is still O(MN)
## -- The space complexity is O(N)
## -- Because need to deal with scroll array, it is slower than previous solution
#################################################################################
def solve3( N , coins ):
    
    dp = [ [0]*(N+1) for i in range(2) ]

    for j in range(N+1):
        dp[0][j] = 1

    for i in range( 1 , len(coins) ):
        dp[i&1][0] = 1
        for j in range( 1 , N+1 ):
            dp[i&1][j] = dp[(i-1)&1][j] + ( dp[i&1][j-coins[i]] if j-coins[i] >= 0 else 0 )

    return dp[(len(coins)-1)&1][N]


###############################################################
## Thinking 4: Using only on 1-D Array to deal with the problem
## -- the DP formualtion can be inducted from previous method
## -- The time complexity is still O(MN)
## -- The space complexity is still O(N)
## -- It is the fastest!
################################################################
def solve4( N , coins ):

    dp = [1]*(N+1)
    for i in range( 1 , len(coins) ):
        for j in range( 1 , N+1 ):
            dp[j] += ( dp[j-coins[i]] if j-coins[i] >= 0 else 0 )

    return dp[N]


def test( func , N , coins , title ):

    t1 = time.time()
    for t in range(1000):
        res = func( N , coins )
    t2 = time.time()
    print( res )
    print( title , "- time :" , t2-t1 , "s" )
    print( "="*50 )
    print()
    
    
if __name__ == "__main__":

    coins = [1,2,5,10,20,50,100,200]
    N = 1000
    
    #test( solve1 , N , coins , "Thinking 1" )
    test( solve2 , N , coins , "Thinking 2" )
    test( solve3 , N , coins , "Thinking 3" )
    test( solve4 , N , coins , "Thinking 4" )
