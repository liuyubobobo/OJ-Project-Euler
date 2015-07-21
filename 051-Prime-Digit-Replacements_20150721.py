import time
import functools
    
        
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
            res.append( n )
    return sieve , res


def ok( number , L , primes , sieve ):

    #print("calc changable position of" , number )
    changablePositions = getChangablePositions( number )
    #print( changablePositions )
    #print( "=" * 50 )
    #print()

    oNumberDigits = [int(x) for x in str(number)]
    for aChangablePosition in changablePositions:
        if canAttainLPrimes( oNumberDigits[:] , aChangablePosition , L , sieve ):
            return True

    return False


def getChangablePositions( number ):

    numberDigits = [c for c in str(number)]
    res = [[x] for x in range(len(numberDigits))]

    repeatNumbers = set()
    sortedNumberDigits = sorted( numberDigits )
    for i in range( 1 , len(sortedNumberDigits) ):
        if sortedNumberDigits[i] == sortedNumberDigits[i-1]:
            repeatNumbers.add( sortedNumberDigits[i] )

    repeatNumbersPositions = []
    for digit in repeatNumbers:
        tres = []
        for i in range( len(numberDigits) ):
            if digit == numberDigits[i]:
                tres.append( i )
        repeatNumbersPositions.append( tres )
    #print( "repeatNumbersPositions is:" , repeatNumbersPositions )

    for aRepeatNumberPositions in repeatNumbersPositions:

        for chooseNum  in range( 2 , len(aRepeatNumberPositions)+1 ):

            used = [False]*len(aRepeatNumberPositions)
            generateChooseResult( aRepeatNumberPositions , 0 , chooseNum , [] , used , res )

    return res


def generateChooseResult( nums , index , N , tres , used , res ):

    if index == N:
        res.append( tres[:] )
        return
    
    for i in range( index , len(nums) - ( N - len(tres) ) + 1 ):
        if not used[i]:
            used[i] = True
            tres.append( nums[i] )
            generateChooseResult( nums , index + 1 , N , tres , used , res )
            used[i] = False
            tres.pop()


def canAttainLPrimes( numDigits , changablePosition , L , sieve ):

    if changablePosition[0] == 0:
        startNumber = 1
    else:
        startNumber = 0

    res = 0
    for replacedNumber in range( startNumber , 10 ):

        for place in changablePosition:
            numDigits[place] = replacedNumber
        if not sieve[ functools.reduce( lambda x,y:10*x+y , numDigits , 0 ) ]:
            res += 1

    return res == L


if __name__ == "__main__":

    t1 = time.time()
    MAX_NUM = 10**6
    sieve , primes = primesSieve( MAX_NUM )
    t2 = time.time()
    print( "Generate all" , len(primes) , "primes under" , MAX_NUM , ", time:" , t2-t1 , "s" )

    for i in range( 4 , len(primes) ):
        if ok( primes[i] , 8 , primes , sieve ):
            print( primes[i] )
            break
    
