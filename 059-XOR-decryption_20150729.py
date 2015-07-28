def decryption( chars , code , printableSet , alphabetaSet ):

    res = []
    j = 0
    for i in range( len(chars) ):
        charascii = chars[i]^code[j]
        if charascii not in printableSet:
            return False , []
        res.append( charascii )
        j = ( j + 1 ) % 3

    #if ord(chr(res[0]).lower()) not in alphabetaSet:
    #    return False , []
    
    return True , res


def charStat( sentence ):

    charDict = dict()
    for c in sentence:
        if c in charDict:
            charDict[c] += 1
        else:
            charDict[c] = 1

    res = []
    for c , num in charDict.items():
        res.append( (-num,c) )
    res.sort()

    return [ res[i][1] for i in range(len(res)) ]

if __name__ == "__main__":

    fp = open("059-XOR-decryption.txt")
    chars = [int(x) for x in fp.readline().strip().split(",")]
    fp.close()

    printableSet = {x for x in range(32,127)}
    alphabetaSet = [x for x in range( ord('a') , ord('z') + 1 )]

    tcode = [ord('g'),ord('o'),ord('d')]
    ok , res = decryption( chars , tcode , printableSet , alphabetaSet )
    #print( "".join([chr(x) for x in res]).lower() )
    #input()
    
    for a in range( ord('a') , ord('z') + 1 ):
        for b in range( ord('a') , ord('z') + 1 ):
            for c in range( ord('a') , ord('z') + 1 ):
                code = [ a , b , c ]
                ok , res = decryption( chars , code , printableSet , alphabetaSet )
                if ok:
                    sentence = "".join([chr(x) for x in res]).lower()
                    #print( sentence )
                    #print( "=" * 50 )
                    charSortedArray = charStat( sentence )
                    mostPopularCharSet = set( charSortedArray[0:3] )
                    if 'e' in mostPopularCharSet and ' ' in mostPopularCharSet:
                        print("***",code)
                        print(sentence)
                        print( "res =" , sum(res) )
                        print( "=" * 50 )
