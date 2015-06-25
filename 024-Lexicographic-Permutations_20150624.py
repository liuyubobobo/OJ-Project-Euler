######################################################################
## permutationByIndex( elements , index )
## - calc the index'th permutation for the array elements
## - the initial order of elements is think to be the 0'th permutation
## ---- may need to sort elements before call this algorithm
## - index is 0 based index
## - this algorithm is based on lehmer code
## - the process of lehmer code can be refer in
##   - http://blog.csdn.net/chen895281773/article/details/12357703
######################################################################
def permutationByIndex( elements , index ):
    assert( isinstance( elements , list ) and len(elements) != 0 )

    ## The process of calc the fac array can be out of the algorithm
    ## Especially when you need to call this algorithm lots of times
    fac = [1]
    for i in range(1,len(elements)+1):
        fac.append( i*fac[i-1] )
    assert( isinstance( index , int ) and index < fac[len(fac)-1] )
    
    elementsArr = elements[:]
    res = []
    for i in range( len(elements)-1 , -1 , -1 ):

        #print("index:",index)
        code = index // fac[i]
        index = index % fac[i]

        #print("code:",code,"modres:",index)
        
        res.append( elementsArr[code] )

        #elementsArr = elementsArr[0:code] + elementsArr[code+1:]
        ## Use this way may faster than above sentence
        elementsArr[code:i] = elementsArr[code+1:i+1]
        
        #print("After remove", code, "th:", elementsArr)
        #print("======")
    return res


if __name__ == "__main__":
    arr = permutationByIndex( [0,1,2,3,4,5,6,7,8,9] , 10**6-1 )
    print( ''.join([str(x) for x in arr]))
