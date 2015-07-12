import functools

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


def prePermutationByLex(arr):

    k = -1
    for i in range( len(arr)-2 , -1 , -1 ):
        if arr[i] > arr[i+1]:
            k = i
            break

    if k == -1:
        return False

    for i in range( len(arr)-1 , k , -1 ):
        if arr[i] < arr[k]:
            l = i
            break

    arr[k],arr[l] = arr[l],arr[k]
    arr[k+1:] = list( reversed(arr[k+1:]))

    return True


def allPermutationByReversedLex( elements ):
    #assert( isinstance( elements , list ) )

    ## sort first to make sure the first permutation is lex smallest
    arr = list(reversed(sorted(elements)))  
    res = [ arr[:] ]

    while prePermutationByLex(arr):
        res.append(arr[:])

    return res


def genPermutationByReversedLex( elements ):
    #assert( isinstance( elements , list ) )
    arr = list(reversed(sorted(elements)))
    yield arr[:]

    while prePermutationByLex(arr):
        yield arr[:]


def findPandigitalPrime( digitsnum ):
    
    digits = [x for x in range(digitsnum,0,-1)]
    #allP = allPermutationByReversedLex( digits )

    for p in genPermutationByReversedLex( digits ):
    #for p in allP:
        num = functools.reduce( lambda x,y:10*x+y , p , 0 )
        #print("test",num)
        if isPrime( num ):
            return True , num

    return False , 0
    

def solve():

    for digitsnum in range(9,0,-1):

        ok , num = findPandigitalPrime( digitsnum )
        if ok:
            #print(num)
            return num


if __name__ == "__main__":

    print( solve() )
    
