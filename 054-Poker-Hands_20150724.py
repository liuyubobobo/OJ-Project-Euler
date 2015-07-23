def convertCard(s):

    if s[:-1] == "T":
        return ( 10 , s[-1] )
    elif s[:-1] == "J":
        return ( 11 , s[-1] )
    elif s[:-1] == "Q":
        return ( 12 , s[-1] )
    elif s[:-1] == "K":
        return ( 13 , s[-1] )
    elif s[:-1] == "A":
        return ( 14 , s[-1] )

    return ( int(s[:-1]) , s[-1] )


def sameSuit( x ):

    for i in range( 1 , len(x) ):
        if x[i][1] != x[0][1]:
            return False

    return True


def consecutive( x ):

    if x[0][0] == 2 and x[1][0] == 3 and x[2][0] == 4 and x[3][0] == 5 and x[4][0] == 14:
        return True

    for i in range( 1 , len(x) ):
        if x[i][0] - x[i-1][0] != 1:
            return False

    return True


def fourOfAHand( x ):

    ok = True
    for i in range( 1 , 4 ):
        if x[i][0] != x[0][0]:
            ok = False
            break
    if ok:
        return True

    for i in range( 2 , 5 ):
        if x[i][0] != x[1][0]:
            return False

    return True


def fullHouse( x ):

    nums = set()
    for i in range(5):
        nums.add( x[i][0] )

    # before that, we know it's not a four-of-a-hand
    return len(nums) == 2


def threeOfAKind( x ):

    for i in range(3):

        if x[i][0] == x[i+1][0] and x[i][0] == x[i+2][0]:
            return True

    return False


def numberOfValueInCards( num , x ):

    res = 0
    for c in x:
        if c[0] == num:
            res += 1

    return res


def twoPairs( x , cmpTarget ):

    nums = set()
    for i in range(5):
        nums.add( x[i][0] )

    # before that, we know it's not a three-of-a-kind
    if len(nums) != 3:
        return False

    for num in nums:
        if numberOfValueInCards( num , x ) == 2:
            cmpTarget.append(num)

    cmpTarget.sort( key = lambda x:-x )

    return True


def onePair( x , cmpTarget ):

    nums = set()
    for i in range(5):
        nums.add( x[i][0] )

    if len(nums) != 4:
        return False

    for num in nums:
        if numberOfValueInCards( num , x ) == 2:
            cmpTarget.append(num)

    cmpTarget.sort( key = lambda x:-x )

    return True


def rank( x ):

    cmpTarget = []
    if sameSuit( x ) and consecutive( x ) and x[0][0] == 10:
        return ( 10 , 100 , [x[4-i][0] for i in range(5)] )
    elif sameSuit( x ) and consecutive( x ):
        if x[4][0] == 14 and x[0][0] == 2:
            return ( 9 , 5 , [x[4-i][0] for i in range(5)])
        return ( 9 , x[0][0] , [x[4-i][0] for i in range(5)] )
    elif fourOfAHand( x ):
        return ( 8 , x[2][0] , [x[4-i][0] for i in range(5)] )
    elif fullHouse( x ):
        return ( 7 , x[2][0] , [x[4-i][0] for i in range(5)] )
    elif sameSuit( x ):
        return ( 6 , x[4][0] , [x[4-i][0] for i in range(5)] )
    elif consecutive( x ):
        if x[4][0] == 14 and x[0][0] == 2:
            return ( 5 , 5 , [x[4-i][0] for i in range(5)])
        return ( 5 , x[4][0] , [x[4-i][0] for i in range(5)] )
    elif threeOfAKind( x ):
        return ( 4 , x[2][0] , [x[4-i][0] for i in range(5)] )
    elif twoPairs( x , cmpTarget ):
        return ( 3 , cmpTarget , [x[4-i][0] for i in range(5)] )
    elif onePair( x , cmpTarget ):
        return ( 2 , cmpTarget[0] , [x[4-i][0] for i in range(5)] )

    return ( 1 , x[4][0] , [x[4-i][0] for i in range(5)] )
    
    
def play( a , b ):

    ranka = rank( a )
    rankb = rank( b )
    #print( a )
    #print( "ranka :" , ranka )
    #print( b )
    #print( "rankb :" , rankb )
    #input()
    return ranka > rankb

if __name__ == "__main__":

    fp = open("054-Poker-Hands.txt")
    res = 0
    while True:
        line = fp.readline().strip()
        if line == "":
            break

        cardsStr = line.split()
        cards = []
        for i in range(len(cardsStr)):
            cards.append( convertCard( cardsStr[i] ) )
        if play( sorted(cards[:5]) , sorted(cards[5:]) ) == 1:
            res += 1

    fp.close()
    print(res)
