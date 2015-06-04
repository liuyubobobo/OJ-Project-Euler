import time

if __name__ == "__main__":

    fibs = [1,2]

    index = 2
    while True:
        x = fibs[index-1] + fibs[index-2]
        if x > 4000000:
            break
        fibs.append(x)
        index = index + 1
    #print(fibs)

    #############################################
    ##Thinking 1: Judge even number by % operator
    #############################################
    t1 = time.time()
    print( sum( [x for x in fibs if x%2 == 0 ]) )
    t2 = time.time()
    print("Thinking 1 - time:",t2-t1,"s")

    print("-"*50)

    ## ------------------------------------------

    #####################################################################
    #Thinking 2:
    #We can conclude that for every three number, the middle one is even.
    #To make things clear, we can add an extra 1 at the first
    #After that, we can conclude that every three number is even
    #Besides, we don't need to use the array to store all the fib numbers
    #####################################################################
    t1 = time.time()
    
    res = 0
    a = 1
    b = 1
    c = a+b
    while c <= 4000000:
        res = res + c
        a = b + c
        b = a + c
        c = a + b
    print(res)

    t2 = time.time()
    print("Thinking 1 - time:",t2-t1,"s")
