def muiltipleNum( multifier , below ):
    res = (below-1) // multifier
    return res

def sumOfMutiples( n , below ):
    return ( n + muiltipleNum( n , 1000 )*n ) * muiltipleNum( n , 1000 ) // 2

print( sumOfMutiples( 3 , 1000) + sumOfMutiples( 5 , 1000) - sumOfMutiples( 15 , 1000 ) )
