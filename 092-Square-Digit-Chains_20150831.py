import time


def isTo89_2( x , dp , N ):
    #print("check",x)
    num = x
    unTagNums = set()
    while True:

        if x <= N:
            if dp[x] != -1:
                for unTagNum in unTagNums:
                    dp[unTagNum] = dp[x]
                return dp[x] == 89
            else:
                if x == 1 or x == 89:
                    for unTagNum in unTagNums:
                        dp[unTagNum] = x
                    dp[num] = x 
                    return x == 89
            unTagNums.add(x)
        
        x = sum( [int(i)**2 for i in str(x)] )
        
    return None


def isTo89_1( x , dp ):

    num = x
    while True:
        if x == 1 or x == 89:
            dp[num] = x
            return x == 89
        if x < num:
            dp[num] = dp[x]
            return dp[num] == 89

        x = sum( [int(i)**2 for i in str(x)] )

if __name__ == "__main__":

    t1 = time.time()
    N = 10**7
    dp = [-1]*(N+1)
    dp[0] = 0
    dp[1] = 1
    res = 0
    for i in range( 2 , N + 1 ):
        if isTo89_1( i , dp ):
        #if isTo89_2( i , dp , N ):
            res += 1
    print( res )
    t2 = time.time()
    print( "time :" , t2-t1 , "s" )
            
