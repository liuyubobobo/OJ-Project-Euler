import time


def gcd( a , b ):
    if a%b == 0:
        return b
    return gcd( b , a%b )


#########################################################
## Thinking 1: Using Stern-Brocot Tree
## -- Recursion solution will cause run time error
## -- Transform the algorithm into non-recursive solution
#########################################################
def solve1( a , b , c , d , N ):

    s = []
    s.append( (a,b,c,d) )
    res = 0
    while len(s) != 0:
        x0 , y0 , x1 , y1 = s.pop()
        x = x0 + x1
        y = y0 + y1
        gcd_x_y = gcd( y , x )
        if gcd_x_y != 1:
            x //= gcd_x_y
            y //= gcd_x_y

        #print(y)
        if y <= N:
            res += 1
            s.append( (x0,y0,x,y) )
            s.append( (x,y,x1,y1) )

    return res


#############################################
## Thinking 2: Optimize the previous solution
## -- Omit the numerators
#############################################
def solve2( a , b , c , d , N ):

    res = 0
    s = []
    left = b
    right = d
    while True:
        med = left + right
        if med > N:
            if len(s) > 0:
                left = right
                right = s.pop()
            else:
                break
        else:
            res += 1
            s.append(right)
            right = med

    return res


####################################################################################
## Thinking 3: Calculate the rightrous fraction of a/b and enumerate all the results
## -- by fareyNextTerm
## -- Using exgcd all the time make it slow 
####################################################################################
def solve3( a , b , c , d , N ):

    curn , curd = a , b
    res = 0
    while True:
        curn , curd = fareyNextTerm( curn , curd , N )
        if curn == c and curd == d:
            break
        res += 1

    return res


def fareyNextTerm( n0 , d0 , N ):
    limit = ( n0 * N + 1 ) // d0

    if ( d0*limit - 1 ) % n0 == 0:
        nextn = limit
        nextd = ( d0*nextn - 1 ) // n0
        return nextn , nextd
    
    # ax = b ( mod m )
    a = d0
    b = (d0*limit - 1)%n0
    m = n0
    k = linearCongruenceEquation( a , b , m )

    nextn = limit - k[0]
    nextd = ( d0*nextn - 1 ) // n0
    return nextn , nextd


def linearCongruenceEquation( a , b , m ):

    d , x , y = exgcd( a , m )
    if b%d == 0:

        x = ( x * (b//d) ) % m
        res = []
        for i in range(d):
            res.append( ( x + i * (b//d) ) % m )
        return res
    else:
        return None
    

def exgcd( a , b ):
    if a < b:
        a,b = b,a

    if b == 0:
        return a,1,0

    d,x,y = exgcd( b , a%b )

    return d , y , x - (a//b)*y


####################################################################################
## Thinking 4: Calculate the rightrous fraction of a/b and enumerate all the results
## -- by fareyNextTermByTwoPreviousTerms
## -- Much faster comparing with last one
####################################################################################
def solve4( a , b , c , d , N ):

    ea , eb = a , b
    ec , ed = fareyNextTerm( a , b , N )

    res = 1
    while True:
        p , q = fareyNextTermByTwoPreviousTerms( ea , eb , ec , ed , N )
        if p == c and q == d:
            break
        res += 1

        ea , eb , ec , ed = ec , ed , p , q

    return res


def fareyNextTermByTwoPreviousTerms( a , b , c , d , N ):
    p = (N+b)//d * c - a
    q = (N+b)//d * d - b
    return p , q


####################################################################
## Thinking 5: Optimize the previous algorithm by omitting numerator
####################################################################
def solve5( a , b , c , d , N ):

    ea , eb = a , b
    ec , ed = fareyNextTerm( a , b , N )

    #res = 1
    #while True:
    #    q = (N+eb)//ed * ed - eb
    #    if q == d:
    #        break
    #    res += 1
    #
    #    eb , ed = ed , q

    res = 0
    while ed != d:
        res += 1
        eb , ed = ed , (N+eb)//ed * ed - eb
    return res


####################################################################
## Thinking 6: Mobius Inversion or the Inclusion-Exclusion Principle
####################################################################
def solve6( a , b , c , d , N ):

    primes = primesSieveWithoutEven( N )
    return inclusionExclusion( b , d , N , 0 , primes )


def inclusionExclusion( b , d , limit , index , primes ):

    res = F( b , d , limit )
    while index < len( primes ) and primes[index]*5 < limit :
        newLimit = limit // primes[index]
        res -= inclusionExclusion( b , d , newLimit , index + 1 , primes )
        index += 1
    return res


def F( b , d , N ):
    # b > d so that 1/b < 1/d

    res = 0
    for i in range( 1 , N+1 ):
        res += ((i-1)//d - i//b)
    return res


def primesSieveWithoutEven(N):
    ## N included!
    if N < 2 : return []
    elif N == 2: return [2]

    sieveBound = (N-1)//2 + 1
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


def test( func , title ):

    t1 = time.time()
    #print( func( 1 , 3 , 1 , 2 , 12000 ) )
    #print( func( 1 , 101 , 1 , 100 , 2*(10**6) ) )
    print( func( 1 , 3 , 1 , 2 , 2*(10**6) ) )
    t2 = time.time()
    print( title , " - time :" , t2 - t1 , "s" )

    
if __name__ == "__main__":

    #test( solve1 , "Thinking 1" )
    #test( solve2 , "Thinking 2" )
    #test( solve3 , "Thinking 3" )
    #test( solve4 , "Thinking 4" )
    #test( solve5 , "Thinking 5" )
    test( solve6 , "Thinking 6" )
