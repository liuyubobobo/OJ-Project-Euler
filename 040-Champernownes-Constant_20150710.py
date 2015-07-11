def getDigits( order , d ):

    digitsnum = 0
    for i in range( 1,len(d) ):
        if order > d[i-1] and order <= d[i]:
            digitsnum = i
            break

    #print("order =" , order)
    #print("digitsnum =" , digitsnum)

    num = (order - d[digitsnum-1] - 1) // digitsnum
    #print(num)
    return int(str(10**(digitsnum-1)+num)[(order - d[digitsnum-1] - 1) % digitsnum])

if __name__ == "__main__":
    
    d = [0] * 8
    for i in range(1,8):
        d[i] = 10**i - 10**(i-1)
    print(d)

    for i in range(1,8):
        d[i] = d[i-1] + d[i]*i
    print(d)

    #for i in range(1,34):
    #    print( getDigits(i,d) , end="")

    res = 1
    for i in range(7):
        print( getDigits( 10**i , d ) )
        res *= getDigits( 10**i , d )

    print(res)
