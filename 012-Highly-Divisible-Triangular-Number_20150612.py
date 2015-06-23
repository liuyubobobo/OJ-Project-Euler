import math
import time

##################################################################
## factorize
## -- Present N as the form of p[0]^a[0]*p[1]^a[1]*...*p[m]^a[m]
## -- Return a dictionary, the key is the prime factor
## ---- and the value is corresponding number of that prime factor  
##################################################################
def factorize( N ):
    res = dict()
    if N%2 == 0:
        res[2] = 0
        while N%2 == 0:
            N //= 2
            res[2] = res[2] + 1

    x = 3
    while x*x <= N:
        if N % x == 0:
            res[x] = 0
            while N%x == 0:
                N //= x
                res[x] = res[x] + 1
        x += 2

    if N != 1:
        res[N] = 1

    return res

def findAllPrimes( N ):
    ## N is included!
    if N < 2:
        return []

    res = [2]
    for i in range(3,N+1,2):
        ok = True
        j = 0
        while res[j]*res[j] <= i:
            if i%res[j] == 0:
                ok = False
                break
            j += 1

        if ok:
            res.append(i)

    return res


def getDivisorNumber( num ):
    p = factorize( num )
    res = 1
    for key in p:
        res *= (p[key]+1)
    return res


def getDivisorNumber2( num , primeTable ):
    res = 1
    for i in range(len(primeTable)):
        if primeTable[i]*primeTable[i] > num:
            break
        a = 0
        while num%primeTable[i] == 0:
            num //= primeTable[i]
            a += 1
        res *= (a+1)

    if num != 1:
        res *= 2
        
    return res


def getDivisorNumber3( num , triangle_num_dict , primeTable , dp_dict ):

    if num == 1:
        return 1
    elif num <= 3:
        return 2
    if num in dp_dict:
        return dp_dict[num]

    #print("deal with",num)
    #input()
    
    if num in triangle_num_dict.keys():
        n = triangle_num_dict[num]
        if n%2 == 0:
            res = getDivisorNumber3( n//2 , triangle_num_dict , primeTable , dp_dict ) * getDivisorNumber3( n + 1 , triangle_num_dict , primeTable , dp_dict )
        else:
            res = getDivisorNumber3( (n+1)//2 , triangle_num_dict , primeTable , dp_dict ) * getDivisorNumber3( n , triangle_num_dict , primeTable , dp_dict )
    else:
        res = getDivisorNumber2( num , primeTable )
        
    dp_dict[num] = res
    return res


if __name__ == "__main__":

    ####################################################################
    ## Thinking 1: generate all num's factorize form without prime table
    ####################################################################
    t1 = time.time()
    num = 0
    index = 1
    while True:
        num = num + index
        divisorNumber = getDivisorNumber( num )
        if divisorNumber > 500:
            print( num )
            break
        index += 1
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")
    print("="*50)


    ####################################################################
    ## Thinking 2: generate all num's factorize form with a prime table
    ####################################################################
    t1 = time.time()

    ## The result is within 32 bit integer representation
    primeTable = findAllPrimes( 2**16 )
    t2 = time.time()
    print("Thinking 2, generate prime table use time:",t2-t1,"s")
    num = 0
    index = 1
    while True:
        num = num + index
        divisorNumber = getDivisorNumber2( num , primeTable)
        if divisorNumber > 500:
            print( num )
            break
        index += 1
    t3 = time.time()
    print("Thinking 2, time:",t3-t1,"s")
    print("="*50)


    ###########################################################
    ## Thinking 3: using the n*(n+1)/2 form without prime table
    ###########################################################
    t1 = time.time()
    num = 0
    index = 1
    triangle_num_dict = dict()
    dp_dict = dict()
    while True:
        num = num + index
        triangle_num_dict[num] = index
        divisorNumber = getDivisorNumber3( num , triangle_num_dict , primeTable , dp_dict )
        if divisorNumber > 500:
            print( num )
            break
        index += 1
    t2 = time.time()
    print("Thinking 3, time:",t2-t1,"s")
    print("="*50)
