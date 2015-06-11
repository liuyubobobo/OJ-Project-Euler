import time

def findAllPrimes( N ):
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

def primesShieve(N):
    ## N included!
    if N < 2 : return []
    elif N == 2: return [2]
    
    sieve = [False] * N
    sieve[0] = True
    sieve[1] = True
    for i in range(4,N,2):
        sieve[i] = True

    n = 3
    while n*n <= N:
        if sieve[n] == False:
            for i in range(n*n,N,2*n):
                sieve[i] = True
        n += 2

    res = [2]
    for n in range(3,N,2):
        if not sieve[n]:
            res.append(n)
    return res

def primesShieveWithoutEven(N):
    ## N included!
    if N < 2 : return []
    elif N == 3: return [2]

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

if __name__ == "__main__":

    #########################################
    ## Thinking 1
    ## -- Find all the primes and sum them up
    #########################################
    '''
    t1 = time.time()
    print( sum(findAllPrimes(2000000-1)) )    
    t2 = time.time()
    print("Thinking 1 - time:",t2-t1,"s")
    '''

    #########################################
    ## Thinking 2
    ## -- Primes Shieve Basic Implementation
    #########################################
    t1 = time.time()
    print( sum(primesShieve(2000000-1)) )    
    t2 = time.time()
    print("Thinking 2 - time:",t2-t1,"s")


    #############################################
    ## Thinking 3
    ## -- Primes Shieve Only Consider Odd Numbers
    #############################################
    t1 = time.time()
    print( sum(primesShieveWithoutEven(2000000-1)) )    
    t2 = time.time()
    print("Thinking 3 - time:",t2-t1,"s")
