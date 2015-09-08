import time

def solve( N ):

    #parr = []
    res = 0
    stack = [(3,4,5,-1)]
    while len(stack) != 0:

        t = list(stack.pop())
        #if sum(t) > N:
        #    continue

        t.sort()
        #print( "check" , t )

        c = 1
        while True:
            tt = [c*x for x in t[1:]]
            tag = t[0]
            if sum(tt) > N or abs(tt[2] - 2*tt[0]) > 2:
                break

            if tt[2]%2 == 0:
                if abs( tt[2]//2 - tt[0] ) == 1:
                    res += tt[2] + tt[0]
                    print( tt[2]//2 , tt[2]//2 , tt[0] )
                    print( "tag:" , tag )
                    print( res )
                    #parr.append( tt[2] + tt[0] )
                    #print( parr )
                if abs( tt[2]//2 - tt[1] ) == 1:
                    res += tt[2] + tt[1]
                    print( tt[2]//2 , tt[2]//2 , tt[1] )
                    print( "tag:" , tag )
                    print( res )
                    #parr.append( tt[2] + tt[0] )
                    #print( parr )
            c += 1

        t = t[1:]
        if 5*(t[0]-t[1]) + 7*t[2] <= N:
            stack.append( ( t[0]-2*t[1]+2*t[2] , 2*t[0]-t[1]+2*t[2] , 2*t[0]-2*t[1]+3*t[2] , -3 ) )
        if 5*(t[0]+t[1]) + 7*t[2] <= N:
            stack.append( ( t[0]+2*t[1]+2*t[2] , 2*t[0]+t[1]+2*t[2] , 2*t[0]+2*t[1]+3*t[2] , -2 ) )

        #######################################################
        ## It seems only this branch can get the right solution
        ## Don't know wht yet...
        #######################################################
        if 5*(t[1]-t[0]) + 7*t[2] <= N:
            stack.append( ( -t[0]+2*t[1]+2*t[2] , -2*t[0]+t[1]+2*t[2] , -2*t[0]+2*t[1]+3*t[2] , -1 ) )

        #print( "len of stack =" , len(stack) )

    print( "="*50 )
    return res

if __name__ == "__main__":

    n = 18
    N = 10**n
    print( "solve N = 10^%d" % n )
    
    t1 = time.time()
    print( solve( N ) )
    t2 = time.time()
    print( "complete" )
    print( "time :" , t2-t1 , "s" )
