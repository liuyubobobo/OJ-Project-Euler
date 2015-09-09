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


def solve1():

    N = 10**7
    dp = [-1]*(N+1)
    dp[0] = 0
    dp[1] = 1
    res = 0
    for i in range( 2 , N + 1 ):
        if isTo89_1( i , dp ):
        #if isTo89_2( i , dp , N ):
            res += 1
    return res


########################################################################
## solve2 try to calculate every digits permutation for a number at once
########################################################################
def solve2():

    K = 7
    N = 700#7*9*9
    dp = [-1]*(N+1)
    dp[0] = 0
    dp[1] = 1
    for i in range( 2 , N + 1 ):
        isTo89_1( i , dp )
        
    nums = [-1]*K
    p = [1]*10
    for i in range(2,10):
        p[i] = i*p[i-1]
        
    return genNumber( 0 , nums , K , dp , p )


def genNumber( index , nums , K , dp , p ):

    if index == K:
        if dp[ sum( [x*x for x in nums] ) ] == 89:
            return processCombination( nums , p )
        else:
            return 0
    
    if index == 0:
        startNum = 0
    else:
        startNum = nums[index-1]

    res = 0
    for i in range( startNum , 10 ):
        nums[index] = i
        res += genNumber( index + 1 , nums , K , dp , p )

    return res


def processCombination( nums , p ):

    res = p[len(nums)]

    start = 0
    i = 1
    while i <= len(nums):
        if i == len(nums) or nums[i] != nums[start]:
            res //= p[i-start]
            start = i
        i += 1
        
    return res


def test( func , title ):

    print( "test" , title )
    t1 = time.time()
    print( func() )
    t2 = time.time()
    print( "time :" , t2-t1 , "s" )
    print( "="*50 )
    print()

    
if __name__ == "__main__":

    #test( solve1 , "solve1" )
    test( solve2 , "solve2" )       
