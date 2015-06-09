def getItemOfArithmeticSequence( a , d , n ):
    return a + (n-1)*d

def sumOfArithmeticSequence( a , d , n ):
    return ( a + a + (n-1)*d ) * n // 2

def sumOfSquares(n):
    return n*(n+1)*(2*n+1)//6

if __name__ == "__main__":

    N = 100

    print( sumOfArithmeticProgression( 1 , 1 , N )**2 - sumOfSquares(N) )
