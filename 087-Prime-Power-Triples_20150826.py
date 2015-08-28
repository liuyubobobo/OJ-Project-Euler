import math
import time

def primesSieveWithoutEven(N):
    ## N included!
    if N < 2 : return []
    elif N == 2: return [2]

    sieveBound = (N-1)//2 + 1
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


if __name__ == "__main__":

    t1 = time.time()
    primes = primesSieveWithoutEven( int(math.sqrt(50000000)) )
    print( len(primes) )
    t2 = time.time()
    print( "primes calculate completed. time :" , t2 - t1 , "s" )

    resSet = set()
    for a in primes:
        for b in primes:
            sum1 = a**2 + b**3
            if sum1 >= 50000000:
                break
            for c in primes:
                res = sum1 + c**4
                if res >= 50000000:
                    break
                resSet.add( res )

    print( len(resSet) )
    
    t2 = time.time()
    print( "total time :" , t2 - t1 , "s" )
    
