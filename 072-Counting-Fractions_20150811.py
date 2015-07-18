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


######################################################################
## Thinking 1: The result is segma(phi(x)), x through 2 to d(included)
######################################################################
def solve1():
    d = 10**6
    res = 0
    for i in range( 2 , d + 1 ):
        res += eulerFunction( i )
    return res


####################################################################
## Thinking 2: Using prime numbers to accelerate the above algorithm
####################################################################
def solve2():

    d = 10**6
    res = 0
    primes = primesShieveWithoutEven( d//2 )
    for i in range( 2 , d + 1 ):
        res += eulerFunctionWithFactorize( i , primes )
    return res

def eulerFunctionWithFactorize( N , primes):

    res = N
    d = 1

    i = 0
    while primes[i] * primes[i] <= N:
        if N%primes[i] == 0:
            res *= ( primes[i] - 1 )
            d *= primes[i]
            while N%primes[i] == 0:
                N //= primes[i]
        i += 1

    if N != 1:
        res *= (N-1)
        d *= N

    return res // d

def primesShieveWithoutEven(N):
    ## N included!
    if N < 2 : return []
    elif N == 2: return [2]

    sieveBound = (N+1)//2 + 1
    sieve = [False] * sieveBound
    sieve[0] = True

    i = 1
    while 4*i*i+4*i+1 <= N:
        if sieve[i] == False:
            for j in range(2*i*(i+1),sieveBound,2*i+1):
                sieve[j] = True
        i += 1

    res = [2]
    for i in range(1,sieveBound):
        if not sieve[i]:
            res.append(2*i+1)
    return res


#################################################################################
## Thinking 3: Using prime-shieve-like algorithm to calculate all the phi numbers
#################################################################################
def solve3():

    d = 10**6
    phi_nums = [x for x in range(d+1)]
    for i in range( 2 , d + 1 ):
        if phi_nums[i] == i:
            for j in range( i , d+1 , i ):
                phi_nums[j] = phi_nums[j] * ( i - 1 ) // i

    return sum( phi_nums[2:d+1] )


###############################################################################
## Thinking 4: Using firstFactor Array to accelerate the phi_nums calculation
## -- If n = PI( pi^ai )
## -- Then, phi(n) = n*PI( (pi-1)/pi ) = PI( (pi-1)*pi^(ai-1) )
## -- for m = n/p
## -- phi(n) = phi(m)*p        if p|m
##           = phi(m)*(p-1)    otherwise
## -- This algorithm is a a little faster than previous one but use more space
## ---- Actually double space consumed for store the information of firstFactor
###############################################################################
def solve4():

    d = 10**6
    limit = int( math.sqrt( d ) )
    firstFactor = [ ( 2 if i%2 == 0 else i ) for i in range(d+1)]
    firstFactor[0] = 0
    for i in range( 3 , limit+1 , 2 ):
        if firstFactor[i] == i:
            for j in range( i*i , d+1 , 2*i ):
                firstFactor[j] = i
    #for i in range( d+1 ):
    #    print( "num %d first factor: %d" % ( i , firstFactor[i] ) )

    phi_nums = [ x for x in range(d+1)]
    for i in range( 2 , d + 1 ):
        p = firstFactor[i]
        m = i // p
        if m % p == 0:
            phi_nums[i] = phi_nums[m] * p
        else:
            phi_nums[i] = phi_nums[m] * ( p - 1 )

    return sum( phi_nums[2:d+1] )


##########################################################################
## Thinking 5: Using just one array to store both firstFactor and phi_nums 
##########################################################################
def solve5():

    d = 10**6
    limit = int( math.sqrt( d ) )
    res = [ ( 2 if i%2 == 0 else i ) for i in range(d+1)]
    res[0] = 0
    for i in range( 3 , limit+1 , 2 ):
        if res[i] == i:
            for j in range( i*i , d+1 , 2*i ):
                res[j] = i
    # until now, res stores for the firstFactor information

    for i in range( 2 , d + 1 ):
        p = res[i]
        m = i // p
        if m % p == 0:
            res[i] = res[m] * p
        else:
            res[i] = res[m] * ( p - 1 )

    return sum( res[2:d+1] )


#############################################
## Thinking 6: Only deal with the odd numbers
#############################################
def solve6():

    d = 10**6
    sieveLimit = int(math.sqrt(d))-1
    maxIndex = (d-1)//2
    cache = [0] * ( maxIndex + 1 )
    # At first, the cache means firstFactor
    for n in range( 1 , sieveLimit + 1 ):
        if cache[n] == 0:   #2*n+1 is a prime
            p = 2*n + 1
            # We leave the firstFactor[n] == 0 if 2*n+1 is prime here on purpose
            # This is for future acceleration, no mathematics meaning
            #cache[n] = p
            for j in range( 2*n*(n+1) , maxIndex + 1 , p ):
                cache[j] = p

    multiplier = 1
    while multiplier <= d:
        multiplier *= 2
    # Until here, determine the largest power of 2 not exceeding d
    # -- The multiplier = 2^m
    
    multiplier //= 2
    res = multiplier - 1
    # At this point, initialize res = 2^m-1, which is segma( phi( power of 2 ) )
    # -- phi( 2^k * n ) = 2^(k-1)*phi(n)
    # -- for k > 0 and odd n:
    # ---- segma( phi( 2^k * n ) ) = ( 1 + segma( 2^(k-1) ) ) * phi(n) = 2^m*phi(n)
    #      k=0,m                           k=1,m
    # -- if n == 1, segma( phi(2^k) ) = 2^m*phi(1) = 2^m( include a phi(1) )
    #               k=0,m
    # ---- so, segma( phi( power of 2 ) ) = 2^m - 1
    
    multiplier //= 2
    stepIndex = ( d // multiplier + 1 ) // 2
    # At this point, stepIndex is the smallest n satisfies:
    # (2*n+1) * multiplier <= N < (2*n+1)*2*multiplier

    for n in range( 1 , maxIndex + 1 ):

        if n == stepIndex:
            multiplier //= 2
            stepIndex = ( d // multiplier + 1 ) // 2
        # Keep the invariant: (2*n+1) * multiplier <= N < (2*n+1)*2*multiplier
        
        if cache[n] == 0:   #2*n+1 is a prime
            cache[n] = 2*n
            res += multiplier * cache[n]
            # res += 2^m*phi(2*n+1)
            # if firstFactor[n] == 0, 2*n+1 is a prime, then phi(2*n+1) = 2*n+1-1 = 2*n
        else:
            p = cache[n]
            m = (2*n + 1)//p
            if m%p == 0:
                factor = p
            else:
                factor = p-1
            cache[n] = factor * cache[ m//2 ]
            res += multiplier * cache[n]

    return res


def test( func , title ):

    t1 = time.time()
    print( func() )
    t2 = time.time()
    print( title , "- time:" , t2 - t1 , "s" )
    print( "="*50 )
    print()

    
if __name__ == "__main__":

    #test( solve1 , "Thinking 1" )
    #test( solve2 , "Thinking 2" )
    test( solve3 , "Thinking 3" )
    test( solve4 , "Thinking 4" )
    test( solve5 , "Thinking 5" )
    test( solve6 , "Thinking 6" )
