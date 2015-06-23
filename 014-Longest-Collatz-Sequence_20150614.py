def getChainLength( num , dp_dict ):
    if num in dp_dict:
        return dp_dict[num]

    if num == 1:
        return 1
    
    if num%2 == 0:
        a = 0
        while num%2 == 0:
            num //= 2
            a += 1
        res = a + getChainLength( num , dp_dict )
    else:
        res = 1 + getChainLength( 3*num+1 , dp_dict )

    dp_dict[num] = res
    return res

if __name__ == "__main__":
    longestChainLength = 0
    res = 0
    dp_dict = dict()
    for i in range(1,1000000+1):
        chainLength = getChainLength( i , dp_dict )
        if chainLength > longestChainLength:
            longestChainLength = chainLength
            res = i
    print(res)
