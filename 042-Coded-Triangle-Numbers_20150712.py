import functools
import math
import time

def calcTriangleNumbersTable( N ):

    res = []
    for i in range(1,N+1):
        res.append( i*(i+1)//2 )
    return res


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


####################################################################################
## Thinking 1: Calculate all the triangle numbers as atable
## -- For each query, using binary search to find out wether the number in the table
####################################################################################
def solve1( words ):

    triangleNumbers = calcTriangleNumbersTable( 100 )
    
    res = 0
    for word in words:
        num = sum([ord(x)-ord('A')+1 for x in word])
        if binarySearch( triangleNumbers , num ) != -1:
            res += 1

    return res


#########################################################################
## Thinking 2: For each query x
## -- If x is a triangle number, then x = 0.5*n*(n+1)
## ---- Then n^2+n-2x=0
## ---- x1 = (-1+sqrt(1+8x))/2 ; x2 = (-1-sqrt(1+8x))/2
## ---- if this x1 , x2 has integer solution, then x is a triangle number
## ---- Because the abs(x1) , abs(x2) are different by 1 exactly
## ---- Then, we can get the n and n+1
## -- Our algorithm just need to see wether 1+8x is a square number
## -- This algorithm is faster than previous one even in this case
#########################################################################
def solve2( words ):

    res = 0
    for word in words:
        num = sum([ord(x)-ord('A')+1 for x in word])
        if isSquareNumber(1+8*num):
            res += 1

    return res


def isSquareNumber(x):
    num = int(math.sqrt(x))
    if num*num == x:
        return True
    return False

    
if __name__ == "__main__":

    fp = open("042-Coded-Triangle-Numbers.txt")
    aline = fp.readline()
    words = [x[1:-1] for x in aline.strip().split(",")]
    fp.close()

    t1 = time.time()   
    print( solve1( words ) )
    t2 = time.time()
    print( "Thinking 1 - time :" , t2-t1 , "s" )


    t1 = time.time()   
    print( solve2( words ) )
    t2 = time.time()
    print( "Thinking 2 - time :" , t2-t1 , "s" )
    
