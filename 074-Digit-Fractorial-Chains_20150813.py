import time


def calFacDigits( num , fac ):
    return sum( [ fac[int(x)] for x in str(num) ] )


###############################################
## Thinking 1: Brute Force to get the res table
###############################################
def getResTable1( N , fac ):

    table = [0] * N
    for i in range( 10 , N ):
        memo = set()
        memo.add(i)
        num = i
        while True:
            nextNumber = calFacDigits( num , fac )
            if nextNumber in memo:
                table[i] = len(memo)
                break
            else:
                memo.add( nextNumber)
            num = nextNumber
    return table


############################
## Thinking 2: Optimization
############################
def getResTable2( N , fac ):

    table = [0] * N
    for i in range( 10 , N ):
        if table[i] == 0:
            #if i%1000 == 0:
            #    print( "check" , i )
            memo = dict()
            memo[i] = 0
            num = i
            index = 1
            while True:
                #print(memo)
                nextNumber = calFacDigits( num , fac )
                if nextNumber in memo:
                    #print("check " , i )
                    loopnum = nextNumber
                    loopLength = index - memo[loopnum]
                    for anum in memo:
                        if anum < N:
                            if memo[anum] >= memo[loopnum]:  
                                table[anum] = loopLength
                            else:
                                table[anum] = memo[loopnum] - memo[anum] + loopLength
                            #print("the res is" , table[loopnum])
                    #input()
                    break
                elif nextNumber < N and table[nextNumber] != 0:
                    for anum in memo:
                        if anum < N:
                            table[anum] = index - memo[anum] + table[nextNumber]
                    break
                else:
                    memo[nextNumber] = index
                    index += 1

                num = nextNumber

    return table

    
if __name__ == "__main__":

    fac = [1]*10
    for i in range( 2 , 10 ):
        fac[i] = i * fac[i-1]

    t1 = time.time()
    table = getResTable2( 10**6 , fac )
    t2 = time.time()
    
    print("init complete - time:" , t2-t1 , "s")
    print( "169:" , table[169] )
    print( "871:" , table[871] )
    print( "872:" , table[872] )
    print( "69:" , table[69] )
    print( "78:" , table[78] )
    print( "540:" , table[540] )
    print( "145:" , table[145] )

    res = 0
    for i in range( len(table) ):
        if table[i] == 60:
            res += 1
    print(res)
