import math

def solve( target ):
    
    best = target+1
    area = 0

    a = 1
    while True:

        #b = a
        b = int( math.sqrt( 4*target//(a*a+a) ) )
        while True:
            cnt = a*b*(a+1)*(b+1)//4
            diff = abs( cnt - target )
            if diff < best:
                best = diff
                area = a*b
                #print("a = %d , b = %d , area = %d , bestdiff = %d" % ( a , b , area , best ) )
            elif diff == best:
                area = max( area , a*b )

            if cnt > target + best:
                break

            b += 1
            
        a += 1
        if a*a*(a+1)*(a+1)//4 > target + best:
            break

    #print( "best :" , best ) 
    #print( "area :" , area
    return area


if __name__ == "__main__":

    print( solve( 2000000 ) )
            

    
