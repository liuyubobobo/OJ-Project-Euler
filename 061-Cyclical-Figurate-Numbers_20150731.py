def nextPermutationByLex(arr):

    k = -1
    for i in range( len(arr)-2 , -1 , -1 ):
        if arr[i] < arr[i+1]:
            k = i
            break

    if k == -1:
        return False

    for i in range( len(arr)-1 , k , -1 ):
        if arr[i] > arr[k]:
            l = i
            break
    
    arr[k],arr[l] = arr[l],arr[k]
    arr[k+1:] = list( reversed(arr[k+1:]))
    
    return True


def initCalcNumFunc():

    res = []
    res.append(lambda x:x)              #0
    res.append(lambda x:x)              #1
    res.append(lambda x:x)              #2
    res.append(lambda x:x*(x+1)//2)     #3
    res.append(lambda x:x*x)            #4
    res.append(lambda x:x*(3*x-1)//2)   #5
    res.append(lambda x:x*(2*x-1))      #6
    res.append(lambda x:x*(5*x-3)//2)   #7
    res.append(lambda x:x*(3*x-2))      #8

    return res


def solve( bases , nums ):

    res = set()

    bases.sort()
    while True:
    
        for key in nums[bases[0]]:
            for anum in nums[bases[0]][key]:
                #print( key , ":" , anum )
                if anum[2:] in nums[bases[1]]:
                    backtrack( 1 , bases , nums , anum[2:] , [anum] , res )

        if not nextPermutationByLex(bases):
            break
        
    return sorted( list(res) )


def backtrack( index , bases , nums , pre , tres , res ):

    if len(tres) == len(bases):
        #print( tres )
        if tres[-1][2:] == tres[0][:2]:
            print("OK!!!" , tres )
            res.add( sum( [ int(x) for x in tres ] ) )
        #else:
        #    print("NO!!!")
        #print("-"*50)
        return

    for anum in nums[bases[index]][pre]:
        if anum[2:] in nums[bases[ (index+1)%len(bases) ]]:
            tres.append( anum )
            backtrack( index+1 , bases , nums , anum[2:] , tres , res )
            tres.pop()
            


if __name__ == "__main__":

    calcNumFunc = initCalcNumFunc()

    nums = [ dict() for i in range(9) ]
    for base in range( 3 , 9 ):

        i = 1
        while True:
            num = str( calcNumFunc[base]( i ) )
            if len( num ) == 4:
                if num[:2] in nums[base]:
                    nums[base][ num[:2] ].append( num )
                else:
                    nums[base][ num[:2] ] = [num]
            elif len( num ) > 4:
                break

            i += 1

    #for base in range( 3 , 9 ):
    #    print( "base" , base , ":" )
    #    print( nums[base] )
    #    print( "="*50 )

    res = solve( [3,4,5,6,7,8] , nums )
    #res = solve( [3,4,5] , nums )
    for aRes in res:
        print( aRes )
    
    
