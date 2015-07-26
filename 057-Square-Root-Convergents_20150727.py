if __name__ == "__main__":

    res = 0
    
    n = 1
    d = 2
    for t in range(1000):
        resn = n + d
        resd = d
        #print( t , ":" , resn , "/" , resd )
        if len( str(resn) ) > len( str(resd) ):
            res += 1
        n += d*2
        n , d = d , n

    print(res)
