import time


def primesSieve(N):
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
    for n in range(3,N,2):
        if not sieve[n]:
            res.append(n)
    return sieve , res


def solve( N ):

    sieve , primes = primesSieve(N)

    res = [ [0]*(N+1) for i in range( len(primes) ) ]
    for i in range( N + 1 ):
        if i%2 == 0:
            res[0][i] = 1
            
    for i in range( len(primes) ):
        res[i][0] = 1

    ans = N + 1
    
    for i in range( 1 , len(primes) ):
        for j in range( 1 , N + 1 ):
            res[i][j] = res[i-1][j] + ( res[i][j-primes[i]] if j-primes[i] >= 0 else 0 )

            if not sieve[j] and res[i][j] - 1 > 5000:
                ans = min( ans , j )
            elif res[i][j] > 5000:
                ans = min( ans , j )

    return ans

    
if __name__ == "__main__":

    t1 = time.time()
    print( solve( 1000 ) )
    t2 = time.time()
    print( "time:" , t2-t1 , "s" )
