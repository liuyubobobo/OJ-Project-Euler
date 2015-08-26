import time
import math


def searchRes( D ):

    y = 1
    while True:
        #print("in searchRes , try y =" , y )
        if isSquare( D*y*y + 1 ):
            return int( math.sqrt( D*y*y+1 ) )
        y += 1

    
def solve( maxD ):

    maxx = 0
    resD = 0
    for i in range( 2 , maxD + 1 ):
        D = i
        limit = int( math.sqrt( D ) )
        if limit * limit == D:
            continue

        m = 0
        d = 1
        a = limit

        numm1 = 1
        num = a

        denm1 = 0
        den = 1

        while num*num - D*den*den != 1:

            m = d*a-m
            d = ( D - m*m ) // d
            a = ( limit + m ) // d

            numm2 = numm1
            numm1 = num

            denm2 = denm1
            denm1 = den

            num = a*numm1 + numm2
            den = a*denm1 + denm2

        if num > maxx:
            maxx = num
            resD = D

    return resD

    
if __name__ == "__main__":
    
    maxD = 1000
    print( solve( maxD ) )
