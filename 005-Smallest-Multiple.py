import time
import math

def findAllPrimes( MAX_NUM ):
    if MAX_NUM < 2:
        return []

    res = [2]
    for i in range(3,MAX_NUM,2):
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
    
def gcd(a,b):
    if a<b:
        a,b = b,a
    if a%b == 0:
        return b
    return gcd(b,a%b)

def lcm(a,b):
    return (a//gcd(a,b))*b

if __name__ == "__main__":

    MAX_NUM = 20000

    #############################
    ## Thinking 1
    ## - Call lcm through 1 to 20
    #############################
    t1 = time.time()
    res = 1
    for i in range(2,MAX_NUM+1):
        res = lcm(res,i)
    t2 = time.time()
    print(res)
    print("Thinking 1 - time:",t2-t1,"s")
    print("-"*50)

    ##----------------------------------------------

    #######################################################
    ## Thinking 2
    ## - the res = p[0]^a[0]+p[1]^a[1]+...+p[m]^a[m]
    ## - p[i] is all prime factor less than n
    ## - a[i] is the max number make p[i]^a[i] < n
    ## - to find out a[i], we conclude a[i]*log(p[i])<log(n)
    ## ---- a[i] < log(n)/log(p[i])
    ## ---- a[i] = floor( log(n) / log(p[]i) )
    ########################################################
    t1 = time.time()
    allPrimes = findAllPrimes(MAX_NUM+1)
    res = 1
    for i in range(0,len(allPrimes)):
        res *= allPrimes[i]**math.floor( math.log(MAX_NUM)/math.log(allPrimes[i]) )
    t2 = time.time()

    #print(allPrimes)
    print(res)
    print("Thinking 2 - time:",t2-t1,"s")
