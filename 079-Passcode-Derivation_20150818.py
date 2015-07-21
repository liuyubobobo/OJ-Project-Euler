def readInput():

    fp = open( "079-Passcode-Derivation.txt")
    logins = set()
    while True:
        line = str(fp.readline()).strip()
        if line == "":
            break
        logins.add(line)
    fp.close()

    #for login in logins:
    #    print( login )

    return logins


def establishGraph( logins ):

    g = [ [] for i in range(10) ]

    for login in logins:
        seq = [ int(x) for x in login ]

        if seq[1] not in g[seq[0]]:
            g[seq[0]].append( seq[1] )
        if seq[2] not in g[seq[1]]:
            g[seq[1]].append( seq[2] )

    for pointInfo in g:
        print( pointInfo )
    return g
        

def topoSort( g ):

    indeg  = [0]*10
    outdeg = [0]*10

    for i in range( 10 ):
        outdeg[i] = len( g[i] )
        for j in range( len( g[i] ) ):
            indeg[ g[i][j] ] += 1

    used = [False]*10
    usedNum = 0
    for i in range( 10 ):
        if indeg[i] == 0 and outdeg[i] == 0:
            used[i] = True
            usedNum += 1

    res = []
    while usedNum < 10:
        node = -1
        for i in range( 10 ):
            if not used[i] and indeg[i] == 0:
                node = i
                break

        assert( node != -1 )
        used[node] = True
        usedNum += 1
        res.append( node )
        for nextNode in g[node]:
            indeg[nextNode] -= 1

    print("".join([str(x) for x in res])) 

        
if __name__ == "__main__":

    logins = readInput()
    graph = establishGraph( logins )
    topoSort( graph )
    
