def sumOfDivisors(x):

    res = 1

    if x%2 == 0:
        a = 0
        while x%2 == 0:
            x//=2
            a += 1
        res *= (2**(a+1) - 1) #(1-2**(a+1))//(1-2)

    f = 3
    while f*f <= x:
        if x%f == 0:
            a = 0
            while x%f == 0:
                x//=f
                a += 1
            res *= (1-f**(a+1))//(1-f)
        f += 2

    if x != 1:
        res *= (1-x**2)//(1-x)

    return res


def solve( x , N ):

    firstnum = x
    #print( "solve" , x )
    numSet = set()
    numSet.add( x )
    while True:
        x = sumOfDivisors( x  ) - x
        #print(x)
        if x in numSet:
            if x == firstnum:
                return len( numSet )
            else:
                return -1
        elif x == 1 or x > N:
            return -1
        numSet.add(x)
    

        
if __name__ == "__main__":

    maxlen = 0
    res = 1
    N =10**6
    for i in range( 6 , N + 1 ):
         tres = solve( i , N )
         if tres > maxlen:
             maxlen = tres
             res = i
             print( "maxlen = %d for num %d" % ( maxlen , res ) )
    print( res )
