import time
import functools 
###########################
## Thinking 1: Brutal Force
###########################
def solve1( N ):
    res = set()
    for a in range(2,N+1):
        for b in range(2,N+1):
            res.add( a**b )
    return len(res)


###############################################
## Thinking 2: Using a^n when calculate a^(n+1)
###############################################
def solve2( N ):
    res = set()
    for a in range(2,N+1):
        x = a*a
        res.add( x )
        for b in range(3,N+1):
            x *= a
            res.add( x )
    #print(sorted(res))
    return len(res)


######################################################
## Thinking 3:Using mathematic to calculate the number
## -- Only perfect power number can be repeated
######################################################
def solve3( N ):

    res = [0] * (N+1)
    for a in range(2,N+1):
        fac = factorize( a )
        p = list(fac.keys())
        v = list(fac.values())
        #print( a )
        #print( p )
        #print( v )

        isPerfectPower , m , k = calcPerfectPower( p , v )
        if isPerfectPower:
            #print(a,"is a perfect number. a = ",m,"^",k)

            for j in range( N//k+1 , N+1 ):
                jk = j*k
                if jk > (k-1)*N:
                    res[a] += N-j+1
                    break

                #print("j =",j,", k =",k,", check",j*k)

                tier = (jk - 1)//N + 1
                ok = True
                for d in range(tier,k):
                    if jk % d == 0:
                        ok = False
                        break
                if ok:
                    res[a] += 1

        else:
            res[a] += N-2+1
            #print(a,"is not a perfect numer. res[",a,"] = ",res[a])

        #print(res)
    return sum(res)

def calcPerfectPower( p , v ):
    if len( p ) == 1:
        if v[0] == 1:
            return False , 0 , 0
        else:
            return True , p[0] , v[0]

    k = v[0]
    for i in range(1,len(v)):
        k = gcd( k , v[i] )

    if k == 1:
        return False , 0 , 0

    m = 1
    for i in range( len(p) ):
        m *= p[i]**(v[i]//k)

    return True , m , k

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

#################
## gcd( a , b )
#################
def gcd( a , b ):
    if a < b:
        a,b = b,a
    if a%b == 0:
        return b
    return gcd( b , a%b )


def test( func , N , title ):
    print("="*50)
    print( title )
    t1 = time.time()
    print( func(N) )
    t2 = time.time()
    print( title , "- time:" , t2-t1 , "s" )
    print("="*50,"",sep="\n")
    
    
if __name__ == "__main__":

    N = 100000

    # Check rightness
    # print( solve3( N ) )

    # Check time complexity
    #test( solve1 , N , "Thinking  1")
    #test( solve2 , N , "Thinking  2")
    test( solve3 , N , "Thinking  3")
