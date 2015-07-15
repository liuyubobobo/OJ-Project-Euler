import math

def isSquare( x ):
    sqrt_num = int(math.sqrt(x))
    if sqrt_num * sqrt_num == x:
        return True , sqrt_num
    return False , -1

######################################################
## Because every H is also a T , so no need to check T
######################################################
def isT( x ):
    ok , sqrt_x = isSquare( 1 + 8 * x )
    return ok

def isP( x ):
    ok , sqrt_x = isSquare( 1 + 24*x )
    return ok and ( 1 + sqrt_x ) % 6 == 0

if __name__ == "__main__":

    i = 144
    while True:
        Hn = i*(2*i-1)

        ######################################################
        ## Because every H is also a T , so no need to check T
        ######################################################
        #if isT( Hn ) and isP( Hn ):
        if isP( Hn ):
            print( Hn )
            break
        i += 1
