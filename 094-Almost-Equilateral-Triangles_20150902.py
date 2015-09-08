import time

def solve( N ):

    res = 0
    stack = [(3,4,5)]
    while len(stack) != 0:

        t = list(stack.pop())
        if sum(t) > N:
            continue

        t.sort()
        #print( "check" , t )

        c = 1
        while True:
            tt = [c*x for x in t]
            if abs(tt[2] - 2*tt[0]) > 2:
                break

            if tt[2]%2 == 0:
                if abs( tt[2]//2 - tt[0] ) == 1:
                    res += tt[2] + tt[0]
                    print( tt[2]//2 , tt[2]//2 , tt[0] )
                    print( res )
                if abs( tt[2]//2 - tt[1] ) == 1:
                    res += tt[2] + tt[1]
                    print( tt[2]//2 , tt[2]//2 , tt[1] )
                    print( res )
            c += 1

        stack.append( ( t[0]-2*t[1]+2*t[2] , 2*t[0]-t[1]+2*t[2] , 2*t[0]-2*t[1]+3*t[2] ) )
        stack.append( ( t[0]+2*t[1]+2*t[2] , 2*t[0]+t[1]+2*t[2] , 2*t[0]+2*t[1]+3*t[2] ) )
        stack.append( ( -t[0]+2*t[1]+2*t[2] , -2*t[0]+t[1]+2*t[2] , -2*t[0]+2*t[1]+3*t[2] ) )

    print( "="*50 )
    return res

if __name__ == "__main__":

    N = 10**9

    t1 = time.time()
    print( solve(N) )
    t2 = time.time()
    print( "time :" , t2-t1 , "s" )
