import time

################################################
## Thinking 1: Check for all numbers below 10**7
## -- about 25s on my machine @ Beijing
################################################
def solve1( power5 ):
    res = 0
    for x in range( 10 , 10**7 ):
        if sum( [power5[int(c)] for c in str(x)] ) == x:
            res += x
    return res


#################################################
## Thinking 2: Check for all numbers below 354294
#################################################
def solve2( power5 ):
    res = 0
    for x in range( 10 , 354294+1 ):
        if sum( [power5[int(c)] for c in str(x)] ) == x:
            res += x
    return res


def test( func , title ):

    power5 = [x**5 for x in range(10)]

    t1 = time.time()
    print(func( power5 ))
    t2 = time.time()
    print(title," - time:",t2-t1,"s")
    print("="*50)
    print()
    
    
if __name__ == "__main__":

    power5 = [x**5 for x in range(10)]

    #test( solve1 , "Thinking 1" )
    test( solve2 , "Thinking 2" )

