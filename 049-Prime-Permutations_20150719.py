def primesShieveWithoutEven( start , N ):
    ## N included!
    if N < 2 : return []
    elif N == 2: return [2]

    sieveBound = (N-1)//2 + 1
    sieve = [False] * sieveBound
    sieve[0] = True

    i = 1
    while 4*i*i+4*i+1 <= N:
        if sieve[i] == False:
            for j in range(2*i*(i+1),sieveBound,2*i+1):
                sieve[j] = True
        i += 1

    #res = [2]
    #for i in range(1,sieveBound):
    #    if not sieve[i] :
    #        res.append(2*i+1)
    res = []
    for i in range( 1 , sieveBound ):
        if not sieve[i] and 2*i+1 >= start:
            res.append( 2*i + 1 )
    
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

def isPermutation( a , b , c ):

    a_arr = sorted([x for x in str(a)])
    b_arr = sorted([x for x in str(b)])
    c_arr = sorted([x for x in str(c)])

    if len(a_arr) == len(b_arr) and len(b_arr) == len(c_arr):

        for i in range(len(a_arr)):
            if a_arr[i] != b_arr[i] or a_arr[i] != c_arr[i]:
                return False

        return True

    return False


#########################################################
## A more complicated and faster algorithm is implemented
## -- in hackerrank.com Project Euler Plus Problem 049
#########################################################
if __name__ == "__main__":

    primes = primesShieveWithoutEven( 1000 , 10000 )
    
    for firstNum in primes:
        #print( "check" , firstNum )
        step = 2
        while firstNum + 2*step < 10000:
            if binarySearch( primes , firstNum + step ) != -1 and binarySearch( primes , firstNum + 2*step ) != -1:
                if isPermutation( firstNum , firstNum + step , firstNum + 2*step ):
                    print( firstNum , firstNum + step , firstNum + 2*step )
            step += 2
