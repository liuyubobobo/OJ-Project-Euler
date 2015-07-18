import time

########################################################
## Thinking 1: Using Python built-in large number system
########################################################
def solve1():

    MOD = 10**10
    res = 0
    for i in range( 1 , 1000+1 ):
        res = ( res + (i**i)%MOD ) % MOD
    return res


######################################################
## Thinking 2: Using divide-and-conquare pow algorithm
######################################################
def solve2():

    MOD = 10**10

    res = 0
    for i in range( 1 , 1000+1 ):
        res =  ( res + myPow( i , i , MOD ) ) % MOD
    return res


def myPow( a , b , MOD ):
    if b == 1:
        return a%MOD

    num = myPow( a , b>>1 , MOD )%MOD

    res = ( num * num ) % MOD
    if b&1 == 0:
        return res

    return ( res * a ) % MOD


##############################################################
## Thinking 3: Using Python built-in pow( a , b , n ) function
## -- It is the fastest!
##############################################################
def solve3():

    MOD = 10**10

    res = 0
    for i in range( 1 , 1000+1 ):
        res =  ( res + pow( i , i , MOD ) ) % MOD
    return res


def test( func , title ):

    t1 = time.time()
    print(func())
    t2 = time.time()
    print( title , "- time:" , t2-t1 , "s")

    
if __name__ == "__main__":

    test( solve1 , "Thinking 1" )
    test( solve2 , "Thinking 2" )
    test( solve3 , "Thinking 3" )
