import time


def isPrime( x , sieve ):
    if x == 1:
        return False
    elif x < 4:
        return True
    elif x%2 == 0:
        return False
    elif x < 9:
        return True
    elif x%3 == 0:
        return False
    elif x < len( sieve ):
        return not sieve[x]
    else:
        f = 5
        while f*f <= x:
            if x%f == 0:
                return False
            if x%(f+2) == 0:
                return False
            f += 6
        return True


def primesSieve( N ):
    ## N included!
    if N < 2 : return []
    elif N == 2: return [2]
    
    sieve = [False] * (N+1)
    sieve[0] = True
    sieve[1] = True
    for i in range(4,N+1,2):
        sieve[i] = True

    n = 3
    while n*n <= N:
        if sieve[n] == False:
            for i in range(n*n,N+1,2*n):
                sieve[i] = True
        n += 2

    res = [2]
    for n in range(3,N+1,2):
        if not sieve[n]:
            res.append(n)
    return res , sieve


def solve( N , K , primes , sieve , indexOfPrimes ):

    notOK = [set() for i in range(len(primes))]
    for i in range( 1 , len(primes) - ( K - 1 ) + 1 ):
        #if primes[i] >= N:
        #    break
        for j in range( i + 1 , len(primes) - ( K - 2 ) + 1 ):
            #if primes[j] >= N:
            #    break
            #print( "try" , primes[i] , "and" , primes[j] )
            #print( int( str(primes[i]) + str(primes[j]) ) )
            #print( int( str(primes[j]) + str(primes[i]) ) )
            #input()
            if isPrime( int( str(primes[i]) + str(primes[j]) ) , sieve ) and isPrime( int( str(primes[j]) + str(primes[i]) ) ,sieve ):
                choosePrime( j + 1 , primes , sieve , N , K , [ primes[i] , primes[j] ] , notOK , indexOfPrimes )
            else:
                notOK[i].add( primes[j] )


def choosePrime( index , primes , sieve , N , K , tres , notOK , indexOfPrimes ):

    if len(tres) == K:
        print( tres )
        print( sum(tres) )
        return True

    for i in range( index , len(primes) - ( K - len(tres) ) + 1 ):
        
        num = primes[i]
        #if num >= N:
        #    break
        
        ok = True
        for j in range( len(tres) ):
            if num in notOK[indexOfPrimes[tres[j]]]:
                ok = False
                break
            elif not isPrime( int( str(tres[j]) + str(num) ) , sieve ) or not isPrime( int( str(num) + str(tres[j]) ) , sieve ):
                ok = False
                notOK[indexOfPrimes[tres[j]]].add( num )
                break

        if ok:
            tres.append( num )
            choosePrime( i + 1 , primes , sieve , N , K , tres , notOK , indexOfPrimes )
            tres.pop()
        #else:
        #    notOK[i].add( tres[j] )

    
if __name__ == "__main__":

    #t1 = time.time()
    #primes , sieve = primesSieve(3*10**8)
    #t2 = time.time()
    #print("calc 3*10**8 prime numbers:" , t2-t1 , "s")
    
    primes , sieve = primesSieve(2*10**4)
    indexOfPrimes = dict()
    for i in range(len(primes)):
        indexOfPrimes[primes[i]] = i
    #print( primes )
    #print("primes num:" , len(primes))`

    t1 = time.time()
    solve( 2*10**4 , 5 , primes , sieve , indexOfPrimes )
    t2 = time.time()
    print("time :" , t2-t1 , "s" )
    
