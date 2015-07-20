#######################################################################################
## Integer Partition Problem
## -- Refer to https://en.wikipedia.org/wiki/Partition_(number_theory)
## -- A tutorial can be found here: http://www.mathblog.dk/project-euler-78-coin-piles/
#######################################################################################
def solve():

    MOD = 10**6
    
    p = [1]

    n = 1
    while True:

        i = 0
        penta = 1
        p.append(0)
        while penta <= n:
            sign = -1 if i%4 > 1 else 1
            p[n] += sign * p[ n - penta ]
            p[n] %= MOD

            i += 1
            j = i//2 + 1 if i%2 == 0 else - ( i//2 + 1 )
            penta = j * ( 3 * j - 1 ) // 2

        if p[n] == 0:
            return n

        n += 1
    

if __name__ == "__main__":

    print( solve())
