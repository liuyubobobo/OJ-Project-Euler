import math

def isPrime( x ):
    if x == 1:
        return False
    elif x < 4:
        return True
    elif x%2 == 0:
        return False
    elif x < 9:
        return True
    elif x%3 == 0:
        return False
    else:
        f = 5
        while f*f <= x:
            if x%f == 0:
                return False
            if x%(f+2) == 0:
                return False
            f += 6
        return True


def isSquare( x ):
    num = int(math.sqrt( x ))
    return num*num == x


def ok( num , primes ):

    for p in primes:
        if isSquare( ( num - p ) //2 ):
            return True

    return False
    
if __name__ == "__main__":

    primes = [2,3,5,7]
    num = 9
    while True:
        if isPrime( num ):
            primes.append( num )
        else:
            if not ok( num , primes ):
                print( num )
                break

        num += 2
        
