class RationalNumber:

    def __init__( self , a , b ):
        self.a = a
        self.b = b


def gcd2( a, b ):
    if a < b:
        a,b = b,a

    if b == 0:
        return 1

    while a%b != 0:
        a , b = b , a%b

    return b


def sign( x ):

    if x > 0:
        return 1
    elif x == 0:
        return 0
    return -1


def add( r1 , r2 ):

    a = r1.a * r2.b + r2.a * r1.b
    signa = sign(a)
    b = r1.b * r2.b
    signb = sign(b)
    g = gcd2( abs(a) , abs(b) )

    if signa*signb >= 0:
        return RationalNumber( a//g , b//g )
    return RationalNumber( -a//g , b//g )


def sub( r1 , r2 ):

    a = r1.a * r2.b - r2.a * r1.b
    signa = sign(a)
    b = r1.b * r2.b
    signb = sign(b)
    g = gcd2( abs(a) , abs(b) )

    if signa*signb >= 0:
        return RationalNumber( a//g , b//g )
    return RationalNumber( -a//g , b//g )


def mul( r1 , r2 ):

    a = r1.a * r2.a
    signa = sign(a)
    b = r1.b * r2.b
    signb = sign(b)
    g = gcd2( abs(a) , abs(b) )

    if signa*signb >= 0:
        return RationalNumber( a//g , b//g )
    return RationalNumber( -a//g , b//g )


def div( r1 , r2 ):

    a = r1.a * r2.b
    signa = sign(a)
    b = r1.b * r2.a
    signb = sign(b)
    g = gcd2( abs(a) , abs(b) )

    if signa*signb >= 0:
        return RationalNumber( a//g , b//g )
    return RationalNumber( -a//g , b//g )

    
def nextPermutationByLex(arr):

    k = -1
    for i in range( len(arr)-2 , -1 , -1 ):
        if arr[i] < arr[i+1]:
            k = i
            break

    if k == -1:
        return False
    #print("k =",k)
    
    #l = k + 1
    #for i in range( k+1 , len(arr) ):
    #    if arr[i] > arr[k]:
    #        l = i
    for i in range( len(arr)-1 , k , -1 ):
        if arr[i] > arr[k]:
            l = i
            break
    #print("l =",l)
    
    arr[k],arr[l] = arr[l],arr[k]
    arr[k+1:] = list( reversed(arr[k+1:]))

    #print("result:",arr)
    #print("------")
    
    return True


def genPermutationByLex( elements ):
    #assert( isinstance( elements , list ) )
    arr = sorted(elements)
    yield arr[:]

    while nextPermutationByLex(arr):
        yield arr[:] 


def solve( m , nums ):

    resSet = set()

    for anums in genPermutationByLex( nums ):
        tnums = [ RationalNumber(x,1) for x in anums]
        __solve( tnums , resSet )
    #res = sorted( list( resSet ) )
    #print( res )

    n = 1
    while n in resSet:
        n += 1

    return n - 1


def __solve( nums , res ):

    if len( nums ) == 1:
        if nums[0].b == 1:
            res.add( nums[0].a )
            res.add( -nums[0].a )
        return

    for i in range( len(nums) - 1 ):

        tnums = nums[:]
        tnums[i:i+2] = [add( nums[i] , nums[i+1] )]
        __solve( tnums , res )

        tnums[i] = sub( nums[i] , nums[i+1] )
        __solve( tnums , res )

        tnums[i] = mul( nums[i] , nums[i+1] )
        __solve( tnums , res )

        tnums[i] = div( nums[i] , nums[i+1] )
        if tnums[i].b != 0:
            __solve( tnums , res )
    
    
if __name__ == "__main__":

    MAXN = 10
    maxres = 0
    res = ""
    for a in range( 1 , MAXN + 1 - 3  ):
        for b in range( a+1 , MAXN + 1 - 2 ):
            for c in range( b + 1 , MAXN + 1 - 1 ):
                for d in range( c + 1 , MAXN + 1 ):
                    tres = solve( 4 , [a,b,c,d] )
                    if tres > maxres:
                        maxres = tres
                        res = str(a) + str(b) + str(c) + str(d)

    print( maxres )
    print( res )
