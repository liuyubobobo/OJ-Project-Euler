import time


def primesSieve(N):
    ## N included!
    if N < 2 :
        return [False] * N
    elif N == 2:
        return [False , False , True]
    
    sieve = [True] * (N+1)
    sieve[0] = False
    sieve[1] = False
    for i in range(4,N+1,2):
        sieve[i] = False

    n = 3
    while n*n <= N:
        if sieve[n] == True:
            for i in range(n*n,N+1,2*n):
                sieve[i] = False
        n += 2

    primes = [0,2]
    for i in range(3,len(sieve),2):
        if sieve[i]:
            primes.append( i )
        
    return primes , sieve


#################################################
## Thinking 1: from start to end, search in order
#################################################
def solve1():

    primeSum , sieve = primesSieve( 10**6-1 )
    #print("%d prime numbers" % len(primes) )
    for i in range( 1 , len(primeSum) ):
        primeSum[i] += primeSum[i-1]
    #print("len(primeSum) =" , len(primeSum) )
    #primes = primeSum[1:]

    maxLen = 1
    res = 2
    for start in range( 0 , len(primeSum) ):
        for end in range( start + maxLen , len(primeSum) ):
            if primeSum[end] - primeSum[start] < 10**6:
                if sieve[primeSum[end] - primeSum[start]] and end - start > maxLen:
                    maxLen = end - start
                    res = primeSum[end] - primeSum[start]
                    #print("%d is the sum of prime number from %d to %d, totally %d prime numbers" % ( res , primes[start+1] , primes[end] , maxLen ) )
            else:
                break
            
    return res


###################################################################
## Thinking 2: from start to end, search in reverse order
## -- For large N, such as 10^12, this solution is much faster
## ---- See details in hackerrank.com Project Euler Plus Problem 50
###################################################################
def solve2():

    primeSum , sieve = primesSieve( 10**6-1 )
    #print("%d prime numbers" % len(primes) )
    for i in range( 1 , len(primeSum) ):
        primeSum[i] += primeSum[i-1]
    #print("len(primeSum) =" , len(primeSum) )
    #primes = primeSum[1:]
    
    maxLen = 1
    res = 2

    startEnd = searchLowerBound( primeSum , 10**6-1 )
    start = 0
    while start + maxLen < len(primeSum):

        end = startEnd
        while end - start > maxLen:
            if primeSum[end] - primeSum[start] < 10**6:
                if sieve[ primeSum[end] - primeSum[start] ] and end - start > maxLen:
                    maxLen = end - start
                    res = primeSum[end] - primeSum[start]
                    #print("%d is the sum of prime number from %d to %d, totally %d prime numbers" % ( res , primes[start+1] , primes[end] , maxLen ) )
                    break

            end -= 1

        start += 1
            
    return res


def searchLowerBound( arr , t ):
    ## assume the arr is sorted
    l = -1
    u = len(arr)
    ## {invariant: arr[l] < t <= arr[u]}
    ## For [0,1,1,1,2], to find 1, the 1 in index 1 satisfy arr[0] < 1 <= arr[u]
    ## assume arr[-1] = - Inf and arr[len(arr)] = Inf at the begining

    while l+1 != u:
        m = (l+u)//2
        if arr[m] < t:
            l = m
            ## arr[l] < t
        else:
            u = m
            ## arr[u] >= t
    ## {invariant: l+1==u and arr[l] < t <= arr[u]}

    #print( "l =",l,"arr[l] =",arr[l])
    #print( "u =",u,"arr[u] =",arr[u])
    
    res = u
    if res >= len(arr):# or arr[u] != t:    ##allow the given t doesn't exist
        res = -1
    return res


def test( func , title ):

    t1 = time.time()
    print( func() )
    t2 = time.time()
    print( title , "- time:" , t2-t1 , "s" )
    print( "=" * 50 )
    print()

        
if __name__ == "__main__":

    test( solve1 , "Thinking 1" )
    test( solve2 , "Thinking 2" )
