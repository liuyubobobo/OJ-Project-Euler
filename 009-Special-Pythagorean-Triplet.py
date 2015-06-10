import math
import time

#################################
## Thinking 1 - Original Thinking
#################################
def solve():
    for i in range(1,999):
        for j in range(i+1,1000-i):
            x = math.sqrt(i*i + j*j)
            c = int(x)
            if i*i + j*j == c*c and c > j and i+j+c == 1000:
                return i*j*c


##################################################
## Thinking 2
## -- a better bound.
## -- at loop 2, you know c is at leat i + 2
## ---- so j can be iterate from i+1 to 1000-2*i-1
##################################################
def solve2():
    for i in range(1,999):
        for j in range(i+1,1000-2*i-1):
            x = math.sqrt(i*i + j*j)
            c = int(x)
            if i*i + j*j == c*c and c > j and i+j+c == 1000:
                return i*j*c


######################################################
## Thinking 3
## -- No need to use sqrt when you choose i and j
## -- use 1000-i-j instead of check it in if statement
######################################################
def solve3():
    for i in range(1,999):
        for j in range(i+1,1000-2*i-1):
            c = 1000-i-j
            if i*i + j*j == c*c and c > j:
                return i*j*c


######################################################
## Thinking 4
## -- a much more better bound
## -- i should not be larger than 1000/3
## -- j should not be larger than (1000-i)/2
######################################################
def solve4():
    for i in range(1,(1000-3)//3+1):
        for j in range(i+1,(1000-i)//2+1):
            c = 1000-i-j
            if i*i + j*j == c*c:
                return i*j*c


###############################################################################
## Thinking 5
## -- for a*a + b*b = c*c
## -- we can transform a,b,c as a = (m^2-n^2)*d , b = 2mn*d , c = (m^2 + n^2)*d
## -- in this case, gcd( m^2-n^2 , 2mn , m^2 + n^2 ) = 1
## ---- so that between m and n, there's exact one even and one odd
## -- so a + b + c = 2m(m+n)d = s(1000 in this problem)
## -- we can walk through m from 2 to sqrt(s/2)
## ---- Because m*(m+n)>s/2 ==> m < sqrt(s/2)
## -- then figure out m+n(=k), k >= m
## ---- Becasue m^2 - n^2 > 0 ==> m > n ==> k < 2*m
## -- When we get m and m+n, we can figure out d, then a, b and c
###############################################################################
def solve5():
    s2 = 500    ## 1000// 2
    mlimit = int( math.ceil( math.sqrt(s2) ) )
    for m in range(2,mlimit):
        if s2%m == 0:
            sm = s2 // m
            #while sm%2 == 0:
            #    sm//=2
            k = m+2 if m%2==1 else m+1
            while k < 2*m and k <= sm:
                if sm%k == 0 and gcd(k,m) == 1:
                    d = s2//(k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    c = d*(m*m+n*n)
                    return a*b*c
                k = k + 2

def gcd(a,b):
    if a<b: a,b = b,a
    if a%b == 0:return b
    return gcd(b,a%b)
            

            
if __name__ == "__main__":

    t1 = time.time()
    print( solve())
    t2 = time.time()
    print("Thinking 1 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve2())
    t2 = time.time()
    print("Thinking 2 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve3())
    t2 = time.time()
    print("Thinking 3 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve4())
    t2 = time.time()
    print("Thinking 4 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve5())
    t2 = time.time()
    print("Thinking 5 - time:",t2-t1,"s")
    print("-"*50)
