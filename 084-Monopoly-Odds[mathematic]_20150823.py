import random
import time

def getMWithoutDoubleRules( face ):

    prob = [0]*(2*face+1)
    for i in range( 1 , face+1 ):
        for j in range( 1 , face+1 ):
            prob[i+j] += 1
    for i in range( 2*face + 1 ):
        prob[i] /= face*face
        
    #print( sum(prob) )
        
    M = [[0]*40 for i in range(40)]
    for i in range( 40 ):

        for j in range( 2 , 2*face+1 ):
            nextPos = ( i + j ) % 40
            
            if nextPos == 30:
                M[i][10] += prob[j]
            elif nextPos in [2,17,33]:
                ##CC
                M[i][0] += prob[j] / 16
                M[i][10] += prob[j] / 16
                M[i][nextPos] += prob[j] * 7 / 8
            elif nextPos in [7,22,36]:
                ##CH
                M[i][0] += prob[j] / 16
                M[i][10] += prob[j] / 16
                M[i][11] += prob[j] / 16
                M[i][24] += prob[j] / 16
                M[i][39] += prob[j] / 16
                M[i][5] += prob[j] / 16

                if nextPos == 7:
                    M[i][15] += prob[j] / 8
                elif nextPos == 22:
                    M[i][25] += prob[j] / 8
                else:
                    assert( nextPos == 36 )
                    M[i][5] += prob[j] / 8

                if nextPos == 22:
                    M[i][28] += prob[j] / 16
                else:
                    assert( nextPos in [7, 36] )
                    M[i][12] += prob[j] / 16

                if nextPos == 36:
                    M[i][33] += prob[j] * 14 / ( 16 * 16 )
                    M[i][0] += prob[j] / ( 16 * 16 )
                    M[i][10] += prob[j] / ( 16 * 16 )
                else:
                    assert( nextPos in [7, 22] )
                    M[i][nextPos-3] += prob[j] / 16
                    
                M[i][nextPos] += prob[j] * 3 / 8
                
            else:
                M[i][nextPos] += prob[j]

            #print("roll" , j , ":" , sum(prob[:j+1]) - sum(M[i]))
            #input()

    #for i in range(40):
    #    print( i , ":" , sum(M[i]) )

    return M


def solveWithoutDoubleRules( face ):

    M = getMWithoutDoubleRules( face )

    t1 = time.time()
    p = [0]*40
    p[0] = 1

    #turn = 0
    #while True:
    #    p = matrixMultiple( p , M )
    #    if time.time() - t1 > 10:
    #        break
    #    turn += 1
    #print("turn :" , turn )
    #print(p)

    for t in range( 100000 ):
        p = matrixMultiple( p , M )
    #print(p)

    res = []
    for i in range(40):
        res.append( (p[i],i) )

    res.sort( key = lambda x: -x[0] )
    for aRes in res:
        print( aRes[1] , ":" , int(aRes[0]*100000)/1000 , "%" )



