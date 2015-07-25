def digitsum( num ):

    res = 0
    nums = str(num)
    for c in nums:
        res += int(c)
    return res

if __name__ == "__main__":

    largest = 0
    for a in range( 100 ):
        for b in range( 100 ):
            largest = max( largest  , digitsum( a**b ) )
    print( largest )
