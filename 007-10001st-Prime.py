import time
def findXthPrimes( x ):
    if x <= 0:
        return None
    
    if x == 1:
        return 2

    res = [2]
    index = 2
    i = 3
    while True:
        ok = True
        j = 0
        while res[j]*res[j] <= i:
            if i%res[j] == 0:
                ok = False
                break
            j += 1

        if ok:
            res.append(i)
            if index == x:
                return i
            else:
                index += 1
        
        i += 2


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

if __name__ == "__main__":

    limit = 200001

    ####################################################
    ## Thinking 1: Generate the 10001st Prime one by one
    ####################################################
    t1 = time.time()
    res = findXthPrimes( limit )
    t2 = time.time()
    print(res)
    print("Thinking 1 - time:",t2-t1,"s")
    print("-"*50)

    ## -------------------------------------------------

    t1 = time.time()
    count = 1
    candidate = 1
    while count < limit:
        candidate += 2
        if isPrime(candidate):
            count += 1
    t2 = time.time()
    print( candidate )
    print("Thinking 2 - time:",t2-t1,"s")
    
        
    
