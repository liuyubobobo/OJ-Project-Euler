import math
import time

#################################
## Thinking 1 - Original Thinking
#################################
def solve(s):
    if s%2 == 1:
        return -1
    for i in range(1,s-1):
        for j in range(i+1,s-i):
            x = math.sqrt(i*i + j*j)
            c = int(x)
            if i*i + j*j == c*c and c > j and i+j+c == s:
                return i*j*c
    return -1

def solve_abc(s):
    if s%2 == 1:
        return None,None,None
    #print("start",s)
    for i in range(1,s-1):
        for j in range(i+1,s-i):
            x = math.sqrt(i*i + j*j)
            c = int(x)
            if i*i + j*j == c*c and c > j and i+j+c == s:
                return i,j,c
    return None,None,None


##################################################
## Thinking 2
## -- a better bound.
## -- at loop 2, you know c is at leat i + 2
## ---- so j can be iterate from i+1 to 1000-2*i-1
##################################################
def solve2(s):
    if s%2 == 1:
        return -1
    for i in range(1,s-1):
        for j in range(i+1,s-2*i-1):
            x = math.sqrt(i*i + j*j)
            c = int(x)
            if i*i + j*j == c*c and c > j and i+j+c == s:
                return i*j*c

def solve2_abc(s):
    if s%2 == 1:
        return None,None,None
    #print("start",s)
    for i in range(1,s-1):
        for j in range(i+1,s-2*i-1):
            x = math.sqrt(i*i + j*j)
            c = int(x)
            if i*i + j*j == c*c and c > j and i+j+c == s:
                return i,j,c
    return None,None,None


######################################################
## Thinking 3
## -- No need to use sqrt when you choose i and j
## -- use 1000-i-j instead of check it in if statement
######################################################
def solve3(s):
    if s%2 == 1:
        return -1
    for i in range(1,s-1):
        for j in range(i+1,s-2*i-1):
            c = s-i-j
            if i*i + j*j == c*c and c > j:
                return i*j*c
    return -1

def solve3_abc(s):
    if s%2 == 1:
        return None,None,None
    #print("start",s)
    for i in range(1,s-1):
        for j in range(i+1,s-2*i-1):
            c = 1000-i-j
            if i*i + j*j == c*c and c > j:
                return i,j,c
    return None,None,None
            

######################################################
## Thinking 4
## -- a much more better bound
## -- i should not be larger than 1000/3
## -- j should not be larger than (1000-i)/2
######################################################
def solve4(s):
    if s%2 == 1:
        return -1
    for i in range(1,(s-3)//3+1):
        for j in range(i+1,(s-i)//2+1):
            c = s-i-j
            if i*i + j*j == c*c:
                return i*j*c
    return -1

def solve4_abc(s):
    if s%2 == 1:
        return None,None,None
    #print("start",s)
    for i in range(1,(s-3)//3+1):
        for j in range(i+1,(s-i)//2+1):
            c = s-i-j
            if i*i + j*j == c*c:
                return i,j,c
    return None,None,None


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
def solve5(s):
    if s%2 == 1:
        return -1
    s2 = s//2
    m = 1
    while m*m < s2:
        if s2%m == 0:
            sm = s2 // m
            while sm%2 == 0:
                sm//=2
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
        m += 1
        
        return -1

def solve5_abc(s):
    if s%2 == 1:
        return None,None,None
    
    s2 = s// 2
    m = 1
    while m*m < s2:
        if s2%m == 0:
            sm = s2 // m
            while sm%2 == 0:
                sm//=2
            k = m+2 if m%2==1 else m+1
            while k < 2*m and k <= sm:
                if sm%k == 0 and gcd(k,m) == 1:
                    d = s2//(k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    if a > b:
                        a,b = b,a
                    c = d*(m*m+n*n)
                    return a,b,c
                k = k + 2
        m += 1

    return None,None,None
                
def gcd(a,b):
    if a<b: a,b = b,a
    if a%b == 0:return b
    return gcd(b,a%b)
            

            
if __name__ == "__main__":

    '''
    t1 = time.time()
    print( solve(1000))
    t2 = time.time()
    print("Thinking 1 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve2(1000))
    t2 = time.time()
    print("Thinking 2 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve3(1000))
    t2 = time.time()
    print("Thinking 3 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve4(1000))
    t2 = time.time()
    print("Thinking 4 - time:",t2-t1,"s")
    print("-"*50)

    # -----------------------------------

    t1 = time.time()
    print( solve5(1000))
    t2 = time.time()
    print("Thinking 5 - time:",t2-t1,"s")
    print("-"*50)
    '''

    ## Big Data Test
    print("Big Data Test")
    t1 = time.time()
    for s in range(1,3001):
        a,b,c = solve5_abc(s)
        if s%2 == 0:
            if a != None:
                if a*a + b*b != c*c or a+b+c != s or a>= b or b>=c or a>= c:
                    print("WA [",s,"] :",a,b,c,"!"*50)
            ## double check
            '''
            else:
                #print("test",s,"again:")
                a,b,c = solve_abc(s)
                if a!= None:
                    print("WA [",s,"not found] :",a,b,c,"!"*50)
            '''
    t2 = time.time()
    print("Thinking 1 - time:",t2-t1,"s")
    print("-"*50)

