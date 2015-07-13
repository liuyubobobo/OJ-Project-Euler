import time

###############################################################
## This problem's algorithm can be accelerated dramatically
## The detail can be seen on same problem in Project Euler Plus
###############################################################
def solve():

    used = [False] * 11
    p = [0] * 10
    return generateRes( p , 0 , used )


def generateRes( p , index , used ):

    if index == 10:
        #print(p)
        pStr = getStrFromP( p )
        if len( pStr ) == 16:
            return pStr
        return ""

    res = ""
    for i in range( 1 , 11 ):
        if not used[i]:
            p[index] = i
            
            if index == 4 and sum(p[0:3]) != sum(p[2:5]):
                continue

            if index == 6 and sum(p[2:5]) != sum(p[4:7]):
                continue

            if index == 8 and sum(p[4:7]) != sum(p[6:9]):
                continue

            if index == 9 and sum(p[6:9]) != sum(p[8:10]) + p[1]:
                continue
            
            used[i] = True
            res = max( res , generateRes( p , index + 1 , used ) )
            used[i] = False

    return res


def getStrFromP( p ):

    res = []
    res.append( tuple([p[0],p[1],p[2]]) )
    res.append( tuple([p[3],p[2],p[4]]) )
    res.append( tuple([p[5],p[4],p[6]]) )
    res.append( tuple([p[7],p[6],p[8]]) )
    res.append( tuple([p[9],p[8],p[1]]) )

    minIndex = 0
    minFirstNumber = res[0][0]
    for i in range( 1 , len(res) ):
        if res[i][0] < minFirstNumber:
            minIndex = i
            minFirstNumber = res[i][0]

    res = res[minIndex:] + res[:minIndex]

    resS = ""
    for i in range(len(res)):
        for j in range(len(res[i])):
            resS += str(res[i][j])

    return resS
        
    
if __name__ == "__main__":

    print( solve() )
