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
    CH.append( lambda x: 28 if x == 22 else 12 )    #9
    CH.append( lambda x: x - 3 )                    #10
    for i in range(6):
        CH.append( lambda x: x )

    shuffle( CH )
    return CH


def nextR( pos ):
    if pos == 7:
        return 15
    elif pos == 22:
        return 25
    return 5


def simulation():

    pos = 0
    turn = 0
    N = 10000000
    
    CC = initCC()
    CH = initCH()
    ccp = 0
    chp = 0
    visit = [0]*40 

    doubleNumber = 0
    while turn < N:

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            doubleNumber += 1
        else:
            doubleNumber = 0

        dice = dice1 + dice2
        pos = ( pos + dice ) % 40

        if doubleNumber == 3:
            pos = 10
            doubleNumber = 0
            
        # G2J
        elif pos == 30:
            pos = 10

        # CC
        elif pos == 2 or pos == 17 or pos == 33:
            #pos = excuteOrder( pos , CC )
            pos = CC[ccp](pos)
            ccp = (ccp+1)%16
        # CH
        elif pos == 7 or pos == 22 or pos == 36:
            #pos = excuteOrder( pos , CH )
            pos = CH[chp](pos)
            chp = (chp+1)%16
            if pos == 33:
                #pos = excuteOrder( pos , CC )
                pos = CC[ccp](pos)
                ccp = (ccp+1)%16
        
        visit[pos] += 1
        
        turn += 1

    res = [(-visit[i],i) for i in range(40)]
    res.sort()

    for i in range( 40 ):
        print( "%02d : %.3f" % ( res[i][1] , -res[i][0] / N * 100 ) )
    print( "%02d%02d%02d" % ( res[0][1] , res[1][1] , res[2][1] ) )

    
if __name__ == "__main__":

    t1 = time.time()
    simulation()
    t2 = time.time()
    print( "simulation time:" , t2-t1 , "s" )