def getM( face ):

    prob = [0]*(2*face+1)
    for i in range( 1 , face+1 ):
        for j in range( 1 , face+1 ):
            prob[i+j] += 1
    for i in range( 2*face + 1 ):
        prob[i] /= face*face

    doubleProb = 1 / (face*face)
    #print( sum(prob) )
        
    M = [[0]*120 for i in range(120)]
    for i in range( 120 ):
        doubleNumber = i//40
        curPos = i%40
        for j in range( 2 , 2*face+1 ):
            nextPos = ( curPos + j ) % 40
            
            if nextPos == 30:
                if j&1 == 1:
                    M[i][10] += prob[j]
                else:
                    if doubleNumber < 2:
                        M[i][(doubleNumber+1)*40+10] += doubleProb
                    else:
                        M[i][10] += doubleProb

                    M[i][10] += prob[j] - doubleProb
                    
            elif nextPos in [2,17,33]:
                ##CC
                if j&1 == 1:
                    M[i][0] += prob[j] / 16
                    M[i][10] += prob[j] / 16
                    M[i][nextPos] += prob[j] * 7 / 8
                else:
                    if doubleNumber < 2:
                        M[i][(doubleNumber+1)*40+0] += doubleProb / 16 
                        M[i][(doubleNumber+1)*40+10] += doubleProb / 16 
                        M[i][(doubleNumber+1)*40+nextPos] += doubleProb * 7 / 8 
                    else:
                        M[i][10] += doubleProb

                    M[i][0] += ( prob[j] - doubleProb ) / 16 
                    M[i][10] += ( prob[j] - doubleProb ) / 16
                    M[i][nextPos] += ( prob[j] - doubleProb ) * 7 / 8
                    
            elif nextPos in [7,22,36]:
                ##CH
                if j&1 == 1:
                    M[i][0] += prob[j] / 16
                    M[i][10] += prob[j] / 16
                    M[i][11] += prob[j] / 16
                    M[i][24] += prob[j] / 16
                    M[i][39] += prob[j] / 16
                    M[i][5] += prob[j] / 16

                    if nextPos == 7:
                        M[i][15] += prob[j] / 8
                    elif nextPos == 22:
                        M[i][25] += prob[j] / 8
                    else:
                        assert( nextPos == 36 )
                        M[i][5] += prob[j] / 8

                    if nextPos == 22:
                        M[i][28] += prob[j] / 16
                    else:
                        assert( nextPos in [7, 36] )
                        M[i][12] += prob[j] / 16

                    if nextPos == 36:
                        M[i][33] += prob[j] * 14 / ( 16 * 16 )
                        M[i][0] += prob[j] / ( 16 * 16 )
                        M[i][10] += prob[j] / ( 16 * 16 )
                    else:
                        assert( nextPos in [7, 22] )
                        M[i][nextPos-3] += prob[j] / 16
                    
                    M[i][nextPos] += prob[j] * 3 / 8

                else:
                    if doubleNumber < 2:

                        M[i][(doubleNumber+1)*40+0] += doubleProb / 16
                        M[i][(doubleNumber+1)*40+10] += doubleProb / 16
                        M[i][(doubleNumber+1)*40+11] += doubleProb / 16
                        M[i][(doubleNumber+1)*40+24] += doubleProb / 16
                        M[i][(doubleNumber+1)*40+39] += doubleProb / 16
                        M[i][(doubleNumber+1)*40+5] += doubleProb / 16

                        if nextPos == 7:
                            M[i][(doubleNumber+1)*40+15] += doubleProb / 8
                        elif nextPos == 22:
                            M[i][(doubleNumber+1)*40+25] += doubleProb / 8
                        else:
                            assert( nextPos == 36 )
                            M[i][(doubleNumber+1)*40+5] += doubleProb / 8

                        if nextPos == 22:
                            M[i][(doubleNumber+1)*40+28] += doubleProb / 16
                        else:
                            assert( nextPos in [7, 36] )
                            M[i][(doubleNumber+1)*40+12] += doubleProb / 16

                        if nextPos == 36:
                            M[i][(doubleNumber+1)*40+33] += doubleProb * 14 / ( 16 * 16 )
                            M[i][(doubleNumber+1)*40+0] += doubleProb / ( 16 * 16 )
                            M[i][(doubleNumber+1)*40+10] += doubleProb / ( 16 * 16 )
                        else:
                            assert( nextPos in [7, 22] )
                            M[i][(doubleNumber+1)*40+nextPos-3] += doubleProb / 16
                    
                        M[i][(doubleNumber+1)*40+nextPos] += doubleProb * 3 / 8

                    else:
                        M[i][10] += doubleProb

                    M[i][0] += ( prob[j] - doubleProb ) / 16
                    M[i][10] += ( prob[j] - doubleProb ) / 16
                    M[i][11] += ( prob[j] - doubleProb ) / 16
                    M[i][24] += ( prob[j] - doubleProb ) / 16
                    M[i][39] += ( prob[j] - doubleProb ) / 16
                    M[i][5] += ( prob[j] - doubleProb ) / 16

                    if nextPos == 7:
                        M[i][15] += ( prob[j] - doubleProb ) / 8
                    elif nextPos == 22:
                        M[i][25] += ( prob[j] - doubleProb ) / 8
                    else:
                        assert( nextPos == 36 )
                        M[i][5] += ( prob[j] - doubleProb ) / 8

                    if nextPos == 22:
                        M[i][28] += ( prob[j] - doubleProb ) / 16
                    else:
                        assert( nextPos in [7, 36] )
                        M[i][12] += ( prob[j] - doubleProb ) / 16

                    if nextPos == 36:
                        M[i][33] += ( prob[j] - doubleProb ) * 14 / ( 16 * 16 )
                        M[i][0] += ( prob[j] - doubleProb ) / ( 16 * 16 )
                        M[i][10] += ( prob[j] - doubleProb ) / ( 16 * 16 )
                    else:
                        assert( nextPos in [7, 22] )
                        M[i][nextPos-3] += ( prob[j] - doubleProb ) / 16
                    
                    M[i][nextPos] += ( prob[j] - doubleProb ) * 3 / 8
                
            else:

                if j & 1 == 1:
                    M[i][nextPos] += prob[j]
                else:
                    if doubleNumber < 2:
                        M[i][(doubleNumber+1)*40+nextPos] += doubleProb
                    else:
                        M[i][10] += doubleProb

                    M[i][nextPos] += prob[j] - doubleProb

            #print("roll" , j , ":" , sum(prob[:j+1]) - sum(M[i]))
            #input()

    #for i in range(120):
    #    print( i , ":" , sum(M[i]) )

    return M


def solve( face ):

    M = getM( face )

    t1 = time.time()
    p = [0]*120
    p[0] = 1

    turn = 0
    while True:
        p = matrixMultiple( p , M )
        if time.time() - t1 > 9.5:
            break
        turn += 1
    print("turn :" , turn )
    print(p)

    #for t in range( 10000 ):
    #    p = matrixMultiple( p , M )
    #print(p)

    res = []
    for i in range(40):
        res.append( (p[i]+p[i+40]+p[i+80],i) )

    res.sort( key = lambda x: -x[0] )
    for aRes in res:
        print( aRes[1] , ":" , int(aRes[0]*100000)/1000 , "%" )

        
def testSimpleCase( N , face ):

    p = [0]*N
    p[0] = 1

    T = 1000
    for t in range(T):

        nextp = [0]*N
        for i in range(N):
            for j in range( 1 , face + 1):
                nextp[ (i + j)%N ] += p[i]/face

        p = nextp

    print(p)


def testSimpleCase2( N , face ):

    M = [[0]*N for i in range(N)]
    for i in range(N):

        for aFace in range( 1 , face + 1 ):
            M[i][(i+aFace)%N] += 1/face


    p = [0]*N
    p[0] = 1

    T = 1000
    for  t in range(T):
        p = matrixMultiple( p , M )
    print(p)


def matrixMultiple( v , A ):

    res = []
    for i in range(len(v)):
        tres = 0
        for j in range(len(v)):
            tres += v[j]*A[j][i]
        res.append(tres)
    return res
        
if __name__ == "__main__":

    #testSimpleCase( 10 , 4 )
    #testSimpleCase2( 10 , 4 )

    #solveWithoutDoubleRules( 6 )
    solve( 6 )
