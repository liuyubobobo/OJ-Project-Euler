import time

##################################################################################
## sumOfDivisors
## -- return the sum of all divisors of x
## -- the core thought of this algorithm is refered on
## ---- http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
##################################################################################
def sumOfDivisors(x):

    res = 1

    if x&1 == 0:
        a = 0
        while x&1 == 0:
            x>>=1
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
        res *= (1-x*x)//(1-x)

    return res


#####################################################################
## Found the Upper Bound
## - find the largest element that smaller than or equal to a given t
## - use binary search
#####################################################################
def searchUpperBound( arr , t ):
    ## assume the arr is sorted
    l = -1
    u = len(arr)
    ## {invariant: arr[l] <= t < arr[u]}
    ## assume arr[-1] = - Inf and arr[len(arr)] = Inf at the begining
    while u-1 != l:
        m = (l+u)//2
        if arr[m] > t:
            u = m
        else:
            l = m
        ## {invariant: u-1==l and arr[l] <= t < arr[u]}

    #print( "l =",l,"arr[l] =",arr[l])
    #print( "u =",u,"arr[u] =",arr[u])

    res = l
    if res < 0:# or arr[l] != t:    ##allow the given t doesn't exist
        res = -1
    return res


if __name__ == "__main__":

    abundant_numbers = []
    for i in range(12,28113):
        if i < sumOfDivisors(i)-i:
            abundant_numbers.append(i)

    
    ########################
    ## Thinking 1
    ########################
    t1 = time.time()
    ok = [False] * (28124)
    for i in range(len(abundant_numbers)):
        for j in range(i,len(abundant_numbers)):
            if abundant_numbers[i]+abundant_numbers[j] < len(ok):
                ok[abundant_numbers[i]+abundant_numbers[j]] = True
            else:
                break

    res = 0
    for i in range(len(ok)):
        if not ok[i]:
            res += i
    print(res)
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")


    ############################################
    ## Thinking 2: use binary search to optimize
    ############################################
    t1 = time.time()
    ok = [False] * (28124)
    for i in range(len(abundant_numbers)):
        upper = searchUpperBound( abundant_numbers , 28123 - abundant_numbers[i] )
        if upper >= i:
            upper += 1
            for j in range(i,upper):
                ok[abundant_numbers[i]+abundant_numbers[j]] = True


    res = 0
    for i in range(len(ok)):
        if not ok[i]:
            res += i
    print(res)
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")
