############################################################
## If we know the upper bound of the number we need to check
## We can then use a prime-shieve-like algorihtm
## The details can refer to hackerranck.com Problem 047
############################################################


##################
## The brute Force
##################
def ok( N ):
    res = 0
    if N%2 == 0:
        res += 1
        while N%2 == 0:
            N //= 2

    x = 3
    while x*x <= N:
        if N % x == 0:
            res += 1
            while N%x == 0: N //= x
        x += 2

    if N != 1:
        res += 1

    return res == 4


if __name__ == "__main__":
    
    num = 2*3*5*7 + 1
    oknum = 1
    while True:
        if ok( num ):
            oknum += 1
            if oknum == 4:
                print( num - 3 )
                break
        else:
            oknum = 0

        num += 1

    
