import time
import math


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


def isPermutation( a , b ):

    sa = str(a)
    sb = str(b)
    if len(sa) == len(sb):

        array_sa = sorted([ c for c in sa])
        array_sb = sorted([ c for c in sb])
        for i in range( len( array_sa ) ):
            if array_sa[i] != array_sb[i]:
                return False
        return True

    return False


##########################
## Thinking 1: Brute Force
##########################
def solve1():
    minRatio = 2*(10**9)
    res = -1
    for num in range( 2 , 10**7 ):
        phi_num = eulerFunction( num )
        if isPermutation( num , phi_num ):
            #print( num , "-" , phi_num )
            if num / phi_num < minRatio:
                minRatio = num / phi_num
                res = num

    return res


##########################################################################
## Thinking 2: The result must contain 2 prime numbers
## -- The result should be least the n/phi(n)
## -- Through previous problem , n should contain as less as prime numbers
## ---- If n contains only one prime numbers p, then phi(n) = phi(p) = n-1
## ---- n and n-1 can not contain same digits
## -- n contains only 2 prime numbers: p1 and p2
## ---- n = p1*p2 , phi(n) = (p1-1)*(p2-1)
## ---- check all p1 and p2 , to get the best p1*p2 we get
##########################################################################
def solve2():

    primes = findAllPrimes( int(math.sqrt( 5*(10**7) )) )

    minRatio = 2*(10**9)
    res = -1
    for i in range( len(primes) ):
        for j in range( i+1 , len(primes) ):
            p1 , p2 = primes[i] , primes[j]

            num = p1*p2
            if num >= 10**7:
                break
            phi_num = (p1-1)*(p2-1)
            if isPermutation( num , phi_num ):
                if num / phi_num < minRatio:
                    minRatio = num / phi_num
                    res = num

    return res


def findAllPrimes( N ):
    ## N is included!
    if N < 2:
        return []

    res = [2]
    for i in range(3,N+1,2):
        ok = True
        j = 0
        while res[j]*res[j] <= i:
            if i%res[j] == 0:
                ok = False
                break
            j += 1

        if ok:
            res.append(i)

    return res


def test( func , title ):
    
    t1 = time.time()
    print( func() )
    t2 = time.time()
    print( title ,"- time :" , t2-t1 , "s")

    
if __name__ == "__main__":

    #test( solve1 , "Thinking 1")
    test( solve2 , "Thinking 2")
