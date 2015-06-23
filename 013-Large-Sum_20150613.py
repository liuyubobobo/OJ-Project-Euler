import time

if __name__ == "__main__":
    fp = open("013-Large-Sum.in")
    numbers = []
    for i in range(100):
        numbers.append(int(fp.readline()))


    ###########################
    ## Thinking 1: Brutal Force
    ###########################
    t1 = time.time()
    res = 0
    for num in numbers:
        res += num
    print( str(res)[:10] )
    t2 = time.time()
    print("Thinking 1, time:",t2-t1,"s")
    print("="*50)


    #########################################
    ## Thinking 2: Just use the needed digits
    #########################################
    t1 = time.time()
    res = 0
    for num in numbers:
        res += int(str(num)[0:11])
    print( str(res)[:10] )
    t2 = time.time()
    print("Thinking 2, time:",t2-t1,"s")
    
