import math
import time


def ok( a , b , c ):

    minPath = min( (a+b)**2+c**2 , (a+c)**2+b**2 , (b+c)**2+a**2 )
    return int( math.sqrt(minPath) )**2 == minPath


#########################################
## solve1 : Brute force to get the answer
#########################################
def solve1( M ):

    res = 0
    for i in range( 1 , M + 1 ):
        for j in range( i , M + 1 ):
            for k in range( j , M + 1 ):
                if ok( i , j , k ):
                    #print( i , j , k )
                    res += 1

    return res


def allPrimitiveTriplesLessOrEqualThan( M ):

    res = []
    stack = [(3,4,5)]
    while len(stack) != 0:

        t = stack.pop()
        if t[0] > M and t[1] > M:
            continue
        res.append(t)

        stack.append( ( t[0]-2*t[1]+2*t[2] , 2*t[0]-t[1]+2*t[2] , 2*t[0]-2*t[1]+3*t[2] ) )
        stack.append( ( t[0]+2*t[1]+2*t[2] , 2*t[0]+t[1]+2*t[2] , 2*t[0]+2*t[1]+3*t[2] ) )
        stack.append( ( -t[0]+2*t[1]+2*t[2] , -2*t[0]+t[1]+2*t[2] , -2*t[0]+2*t[1]+3*t[2] ) )

    return res


def isShortest( t , S2 ):

    return min( (t[0]+t[1])**2 + t[2]**2 , (t[0]+t[2])**2 + t[1]**2 , (t[1]+t[2])**2 + t[0]**2 ) == S2


#######################################################################
## solve2 : Using Primitive Triples Generator
## -- for every primitive triple ( x , y , z ) , try to cut the x and y
#######################################################################
def solve2( M ):
    
    ptriples = allPrimitiveTriplesLessOrEqualThan( M )
    #print( ptriples )

    res = 0
    for i in range( len(ptriples) ):

        triple = sorted(list( ptriples[i] ))
        f = 1
        while f*triple[0] <= M:

            t = [f*x for x in triple]
            if t[1] <= M:
                for k in range( 1 , t[0]//2 + 1 ):
                    ares = sorted( [k , t[0] - k , t[1]] )
                    #print( "try :" , ares )
                    if isShortest( ares , t[2]**2 ):
                        #print( ares )
                        res += 1#M//ares[2]

            for k in range( 1 , t[1]//2 + 1 ):
                ares = sorted( [k , t[1] - k , t[0]] )
                #print( "try :" , ares )
                if ares[2] <= M:
                    if isShortest( ares , t[2]**2 ):
                        #print( t[0] , t[1] , t[2] )
                        #print( ares )
                        res += 1#M//ares[2]

            f += 1

    return res


#######################################################################
## solve3 : Using Primitive Triples Generator
## -- for every primitive triple ( x , y , z ) , try to cut the x and y
## -- no need to try every cut, we can use mathematic to get the res
#######################################################################
def solve3( M ):

    ptriples = allPrimitiveTriplesLessOrEqualThan( M )
    res = 0
    for atriple in ptriples:

        triple0 = min( atriple[0] , atriple[1] )
        triple1 = max( atriple[0] , atriple[1] )

        for f in range( 1 , M//triple0 + 1 ):
            
            t0 = f*triple0
            t1 = f*triple1
            if t1 <= M:
                res += t0//2
            ##########################################
            ## if we try to cut t[0], every cut is ok!
            ##########################################

            #tres = t1//2 - ( t1 - t0 ) + 1
            tres = t0 + 1 - (t1+1)//2
            ########################################
            ## if we try to cut t[1] to k and t[1]-k
            ## -- t[1] - t[0] <= k <= t[1]//2
            ########################################
            if tres > 0:
                res += tres

    return res


##########################
## Optimize from solve3
## -- no need to iterate f
##########################
def solve4( M ):

    ptriples = allPrimitiveTriplesLessOrEqualThan( M )
    res = 0
    for i in range( len(ptriples) ):

        triple = sorted(list( ptriples[i] ))

        # to cut triple[0]
        f = M // triple[1]
        res += calcSequence( triple[0] , f )

        # to cut triple[1]
        ff = M // triple[0]
        tres = triple[1]//2 - ( triple[1] - triple[0] ) + 1
        if tres > 0:
            res += calcSequence( triple[1] , ff ) - ((1+ff)*ff//2)*( triple[1] - triple[0] ) + ff

        #if tres >= 0:
        #    sum2 = calcSequence( triple[1] , ff ) - ((1+ff)*ff//2)*( triple[1] - triple[0] ) + ff
        #    if sum2 != 0:
        #        print( i , "- sum2 :" , sum2 )

            
    return res


## calc unit//2 + 2*unit//2 + 3*unit//2 + ... + f*unit//2
def calcSequence( unit , f ):

    if unit%2 == 0:
        return ((1+f)*f//2) * (unit//2)
    else:
        if f%2 == 0:
            res = 0
            res += ( (unit-1)//2 + ((f-1)*unit-1)//2 ) * ( f // 2 ) // 2
            res += ( unit + (f//2)*unit ) * (f//2) // 2
            return res
        else:
            res = 0
            res += ( (unit-1)//2 + (f*unit-1)//2 ) * ( f // 2 + 1 ) // 2
            res += ( unit + ((f-1)//2)*unit ) * (f//2) // 2
            return res


###################################################
## Using solve1 to brute force calculate the result
###################################################
def bruteForce():

    M = 1
    while True:
        res = solve1( M )
        print( M , ":" , res )
        if res > 1000000:
            break
        M += 1


###################################################
## Using solve3 to binary search the answer
###################################################
def binarySearch():

    l = -1
    u = 2001
    t = 1000000
    while l + 1 != u:
        m = (l+u)//2
        if solve4( m ) < t:
            l = m
        else:
            u = m

    print(u)


def test( func , title ):

    M = 400000
    print( "test" , title , ":" )
    t1 = time.time()
    print( func(M) )
    t2 = time.time()
    print( "time :" , t2-t1 , "s" )
    print()

    
def testSolutions():

    #test( solve1 , "solve 1" )
    #test( solve2 , "solve 2" )
    test( solve3 , "solve 3" )
    test( solve4 , "solve 4" )

    
if __name__ == "__main__":

    testSolutions()
    
    #bruteForce()
    #binarySearch()
    
    #M = 100

    #t1 = time.time()
    #print( "solve1" )
    #print( solve1( M ) )
    #t2 =time.time()
    #print( "solve1 , time:" , t2-t1 , "s" )

    #t1 = time.time()
    #print( "solve1optimize" )
    #print( solve1optimize( M ) )
    #t2 =time.time()
    #print( "solve1optimize , time:" , t2-t1 , "s" )

    #t1 = time.time()
    #print( "solve2" )
    #print( solve2( M ) )
    #t2 = time.time()
    #print( "solve2 , time:" , t2-t1 , "s" )

        
    
    
