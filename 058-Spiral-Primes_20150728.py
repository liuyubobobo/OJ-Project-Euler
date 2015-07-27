def isPrime( x ):
    if x == 1:
        return False
    elif x < 4:
        return True
    elif x%2 == 0:
        return False
    elif x < 9:
        return True
    elif x%3 == 0:
        return False
    else:
        f = 5
        while f*f <= x:
            if x%f == 0:
                return False
            if x%(f+2) == 0:
                return False
            f += 6
        return True

if __name__ == "__main__":

    totalNum = 1
    primeNum = 0

    curnum = 1
    addnum = 1
    while True:

        curnum += addnum
        curnum += addnum
        if isPrime( curnum ):
            primeNum += 1
        totalNum += 1
        #print( curnum )
        
        addnum += 1

        curnum += addnum
        if isPrime( curnum ):
            primeNum += 1
        totalNum += 1
        #print( curnum )
        
        curnum += addnum
        if isPrime( curnum ):
            primeNum += 1
        totalNum += 1
        #print( curnum )
        
        #if isPrime( curnum + addnum ):
        #    primeNum += 1
        totalNum += 1
        #print( curnum + addnum )

        if primeNum*10 < totalNum:
            print( "primeNum:" , primeNum , "totalNum:" , totalNum )
            print( addnum + 1 )
            break

        #print("side length =" , addnum + 1 )
        #input()
        
        addnum += 1
        

        
