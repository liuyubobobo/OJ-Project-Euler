def ok( num ):

    onum = num
    
    turn = 0
    while turn < 50:

        turn += 1
        
        num = num + int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            #print( onum , ":" , num , ", iter:" , turn )
            return True

    return False


def solve( N ):

    res = 0
    for i in range( N ):
        if ok( i ):
            res += 1

    return N - res


if __name__ == "__main__":

    print( solve( 10000 ) )
