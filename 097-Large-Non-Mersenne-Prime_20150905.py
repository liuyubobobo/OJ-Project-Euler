import time


def solve1( A , B , C , D , MOD ):

    res = 1
    for _ in range( C ):
        res = ( res * B ) % MOD

    return ( A * res + D ) % MOD


def solve2( A , B , C , D , MOD ):

    res = mypow( B , C , MOD )
    return ( A * res + D ) % MOD


def mypow( x , y , MOD ):

    if y == 1:
        return x

    tres = mypow( x , y//2 , MOD )
    if y%2 == 0:
        return ( tres * tres ) % MOD
    else:
        return ( tres * tres * x ) % MOD


def solve3( A , B , C , D , MOD ):
    return ( A * pow( B , C , MOD ) + D ) % MOD

    
if __name__ == "__main__":

    print( "solve 1" )
    t1 = time.time()
    print( solve1( 28433 , 2 , 7830457 , 1 , 10**10 ) )
    t2 = time.time()
    print( "time :" , t2 - t1 , "s" )
    print()

    print( "solve 2" )
    t1 = time.time()
    print( solve2( 28433 , 2 , 7830457 , 1 , 10**10 ) )
    t2 = time.time()
    print( "time :" , t2 - t1 , "s" )
    print()

    print( "solve 3" )
    t1 = time.time()
    print( solve3( 28433 , 2 , 7830457 , 1 , 10**10 ) )
    t2 = time.time()
    print( "time :" , t2 - t1 , "s" )
    print()

    
    
