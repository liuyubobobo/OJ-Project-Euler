import time
import math

def binarySearch( arr , t ):
    ## assume the arr is sorted
    l = 0
    u = len(arr)-1
    ## {invariant: arr[l] <= t <= arr[u]}

    while l <= u:
        m = (l+u)//2
        if arr[m] == t:
            return m
        elif arr[m] > t:
            u = m - 1
        else:
            l = m + 1

    return -1


##############################################################################
## Thinking 1: Using binary search to see wether a number is a pentagon number
##############################################################################
def solve1():

    pentagons = [0,1]

    cur = 2
    while True:

        while len(pentagons) - 1 < cur:
            num = len(pentagons)
            pentagons.append( num*(3*num-1)//2 )

        for i in range( cur-1 , 0 , -1 ):

            a = pentagons[i] + pentagons[cur]
            d = pentagons[cur] - pentagons[i]

            while pentagons[-1] < a:
                num = len(pentagons)
                pentagons.append( num*(3*num-1)//2 )

            if binarySearch( pentagons , a ) != -1 and binarySearch( pentagons , d ) != -1:
                #print(len(pentagons))
                #print( pentagons[-1] , pentagons[-2] )
                return d

        cur += 1


########################################################################################
## Thinking 2: Using mathematic attribution to see whether a number is a pentagon number
## -- a number x is a pentagon number means x = n(3n-1)/2
## ---- Then, 3n^2-n-2x = 0 has a solution
## ---- Which means (1+sqrt(1+24x))/6 is an integer
## ---- Check whether 1+24x is a square number and (1+sqrt(1+24x))%6 == 0
########################################################################################
def solve2():

    pentagons = [0,1]

    cur = 2
    while True:

        pentagons.append( cur*(3*cur-1)//2 )

        for i in range( cur-1 , 0 , -1 ):

            a = pentagons[i] + pentagons[cur]
            d = pentagons[cur] - pentagons[i]

            if isPentagon( a ) and isPentagon( d ):
                return d

        cur += 1


def isPentagon( a ):

    ok , num = isSquareNumber( 1+24*a )
    if ok:
        return ( 1 + num ) % 6 == 0
    else:
        return False


def isSquareNumber( x ):

    num = int(math.sqrt(x))
    if num*num == x:
        return True , num
    return False , -1

        
def test( func , title ):

    t1 = time.time()
    print(func())
    t2 = time.time()
    print( title , "- time:" , t2-t1 , "s" )

    
if __name__ == "__main__":

    test( solve1 , "Thinking 1" )
    test( solve2 , "Thinking 2" )
    
