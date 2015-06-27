import time

if __name__ == "__main__":

    ###########################
    ## Thinking 1: Brutal Force
    ###########################
    t1 = time.time()
    res = 1
    num = 1
    for adder in range( 2 , 1001-1+1 , 2 ):
        res += 4*num + 10*adder
        num += adder*4
        #print(res)
    print(res)
    t2 = time.time()
    print("Thinking 1, time =",t2-t1,"s")
    print("="*50,"",sep="\n")

    
    ##########################################
    ## Thinking 2: Mathematical
    ## -- We can get the result = -3 + M1 - M2
    ##########################################
    t1 = time.time()
    S1 = 1001
    S2 = (1001-1)//2

    res = -3

    ###############################################
    ## M1 = segma[1~S1](4*n^2-6n+6)
    ###############################################
    res += 2*S1*(S1+1)*(2*S1+1)//3 - 3*S1**2 + 3*S1

    ###############################################
    ## M1 = segma[1~S2](16*n^2-12n+6)
    ###############################################
    res -= 8*S2*(S2+1)*(2*S2+1)//3 - 6*S2**2
    
    print(res)
    
    t2 = time.time()
    print("Thinking 2, time =",t2-t1,"s")
    print("="*50,"",sep="\n")
