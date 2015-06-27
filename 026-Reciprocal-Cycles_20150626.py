import time

def getCycleLength( d ):

    res = []
    left = 1
    while left != 0:
        a = (left*10)//d
        #assert( a >=0 and a < 10 )
        left = (left*10)%d
        #if left == 0:
        #    return 0

        for i in range(len(res)):
            if res[i] == (a,left):
                return len(res) - i

        res.append( (a,left) )

    return 0

def getCycleLength2( d ):

    res = dict()
    left = 1
    index = 1
    while True:
        a = (left*10)//d
        assert( a >=0 and a < 10 )
        left = (left*10)%d
        if left == 0:
            return 0

        if (a,left) in res:
            return index - res[(a,left)] + 1

        res[ (a,left) ] = index
        index += 1
        

if __name__ == "__main__":

    ##############################
    ## Thinking 1: Plain algorithm
    ##############################
    t1 = time.time()
    longestCycleLen = 0
    d = 1
    for i in range(2,1000):
        cycleLen = getCycleLength(i)
        if cycleLen > longestCycleLen:
            longestCycleLen = cycleLen
            d = i

    print( d )
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")


    ########################################
    ## Thinking 2: Using dict in getCycleLen
    ########################################
    t1 = time.time()
    longestCycleLen = 0
    d = 1
    for i in range(2,1000):
        cycleLen = getCycleLength2(i)
        if cycleLen > longestCycleLen:
            longestCycleLen = cycleLen
            d = i

    print( d )
    t2 = time.time()
    print("Thinking 2, time:",t2-t1,"s")
