import functools
import time

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


def seePossibility( arr , res , bound ):

    for i in range( bound[0] ):
        numa = functools.reduce( lambda x,y: 10*x+y , arr[0:i+1] )
        numb = functools.reduce( lambda x,y: 10*x+y , arr[i+1:bound[1]] )
        numc = functools.reduce( lambda x,y: 10*x+y , arr[bound[1]:] )
        if numa*numb == numc:
            res.add( numc )
            #print( numa , "*" , numb , "=" , numc )


def solve(N):

    arr = [ x for x in range(1,N+1) ]
    res = set()

    bound = { 4:(1,2) , 5:(2,3) , 6:(2,3) , 7:(3,4) , 8:(3,4) , 9:(4,5) }
    while True:
        seePossibility( arr , res , bound[N] )

        if not nextPermutationByLex(arr):
            break
        elif arr[0] > 5:
            break
        
    return sum(list(res))


if __name__ == "__main__":

    t1 = time.time()
    res = solve(9)
    t2 = time.time()
    print(res)
    print(t2-t1,"s")
    
        
