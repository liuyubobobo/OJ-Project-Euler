import functools
import time

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


def genPermutationByReversedLex( arr ):
    #assert( isinstance( elements , list ) )
    #arr = list(reversed(sorted(elements)))
    yield arr[:]

    while prePermutationByLex(arr):
        yield arr[:]


def ok1(p):

    if not (p[1]*100+p[2]*10+p[3])%2 == 0:
        return False

    if not (p[2]*100+p[3]*10+p[4])%3 == 0:
        return False

    if not (p[3]*100+p[4]*10+p[5])%5 == 0:
        return False

    if not (p[4]*100+p[5]*10+p[6])%7 == 0:
        return False

    if not (p[5]*100+p[6]*10+p[7])%11 == 0:
        return False

    if not (p[6]*100+p[7]*10+p[8])%13 == 0:
        return False

    if not (p[7]*100+p[8]*10+p[9])%17 == 0:
        return False

    return True


######################################################################
## Thinking 1: Generate all permutations and check them by brute force
######################################################################
def solve1():

    digits = [x for x in range(9,-1,-1)]

    res = 0
    for p in genPermutationByReversedLex( digits ):
        if p[0] == 0:
            break

        if ok1( p ):
            res += functools.reduce( lambda x,y:10*x+y , p , 0 )

    return res


#########################################################################
## Thinking 2: Generate all permutations and check them using some tricks
#########################################################################
def solve2():

    digits = [x for x in range(9,-1,-1)]

    res = 0
    for p in genPermutationByReversedLex( digits ):
        if p[0] == 0:
            break

        if ok2( p ):
            res += functools.reduce( lambda x,y:10*x+y , p , 0 )

    return res


def ok2(p):

    if p[3]&1 == 1:
        return False

    if (p[2]+p[3]+p[4])%3 != 0:
        return False

    if p[5] != 0 and p[5] != 5:
        return False

    if not (p[4]*100+p[5]*10+p[6])%7 == 0:
        return False

    num = p[5] + p[7] - p[6]
    if num != 0 and num != 11:
        return False

    if not (p[6]*100+p[7]*10+p[8])%13 == 0:
        return False

    if not (p[7]*100+p[8]*10+p[9])%17 == 0:
        return False

    return True


#############################################################################
## Thinking 3: Do not generate all the permutations according the constraints
#############################################################################
def solve3():

    used = [False] * 10
    p = [-1]*10
    
    return generateResult( p , used , 0 )


def generateResult( p , used , index ):

    if index == 10:
        return functools.reduce( lambda x,y:10*x+y , p , 0 )

    res = 0
    for i in range(len(used)):
        if not used[i]:
            p[index] = i

            if index == 3 and p[3]&1 == 1:
                continue

            if index == 4 and (p[2]+p[3]+p[4])%3 != 0:
                continue

            if index == 5 and p[5] != 0 and p[5] != 5:
                continue

            if index == 6 and ( p[4]*10 + p[5] - 2*p[6])%7 != 0:
                continue
            
            if index == 7:
                num = p[5] + p[7] - p[6]
                if num != 0 and num != 11:
                    continue

            if index == 8 and (p[6]*10+p[7]+4*p[8])%13 != 0:
                continue

            if index == 9 and (p[7]*10+p[8]-5*p[9])%17 != 0:
                continue
            
            used[i] = True
            res += generateResult( p , used , index + 1 )
            used[i] = False

    return res


def test( func , title ):

    t1 = time.time()
    print( func() )
    t2 = time.time()

    print( title , "- time :" , t2-t1 , "s" )

    
if __name__ == "__main__":
    
    test( solve1 , "Thinking 1")
    test( solve2 , "Thinking 2")
    test( solve3 , "Thinking 3")
