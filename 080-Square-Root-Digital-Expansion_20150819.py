#######################################
## Using Python built-in decimal module
#######################################
import decimal

def test():

    print("test")
    decimalSqrtNumS = str( decimal.Decimal(2).sqrt() )
    dotpos = decimalSqrtNumS.index(".")
    print( "dotpos =" , dotpos )

    intpart = sum( [int(x) for x in decimalSqrtNumS[:dotpos]] )
    print( "int part is:" , decimalSqrtNumS[:dotpos] )
    print( "sum of intpart =" , intpart )
    
    decimalpart = 0
    for i in range( dotpos + 1 , dotpos + 1 + 100 - dotpos ):
        decimalpart += int( decimalSqrtNumS[i] )
    print( "decimal part is:" , decimalSqrtNumS[dotpos+1:dotpos+1+100-dotpos] )
    print( "sum of decimalpart =" , decimalpart)

    print( "sum =" , intpart + decimalpart )
    print("="*50)
    
    
if __name__ == "__main__":

    N = 100
    decimal.getcontext().prec = 105

    #test()
    
    squareNumbers = set()
    num = 1
    while num*num <= N:
        squareNumbers.add( num*num )
        num += 1
    print( "Square Numbers:" , squareNumbers )

    
    res = 0
    for num in range( 1 , N+1 ):
        if num in squareNumbers:
            continue
        
        decimalSqrtNumS = str( decimal.Decimal(num).sqrt() )
        #print( num , ":" , decimalSqrtNumS )
        dotpos = decimalSqrtNumS.index(".")
        #print( "dotpos =" , dotpos)
        #print( "len =" , len(decimalSqrtNumS) )
        #assert( len(str(decimalSqrtNumS[dotpos+1:])) >= 100 )

        res += sum( [int(x) for x in decimalSqrtNumS[:dotpos]] )
        res += sum( [int(x) for x in decimalSqrtNumS[dotpos+1:dotpos+1+100-dotpos]] )
        #print( res )

    print(res)
