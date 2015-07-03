import functools

def gcd( a , b ):
    if a < b:
        a,b = b,a
    if a%b == 0:
        return b
    return gcd( b , a%b )

if __name__ == "__main__":

    numerator = []
    denominator = []
    for i in range(10,100):
        for j in range(i+1,100):
            if i%10 != 0 and j%10!= 0:
                iarr = [i//10,i%10]
                jarr = [j//10,j%10]

                e1 = i//10
                e2 = i%10
                if e1 not in jarr and e2 not in jarr:
                    continue
                
                if e1 in jarr:
                    del iarr[ iarr.index(e1) ]
                    del jarr[ jarr.index(e1) ]
                elif e2 in jarr:
                    del iarr[ iarr.index(e2) ]
                    del jarr[ jarr.index(e2) ]

                a = iarr[0]
                b = jarr[0]
                if a > b:
                    continue

                gcdij = gcd(i,j)
                gcdab = gcd(a,b)

                
                if i//gcdij == a//gcdab and j//gcdij == b//gcdab:
                    numerator.append( i// gcdij )
                    denominator.append( j//gcdij )
                    #print( "FOUND!!!" , i , j , a , b )
                    #print( i// gcdij , "/" , j//gcdij )

    x = functools.reduce( lambda x,y:x*y , numerator , 1 )
    y = functools.reduce( lambda x,y:x*y , denominator , 1 )

    print( x , y )
    print( x//gcd(x,y) , y//gcd(x,y) )
                    
                    
            
