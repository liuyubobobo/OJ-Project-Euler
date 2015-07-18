import time

def gcd( a , b ):
    if a < b:
        a,b = b,a

    if a%b == 0:
        return b
    return gcd( b , a%b )


################################################################
## Thinking 1: Calculate responding n for each d
## -- enumerate all possible d value
## ---- for each d, if n/d < n0/d0 => n*d0 < d*n0 => n < d*n0/d0
## ---- Then, n <= floor( d*n0/d0 - 1 )
## ---- if the n is not prime to the d , we check for the less n
################################################################
def solve1( n0 , d0 , N ):

    bestd = 1
    bestn = 0

    for d in range( 3 , N + 1 ):
        
        n = ( n0*d - 1 ) // d0
        while gcd( d , n ) != 1 and n > 0:
            n -= 1

        if n*bestd > bestn*d:
            bestd = d
            bestn = n

    return bestn , bestd


############################################################################
## Thinking 2: No need to check for the less n
## -- For every d, using thinking 1 solution
## -- if the responding n satisfy gcd( d , n ) != 1, no need to check less n
## ---- In such a case , just use n/gcd and d/gcd as a solution
############################################################################
def solve2( n0 , d0 , N ):

    bestd = 1
    bestn = 0

    for d in range( 3 , N + 1 ):
        
        n = ( n0*d - 1 ) // d0
        gcd_n_d = gcd( d , n )
        cur_n = n // gcd_n_d
        cur_d = d // gcd_n_d

        if cur_n*bestd > bestn*cur_d:
            bestd = cur_d
            bestn = cur_n

    return bestn , bestd


#########################################################################################################################
## Thinking 3: Search the result downward and terminate the loop quickly
## -- Because with larger denominators, fractions spaced closer
## -- The result will tend to be a larger denominator
## -- We search the result d downwards and try to terminate the loop earlier
## -- The question is: if we get a bestd and bestn dor current d
## ---- Will there be a better d < cur_d?
## ------ If dx can produce a result, say nx/dx
## ------ We have nx/dx < n0/d0
## ------ n0/d0 - nx/dx = (n0*dx - nx*d0)/(d0*dx) >= 1/(d0*dx)
## ------ for cur_n / cur_d is a solution, we have 1/(d0*cur_d) <= (n0*cur_d-d0*cur_x)/(d0*cur_d)
## ------ Because the new_d is smaller than cur_d, we have: 1/(d0*new_d) < (n0*cur_d-d0*cur_x)/(d0*cur_d)
## ------ newd > cur_d / ( n0*cur_d - d0*cur_x )
## ------ If n0*cur_d - d0*cur_x == 1, we have newd > cur_d, which means there's no more newd < cur_d make a better result
## ------ We exit loop at the point n0*cur_d - d0*cur_x == 1
##########################################################################################################################
def solve3( n0 , d0 , N ):

    bestd = 1
    bestn = 0

    for d in range( N , 2 , -1 ):

        n = ( n0*d - 1 ) // d0
        gcd_n_d = gcd( d , n )
        cur_n = n // gcd_n_d
        cur_d = d // gcd_n_d

        if cur_n*bestd > bestn*cur_d:
            bestd = cur_d
            bestn = cur_n

            if n0*bestd - d0*bestn == 1:
                break

    return bestn , bestd    


def test( func , title ):

    t1 = time.time()
    resn , resd = func( 3 , 7 , 10**6 )
    t2 = time.time()
    print( resn , "/" , resd )
    print( title , "- time:" , t2-t1 , "s" )
    print( "=" * 50 )

    
if __name__ == "__main__":

    test( solve1 , "Thinking 1")
    test( solve2 , "Thinking 2")
    test( solve3 , "Thinking 3")
