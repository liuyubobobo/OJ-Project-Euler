if __name__ == "__main__":

    res = 0
    
    power = 1
    while True:

        num = 1
        while True:
            theLen = len( str(num**power) )
            if theLen == power:
                print( "%d^%d = %d" % ( num , power , num**power ) )
                res += 1
                print( res )
            elif theLen > power:
                break
            num += 1
            
        power += 1
