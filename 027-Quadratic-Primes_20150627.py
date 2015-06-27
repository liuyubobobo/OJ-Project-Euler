#################################################################################
## isPrime
## -- determine a given number x is a prime number
## ---- All primes except 2 are odd
## ---- All primes greater than 3 can be written in the form of 6*k+/-1
## ---- Any number n can have only one primefactor greater than sqrt(x)
## ---- The conseguence for primality testing of a number n is:
## ------ if we cannot find a number f less than or equal sqrt(n) that divides x,
## ------ Then x is prime, the only primefactor of x is x itself
#################################################################################
def isPrime( x ):
    if x <= 1:
        return False
    elif x < 4:
        return True
    elif x&1 == 0:
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

#################
## gcd( a , b )
#################
def gcd( a , b ):
    if a < b:
        a,b = b,a
    if b == 0:
        return 0
    if a%b == 0:
        return b
    return gcd( b , a%b )


if __name__ == "__main__":

    longestLen = 0
    res = 0
    for b in range(-1000,1001):
        if not isPrime(abs(b)):
            continue
        
        for a in range(-1000,1001):

            if a != 0:
                x = gcd( abs(a),abs(b))
                if x != 1 and x+1 < longestLen:
                    continue

            if abs(b) + 1 < longestLen or abs(b-a) + 1 < longestLen:
                continue
            
            n = 1
            while isPrime( n*( n + a ) + b ):
                n += 1

            if n > longestLen:
                longestLen = n
                res = a*b


    print(res)
