import time

def isPalindrome( s ):
    return s == s[::-1]

if __name__ == "__main__":
    res = 0

    ################################
    ##Thinking 1:
    ##- Try all the possible a and b
    ################################
    t1 = time.time()
    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome( str(i*j) ):
                res = max( res , i*j )
    t2 = time.time()
    
    print(res)
    print("time:" , t2-t1,"s")
    print("Thinking 1 - time:" , t2-t1,"s")
    print("-"*50)

    ## ------------------------------------

    res = 0
    
    #######################################
    ##Thinking 2:
    ##- Try all the possible a, b ( a < b )
    #######################################
    t1 = time.time()
    for i in range(100,1000):
        for j in range(i,1000):
            if isPalindrome( str(i*j) ):
                res = max( res , i*j )
    t2 = time.time()
    
    print(res)
    print("Thinking 2 - time:" , t2-t1,"s")
    print("-"*50)

    ## ------------------------------------
    
    res = 0
    
    #####################################################
    ##Thinking 3:
    ##- Try all the possible a, b ( a < b )
    ##- Search a and b downwards,
    ##----don't call isPalindrome any more when a*b < res 
    #####################################################
    t1 = time.time()
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            t_res = i*j
            if t_res > res and isPalindrome( str(t_res) ):
                res = max( res , t_res )
    t2 = time.time()
    
    print(res)
    print("time:" , t2-t1,"s")
    print("Thinking 3 - time:" , t2-t1,"s")
    print("-"*50)

    ## ------------------------------------

    res = 0
    
    ##############################################################
    ##Thinking 4:
    ##- From the example, we now the res contains 6 digits
    ##- Assume it is P = 100000x + 10000y + 1000z + 100z + 10y + x
    ##- P = 100001x + 10010y + 1100z = 11(9091x + 910y + 100z)
    ##- so a or b contains a factor 11
    ##############################################################
    t1 = time.time()
    for i in range(999,99,-1):
        if i%11 == 0:
            jstart = i
            jstep = -1
        else:
            jstart = 990
            jstep = -11
        for j in range(jstart,99,jstep):
            t_res = i*j
            if t_res > res and isPalindrome( str(t_res) ):
                res = max( res , t_res )
    t2 = time.time()
    
    print(res)
    print("time:" , t2-t1,"s")
    print("Thinking 4 - time:" , t2-t1,"s")
    print("-"*50)
