import math
import time


def gcd( a, b ):
    if a < b:
        a , b = b , a
    if a%b == 0:
        return b
    return gcd( b , a%b )


##########################
## Thinking 1: Brute Force
## -- Check all the a,b
##########################
def solve1( N ):

    squareNum = dict()
    for i in range( 1 , N-1 ):
        squareNum[ i*i ] = i

    res = 0
    maxNum = 0
    resHashTable = [0]*(N+1)
    a = 3
    while 2*a <= N and a <= N - 2*a - 1:

        #########################################
        ## No need to check when both a,b is even
        ## Because in that case, gcd(a,b) != 1
        #########################################
        if a%2 == 1:
            b , step = a , 1
        else:
            b , step = a+1 , 2
        while b <= N - a - b:

            if a*a + b*b in squareNum and gcd(a,b) == 1:
                c = squareNum[ a*a + b*b ]
                n = 1
                p = a + b + c
                while p * n <= N:
                    resHashTable[ p * n ] += 1
                    if resHashTable[ p * n ] > maxNum:
                        maxNum = resHashTable[ p * n ]
                        res = p*n
                    n += 1

            b += step

        a += 1

    return res


#########################################################################
## Thinking 2:
## -- First of all, We can see no matter a or b is odd or even, p is even
## -- Then, the smallest a is 3
## -- Then , we can through a^2 + b^2 = (p-a-b)^2 conclude:
## ---- b = p*(p-2a) / 2(p-a)
#########################################################################
def solve2( N ):

    maxNum = 0
    res = 0
    for p in range(12,N+1,2):

        cnt = 0
        a = 3
        while a+a<p:
            if( p*(p-2*a) % (p-a) == 0 ):
                b = p*(p-2*a) // (2*(p-a))
                if b>=a and p-a-b>b and a+b>p-a-b:
                    cnt += 1
                else:
                    break

            a += 1
            

        if cnt > maxNum:
            maxNum = cnt
            res = p

    return res


########################################################################
## Thinking 3:
## -- This method uses generate all primitive triples
## -- Reference: http://mathworld.wolfram.com/PythagoreanTriple.html
## ---- Every primitive triples can be generated from (a,b,c) = (3,4,5)M
## ------ Where M is a finite product of the matrices U, A , D
##            |  1  2  2 |      | 1 2 2 |      | -1 -2 -2 |
## ------ U = | -2 -1 -2 |  A = | 2 1 2 |  D = |  2  2  2 |
##            |  2  2  3 |      | 2 2 3 |      |  2  2  3 |
########################################################################
def solve3( N ):

    resHashTable = [0]*(N+1)
    genPrimitiveTriples( N , (3,4,5) , resHashTable )

    res = 0
    maxNum = 0
    for i in range(12,N+1):
        if resHashTable[i] > maxNum:
            maxNum = resHashTable[i]
            res = i

    return res


def genPrimitiveTriples( N , t , h ):

    p = t[0] + t[1] + t[2] 
    if p > N:
        return

    n = 1
    while n*p <= N:
        h[n*p] += 1
        n += 1

    genPrimitiveTriples( N , ( t[0]-2*t[1]+2*t[2] , 2*t[0]-t[1]+2*t[2] , 2*t[0]-2*t[1]+3*t[2] ) , h )
    genPrimitiveTriples( N , ( t[0]+2*t[1]+2*t[2] , 2*t[0]+t[1]+2*t[2] , 2*t[0]+2*t[1]+3*t[2] ) , h )
    genPrimitiveTriples( N , ( -t[0]+2*t[1]+2*t[2] , -2*t[0]+t[1]+2*t[2] , -2*t[0]+2*t[1]+3*t[2] ) , h )
    

def test( func , title ):

    t1 = time.time()
    res = func( 10000 )
    t2 = time.time()
    print(res)
    print(title,"- time :",t2-t1,"s")
    print("="*50)
    print()

    
if __name__ == "__main__":

    test( solve1 , "Thinking 1" )
    test( solve2 , "Thinking 2" )
    test( solve3 , "Thinking 2" )
                    
