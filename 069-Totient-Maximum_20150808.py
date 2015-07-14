import functools
import time

def findNumbersAllPrimeFactors( N ):
    res = []
    if N%2 == 0:
        res.append(2)
        while N%2 == 0: N //= 2

    x = 3
    while x*x <= N:
        if N % x == 0:
            res.append(x)
            while N%x == 0: N //= x
        x += 2

    if N != 1:
        res.append(N)

    return res

def eulerFunction( n ):

    if n == 1:
        return 1
    
    primeFactors = findNumbersAllPrimeFactors( n )
    res = n
    d = 1
    for p in primeFactors:
        res *= (p-1)
        d *= p
    return res // d

###########################################################################
## Thinking 1: Scan all numbers <= 10^6
## -- Cal Eeuler function number directly and compare to the maximum result
###########################################################################
def solve1():

    maxRes = 0.0
    maxN = 0
    for n in range( 2 , 10**6 + 1 ):
        tres = n / eulerFunction( n )
        if tres > maxRes:
            maxRes = tres
            maxN = n
            #print( "new winner:" , maxN )

    return maxN
        

###############################################
## Thinking 2: Using Mathematics attribution
## -- phi(n) = n*PI(1-1/p)
## -- Then, n/phi(n) = PI(p/(p-1))
## -- Then, we need to maximize the number of p
###############################################
def solve2():

    p = [2]
    res = 2

    num = 3
    while res*num <= 10**6:
        
        isPrime = True
        i = 0
        while p[i]*p[i] <= num:
            if num%p[i] == 0:
                isPrime = False
                break
            i += 1
        if isPrime:
            p.append( num )
            res *= num

        num += 2

    return res
    
def test( func , title ):

    t1 = time.time()
    print( func() )
    t2 = time.time()
    print( title , "- time:" , t2 - t1 , "s" )
    
    
if __name__ == "__main__":

    test( solve1 , "Thinking 1" )
    test( solve2 , "Thinking 1" )
