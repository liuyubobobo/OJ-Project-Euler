import time
import math

################################################################################
## The solution is about to solve one kind of Diophantine equation,
## -- Pell's equation
## -- The detail can be seen on: https://en.wikipedia.org/wiki/Pell%27s_equation
## -- a paper is attached for solving this specific equation
## ---- Solving the Pell Equation by H. W. Lenstra Jr.
################################################################################
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
