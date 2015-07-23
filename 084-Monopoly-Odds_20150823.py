import random
import time

def shuffle( arr ):

    for i in range( len(arr) ):
        r = random.randint( i , len(arr) - 1 )
        arr[i] , arr[r] = arr[r] , arr[i]

    
def initCC():

    CC = []
    CC.append( lambda x: 0 )
    CC.append( lambda x: 10 )
    for i in range(14):
        CC.append( lambda x: x )

    shuffle( CC )
    return CC


def excuteOrder( pos , C ):

    theOrder = C[0]
    newPos = theOrder(pos)
    del C[0]
    C.append( theOrder )
    return newPos


def initCH():

    CH = []
    CH.append( lambda x: 0 )    #1
    CH.append( lambda x: 10 )   #2
    CH.append( lambda x: 11 )   #3
    CH.append( lambda x: 24 )   #4
    CH.append( lambda x: 39 )   #5
    CH.append( lambda x: 5 )    #6
    CH.append( nextR )          #7
    CH.append( nextR )          #8
    CH.append( nextU )          #9
    CH.append( goback )         #10
    for i in range(6):
        CH.append( lambda x: x )

    shuffle( CH )
    return CH


def nextR( pos ):
    if pos <= 5 or pos > 35:
        return 5
    elif pos <= 15:
        return 15
    elif pos <= 25:
        return 25
    elif pos <= 35:
        return 35


def nextU( pos ):
    if pos <= 12 or pos > 28:
        return 12
    return 28


def goback( pos ):
    res = pos - 3
    if res < 0:
        res += 40
    return res


def simulation():

    pos = 0
    turn = 0
    N = 5000000
    
    CC = initCC()
    CH = initCH()
    visit = [0]*40 

    doubleNumber = 0
    while turn < N:
        dice1 = random.randint(1,4)
        dice2 = random.randint(1,4)
        dice = dice1 + dice2

        if dice1 == dice2:
            doubleNumber += 1
        else:
            doubleNumber = 0
            
        pos += dice
        pos %= 40

        if doubleNumber == 3:
            pos = 10
            doubleNumber = 0
            
        # G2J
        elif pos == 30:
            pos = 10

        # CC
        elif pos == 2 or pos == 17 or pos == 33:
            pos = excuteOrder( pos , CC )

        # CH
        elif pos == 7 or pos == 22 or pos == 36:
            pos = excuteOrder( pos , CH )
        
        pos %= 40
        
        visit[pos] += 1
        
        turn += 1

    res = [(-visit[i],i) for i in range(40)]
    res.sort()
    print( "%02d%02d%02d" % ( res[0][1] , res[1][1] , res[2][1] ) )

    
if __name__ == "__main__":

    t1 = time.time()
    simulation()
    t2 = time.time()
    print( "simulation time:" , t2-t1 , "s" )
