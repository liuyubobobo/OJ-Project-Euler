import time

if __name__ == "__main__":

    ##############################################
    #Thinking 1: The basic idea, an O(n) algorithm
    ##############################################

    t1 = time.time()

    res = 0
    for i in range(1000):
        if i%3 == 0 or i%5==0:
            res += i

    t2 = time.time()
    
    print(res)
    print("Thinking 1 - time:",t2-t1,"s")

    print("-"*50)

    ## ---------------------------------------------
    
    ###################################
    #Thinking2: Using an O(1) algorithm
    ###################################
    def muiltipleNum( multifier , below ):
        res = (below-1) // multifier
        return res

    def sumOfMutiples( n , below ):
        return ( n + muiltipleNum( n , below )*n ) * muiltipleNum( n , below ) // 2

    t1 = time.time()
    print( sumOfMutiples( 3 , 1000) + sumOfMutiples( 5 , 1000) - sumOfMutiples( 15 , 1000 ) )
    t2 = time.time()

    print("Thinking 2 - time:",t2-t1,"s")
