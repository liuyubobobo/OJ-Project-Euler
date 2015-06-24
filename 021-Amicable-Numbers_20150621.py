import time

def sumOfDivisors(x):

    res = 1
    f = 2
    while f*f <= x:
        if x%f == 0:
            if f == x//f:
                res += f
            else:
                res += (f+x//f)
        f += 1
    
    return res


def sumOfDivisors2(x):

    res = 1
    f,step = [2,1] if x&1 == 0 else [3,2]
    while f*f <= x:
        if x%f == 0:
            if f == x//f:
                res += f
            else:
                res += (f+x//f)
        f += step
    
    return res


def sumOfDivisors3(x):

    res = 1

    if x%2 == 0:
        a = 0
        while x%2 == 0:
            x//=2
            a += 1
        res *= (1-2**(a+1))//(1-2)

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
        res *= (1-x**2)//(1-x)

    return res


if __name__ == "__main__":

    #############################
    ## Thinking 1: Plain Thinking
    #############################
    t1 = time.time()
    res = 0
    for i in range(1,10000+1):
        x = sumOfDivisors(i)
        if i == sumOfDivisors(x) and i != x:
            res += (i+x)
            #print("Amicable Numbers found:",i,x)

    print( res//2 )
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")
    print("="*50)


    ###########################################
    ## Thinking 2: Optimize by check only x > i
    ###########################################
    t1 = time.time()
    res = 0
    for i in range(1,10000+1):
        x = sumOfDivisors(i)
        if x > i and i == sumOfDivisors(x) and i != x:
            res += (i+x)
            #print("Amicable Numbers found:",i,x)

    print( res )
    t2 = time.time()
    print("Thinking 2, time:",t2-t1,"s")
    print("="*50)


    ############################################
    ## Thinking 3: Optimize in sumOfDivisors
    ## -- Odd numbers can not have even divisors
    ############################################
    t1 = time.time()
    res = 0
    for i in range(1,10000+1):
        x = sumOfDivisors2(i)
        if x > i and i == sumOfDivisors2(x) and i != x:
            res += (i+x)
            #print("Amicable Numbers found:",i,x)

    print( res )
    t2 = time.time()
    print("Thinking 3, time:",t2-t1,"s")
    print("="*50)


    ##################################################################################################
    ## Thinking 4: Optimize by a factorization form
    ## -- See the detail on http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
    ##################################################################################################
    t1 = time.time()
    res = 0
    for i in range(1,10000+1):
        x = sumOfDivisors3(i) - i
        if x > i and i == sumOfDivisors3(x) - x and i != x:
            res += (i+x)
            #print("Amicable Numbers found:",i,x)

    print( res )
    t2 = time.time()
    print("Thinking 4, time:",t2-t1,"s")
    print("="*50)
