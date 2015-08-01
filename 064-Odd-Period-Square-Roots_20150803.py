import math

##################################################################################################
## The main idea comes from:
## -- https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
##################################################################################################
def calcPeriod( S ):

    m = 0
    d = 1
    a = int(math.sqrt(S))
    a0 = a
    
    preConditionSet = set()
    
    res = 0
    while True:
        
        m = d*a - m
        d = ( S - m*m ) // d
        a = ( a0 + m ) // d

        if (m,d,a) in preConditionSet:
            break
        else:
            preConditionSet.add( (m,d,a) )
            res += 1

    return res
        

if __name__ == "__main__":

    N = 10**4
    #N = 13
    
    squaresSet = set()
    i = 1
    while True:
        squareNum = i*i
        if squareNum > N:
            break
        squaresSet.add( squareNum )
        i += 1

    res = 0
    for i in range(1 , N + 1 ):
        if i not in squaresSet:
            periodRes = calcPeriod( i )
            #print( i , ":" , periodRes )
            if periodRes % 2 == 1:
                res += 1

    print( res )

    
