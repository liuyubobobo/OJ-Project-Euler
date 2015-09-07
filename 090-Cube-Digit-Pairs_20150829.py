def chooseCubes():

    res = []
    __chooseCubes( 0 , [x for x in range(10)] , [] , res )
    return res


def __chooseCubes( index , scope , tres , res ):

    if len( tres ) == 6:
        res.append( tres[:] )
        return

    for i in range( index , len(scope) - ( 6 - len(tres) ) + 1 ):
        tres.append( scope[i] )
        __chooseCubes( i + 1 , scope , tres , res )
        tres.pop()


def ok( p1 , p2 , t1 , t2 ):

    if 6 in p1:
        p1.add(9)
    if 9 in p1:
        p1.add(6)

    if 6 in p2:
        p2.add(9)
    if 9 in p2:
        p2.add(6)

    for i in range( len(t1) ):
        if not ( ( t1[i] in p1 and t2[i] in p2 ) or ( t1[i] in p2 and t2[i] in p1 ) ):
            return False
        
    return True

        
if __name__ == "__main__":

    cubes = chooseCubes()
    #print( len(cubes) )

    t1 = [0,0,0,1,2,3,4,6,8]
    t2 = [1,4,9,6,5,6,9,4,1]
    res = 0
    for i in range( len(cubes) ):
        for j in range( i , len(cubes) ):
            d1 = cubes[i]
            d2 = cubes[j]
            if ok( set(d1) , set(d2) , t1 , t2 ):
                res += 1
    print( res )
