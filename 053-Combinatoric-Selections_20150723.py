import time

def C( n , k ):

    if k > n-k:
        k = n - k

    res = 1
    for i in range( 1 , k + 1 ):
        res = res * n // i
        n -= 1

    return res


########################################
## Thinking 1: Using the definition of C
## -- The time complexity is O( N^3 )
########################################
def solve1( N ):

    res = 0
    for n in range( 1 , N + 1 ):
        for k in range( 1 , n ):
            if C( n , k ) > 10**6:
                res += 1
    return res


########################################
## Thinking 2: Cache the factoial Number
## -- The time complexity is O( N^2 )
########################################
def solve2( N ):

    fac = [1] * (N+1)
    for i in range( 2 , N + 1 ):
        fac[i] = i*fac[i-1]
        
    res = 0
    for n in range( 1 , N + 1 ):
        for k in range( 1 , n ):
            if fac[n]//fac[k]//fac[n-k] > 10**6:
                res += 1
    return res


#####################################################################################
## Thinking 3: Using Pascal Triangle
## -- The time complexity is O( N^2 ) but without lots of multiplication and division
#####################################################################################
def solve3(N):

    res = 0
    p = [ [1]*(N+1) for i in range(N+1)]
    for n in range(1,N+1):
        for r in range( 1 , n ):
            p[n][r] = p[n-1][r] + p[n-1][r-1]
            if p[n][r] > 1000000:
                res += 1
        #print( n , ":" , p[n])
    return res

    
################################################################
## Thinking 4: Using Pascal Triangle
## -- Only 1-D Array is used
## -- The time complexity is O( N^2 ) but without 2-D addressing
################################################################
def solve4(N):

    res = 0
    p = [1]*(N+1)
    for n in range(1,N+1):
        for r in range( n-1 , 0 , -1 ):
            p[r] += p[r-1]
            if p[r] > 1000000:
                res += 1
        #print( n , ":" , p)
    return res


####################################################################################################
## Thinking 5: Using Pascal Triangle
## -- Using the symmetry, when we find the C(n,r) is ok, there is r - (n-r) + 1 elements ok in row n
## -- The time comlexity is nearly O(n)
## -- The space complexity is O(n)
####################################################################################################
def solve5(N):

    res = 0
    p = [1]*(N+1)
    for n in range(1,N+1):
        for r in range( n-1 , 0 , -1 ):
            p[r] += p[r-1]
            if p[r] > 1000000:
                res += ( r - (n-r) + 1 )
                break
        #print( n , ":" , p)
    return res


##############################################################################
## Thinking 6: Reverse the search process
## -- From n = maxn , if we find C(n,k) is ok, we can get the number of that n
## -- Then, we can move upward to find the result of row n-1
## -- For moving right, we can use: C(n,r+1) = (n-r)/(r+1) * C(n,r)
## -- For moving top, we can use: C(n-1,r) = (n-r)/n * C(n,r)
## -- This can be twice faster than Thinking 5!
## ---- Even if it uses more multification and division than Thinking 5
## ---- But the space complexity is O(1)
##############################################################################
def solve6(N):

    res = 0
    r = 0
    n = N
    C = 1
    while r < n//2 + 1:

        if C <= 1000000:
            C = C * (n-r) // (r+1)
            r += 1
        else:
            res += n - 2*r + 1
            C = C * (n-r) // n
            n -= 1

    return res


def test( func , title ):

    N = 100000
    t1 = time.time()
    print( func( N ) )
    t2 = time.time()
    print( title , "- time:" , t2-t1 , "s" )
    

if __name__ == "__main__":

    #test( solve1 , "Thinking 1" )
    #test( solve2 , "Thinking 2" )
    #test( solve3 , "Thinking 3" )
    #test( solve4 , "Thinking 4" )
    test( solve5 , "Thinking 5" )
    test( solve6 , "Thinking 6" )
