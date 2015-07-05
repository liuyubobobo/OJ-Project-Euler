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


def ok(num):

    numS = str(num)
    for i in range( 0 , len(numS) ):

        #print("check " , int(numS[i-1:]) )
        if not isPrime( int(numS[i:]) ):
            return False

    for i in range(1,len(numS)):
        #print("check " , int(numS[:i]) )
        if not isPrime( int(numS[:i]) ):
            return False
        
    return True


if __name__ == "__main__":

    res = []

    ############################################################
    ## Because we already know there is 11 results
    ## We then try to figure out all results by brute force
    ## ---------------------------------------------------------
    ## If we know a range, we can check all primes in that range
    ############################################################
    i = 11
    while True:

        if ok(i):
            res.append(i)
            print(i)
            if len(res) == 11:
                break

        i += 2

    print(res)
    print( sum(res) )
        
