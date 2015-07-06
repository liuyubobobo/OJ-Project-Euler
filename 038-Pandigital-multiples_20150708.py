import time
import functools

def nextPermutationByLex(arr):

    k = -1
    for i in range( len(arr)-2 , -1 , -1 ):
        if arr[i] < arr[i+1]:
            k = i
            break

    if k == -1:
        return False
    #print("k =",k)
    
    l = k + 1
    for i in range( k+1 , len(arr) ):
        if arr[i] > arr[k]:
            l = i
    #print("l =",l)
    
    arr[k],arr[l] = arr[l],arr[k]
    arr[k+1:] = list( reversed(arr[k+1:]))

    #print("result:",arr)
    #print("------")
    
    return True


###################################################
## Generate all permutations by lexicographic order
## - Use the nextPermutationByLex(arr) func
###################################################
def allPermutationByLex( elements ):
    #assert( isinstance( elements , list ) )

    ## sort first to make sure the first permutation is lex smallest
    arr = sorted(elements)  
    res = [ functools.reduce( lambda x,y:x+y , arr[:] , "" ) ]

    while nextPermutationByLex(arr):
        res.append( functools.reduce( lambda x,y:x+y , arr[:] , "" ) )

    return res


def okByPermutation( pS ):

    for firstLen in range( 1 , 5 ):

        num = int(pS[:firstLen])
        tres = str(num)
        multiplier = 2
        while True:
            if len(tres) > 9:
                break
            if len(tres) == 9:
                if tres == pS:
                    #print( "num =" , num )
                    #print( "pandigital 9-digit number =" , tres )
                    return True
                else:
                    break

            tres += str(num*multiplier)
            multiplier += 1

    return False


#################################################################
## Thinking 1: Generate all permutations and check them reversely
#################################################################
def solve1():

    nums = allPermutationByLex( ["1","2","3","4","5","6","7","8","9"] )

    for pindex in range( len(nums)-1 , -1 , -1 ):

        if okByPermutation( nums[pindex] ):
            #print( nums[pindex] )
            return nums[pindex]

    return None


####################################################################
## Thinking 2: Try every base number to generate a pandigital number
## -- It is the fastest one!
####################################################################
def solve2():

    #cnt = 0
    res = ""
    for i in range(1,10000):
        
        numS = str(i)

        if allNumDigitsAreDifferent( numS ):
            #cnt += 1
            #print(numS)
            ok ,tres = okByNum( numS )
            if ok:
                #print( numS , tres )
                if tres > res:
                    res = tres

    #print(cnt)
    return res

def allNumDigitsAreDifferent( numS ):

    visit = [False]*10
    visit[0] = True
    for x in numS:
        num = int(x)
        if visit[num]:
            return False
        else:
            visit[num] = True
            
    return True

def okByNum( numS ):

    num = int(numS)
    tres = numS
    multiplier = 2
    while True:
        if len(tres) > 9:
            break
        if len(tres) == 9:
            if allNumDigitsAreDifferent( tres ):
                return True , tres
            else:
                break

        tres += str(num*multiplier)
        multiplier += 1

    return False , None


######################################################################
## Thinking 3: Generate permutation reversedly and check it one by one
######################################################################
def solve3():
    
    for aPermutation in genPermutationByReversedLex( [str(x) for x in range(9,0,-1)] ):
        pS = functools.reduce( lambda x,y:x+y , aPermutation , "" )
        if okByPermutation( pS ):
            return pS

    return None

###################################################################
## Generate permutations by reversed lexicographic order one by one
## - Use yield to create a generator
## - Use prePermutationByLex(arr) func
###################################################################
def genPermutationByReversedLex( elements ):
    #assert( isinstance( elements , list ) )
    arr = list(reversed(sorted(elements)))
    yield arr[:]

    while prePermutationByLex(arr):
        yield arr[:]

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

    
def test( func , title ):

    t1 = time.time()
    res = func()
    t2 = time.time()
    print(res)
    print( title , "- time:" , t2-t1 , "s" )
    print("="*50)
    print()
    
if __name__ == "__main__":

    test( solve1 , "Thinking 1")
    test( solve2 , "Thinking 2")
    test( solve3 , "Thinking 3")


        
