def gcd( a , b ):
    if a < b:
        a,b = b,a
    if a%b == 0:
        return b
    return gcd( b , a%b )


def solve( N , e ):

    N -= 1
    resn = e[N]
    resd = 1

    for i in range( N-1 , -1 , -1 ):
        resn , resd = resd , resn
        resn += e[i]*resd

        resgcd = gcd( resn , resd )
        resn //= resgcd
        resd //= resgcd

    return sum( [ int(x) for x in str(resn)] )
        
    
if __name__ == "__main__":

    N = 10000
    
    e = [2]
    for i in range(1,N+1):
        e += [1,2*i,1]

    #print( e )

    print( solve( int( input() ) , e ) )
