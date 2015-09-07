def romanToInt( s ):

    if s == "":
        return 0
        
    romanP = [""]*4
    romanCharacters = [ ["I","V","X"] , ["X","L","C"] , ["C","D","M"] , ["M"] ]

    i = 0
    while i < len(s):

        for j in range(len(romanCharacters)-1,-1,-1):
            if s[i] in romanCharacters[j]:
                carr = romanCharacters[j]
                break
        index = j
            
        j = i
        while j < len(s) and s[j] in carr:
            romanP[index] += s[j]
            j += 1

        #print(romanP[index])
        i = j

    res = 0
    for i in range( 3 , -1 , -1 ):
        tres = 0
        for c in romanP[i]:
            if c == romanCharacters[i][0]:
                tres += 1
            elif c == romanCharacters[i][1]:
                if tres != 0:
                    tres *= -1
                tres += 5
            else:
                if tres != 0:
                    tres *= -1
                tres += 10
            assert( tres < 10 )
        res += tres*(10**i)

    return res


def intToRoman( num ):
    
    roman = [ ["I","V","X"] , ["X","L","C"] , ["C","D","M"] , ["M"] ]

    index = 0
    res = ""
    while num != 0:

        if index == 3:
            res = "M"*num + res
            break
        
        thenum = num%10

        tres = ""
        if thenum > 0 and thenum < 4:
            tres = roman[index][0]*thenum
        elif thenum == 4:
            tres = roman[index][0] + roman[index][1]
        elif thenum == 5:
            tres = roman[index][1]
        elif thenum > 5 and thenum < 9:
            tres = roman[index][1] + roman[index][0]*(thenum-5)
        elif thenum == 9:
            tres = roman[index][0] + roman[index][2]

        res = tres + res
                
        num //= 10
        index += 1

    return res

    
if __name__ == "__main__":

    res = 0
    fp = open("089-Roman-Numerals.txt")
    #maxnum = 0
    #total = 0
    while True:
        oRomanNum = fp.readline().strip()
        if oRomanNum == "":
            break

        num = romanToInt( oRomanNum )
        #maxnum = max( maxnum , num )
        romanNum = intToRoman( num )

        #if romanNum.find("IIII") != -1 or romanNum.find("XXXX") != -1 or romanNum.find("CCCC") != -1\
        #   or romanNum.find("VIIII") != -1 or romanNum.find("LXXXX") != -1 or romanNum.find("DCCCC") != -1:
        #    print("!!!!")
            
        res += len( oRomanNum ) - len( romanNum )
        #total += 1

    #print( "max num:" , maxnum )
    #print( "total =" , total )
    print( res )

    fp.close()

