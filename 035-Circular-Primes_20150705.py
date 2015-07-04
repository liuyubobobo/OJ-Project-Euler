import functools
import time

def primesShieve(N):
    ## N included!
    if N < 2 : return [False]*(N+1)
    elif N == 2: return [False,False,True]
    
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

    return sieve


#############################################
## Thinking 1: check all odd 2-digits numbers
## -- Get all the results <= N !!!
#############################################
def solve1( N ):
    
    if N <= 1:
        return 0
    elif N == 2:
        return 1
    elif N <= 4:
        return 2
    elif N <= 6:
        return 3
    elif N <= 10:
        return 4
    
    primeNumbers = primesShieve(N)

    num = 11
    cnt = 4
    while num <= N:

        numdigits = [int(x) for x in str(num)]
        ok = True
        for i in range( len(numdigits) ):
            newDigits = numdigits[i:] + numdigits[:i]
            newNum = functools.reduce( lambda x,y:10*x+y , newDigits , 0 )
            if not primeNumbers[ newNum ]:
                ok = False
                break
        if ok:
            cnt += 1
            #print("ok for" , num )

        num += 2

    return cnt


###################################################
## Thinking 2: check all numbers without even digit
## -- Get all the results <= N !!!
###################################################
def solve2( N ):

    if N <= 1:
        return 0
    elif N == 2:
        return 1
    elif N <= 4:
        return 2
    elif N <= 6:
        return 3
    elif N <= 10:
        return 4
    
    primeNumbers = primesShieve(N)

    cnt = 4
    numDigits = [0]*(len(str(N)))
    numDigits[ len(numDigits)-1 ] = 1
    numDigits[ len(numDigits)-2 ] = 1
    while True:
        
        if functools.reduce( lambda x,y:10*x+y , numDigits , 0 ) > N:
            break
        #print( numDigits )
        #input()

        firstNonZeroIndex = findFirstNonZeroIndex( numDigits )
        numdigits = numDigits[firstNonZeroIndex:]
        ok = True
        for i in range( len(numdigits) ):
            newDigits = numdigits[i:] + numdigits[:i]
            newNum = functools.reduce( lambda x,y:10*x+y , newDigits , 0 )
            if not primeNumbers[ newNum ]:
                ok = False
                break
        if ok:
            cnt += 1
            #print("ok for" , functools.reduce( lambda x,y:10*x+y , numDigits , 0 ) )

        
        mostEvenIndex = firstNonZeroIndex
        while mostEvenIndex < len(numDigits):
            if numDigits[mostEvenIndex] % 2 == 0:
                break
            mostEvenIndex += 1

        if mostEvenIndex == len(numDigits):
            numDigits[len(numDigits)-1] += 2
        else:
            numDigits[mostEvenIndex] += 1
            for i in range( mostEvenIndex + 1  , len(numDigits) ):
                numDigits[i] = 1

        extra = 0
        i = len( numDigits ) - 1
        while i >= 0:
            newExtra = (numDigits[i]+extra) // 10
            numDigits[i] = (numDigits[i]+extra) % 10
            extra = newExtra
            i -= 1

        if extra != 0:
            break

    return cnt


def findFirstNonZeroIndex( arr ):
    for i in range(len(arr)):
        if arr[i] != 0:
            return i
    return len(arr)


if __name__ == "__main__":

    N = 10**6

    t1 = time.time()
    print( solve1(N-1) )
    t2 = time.time()
    print("Thinking 1 -" , t2-t1 , "s")

    t1 = time.time()
    print( solve2(N-1) )
    t2 = time.time()
    print("Thinking 2 -" , t2-t1 , "s")
    
