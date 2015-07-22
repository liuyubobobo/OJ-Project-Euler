def inArea( x , y , R , C ):
    return x >= 0 and x < R and y >= 0 and y < C


def establishGraph( m ):

    R = len(m)
    C = len(m[0])
    
    g = [ [] for i in range(R*C) ]
    d = [ (-1,0) , (1,0) , (0,1) , (0,-1) ]
    for i in range(R):
        for j in range(C):
            nodeIndex = i * R + j
            for k in range(4):
                if inArea( i + d[k][0] , j + d[k][1] , len(m) , len(m[0]) ):
                    # add edge info: ( dis , node )
                    g[nodeIndex].append( ( m[i+d[k][0]][j+d[k][1]] , ( i + d[k][0] ) * R + j + d[k][1] ) )

    #print( "Graph:" )
    #for i in range(len(g)):
    #    print( "node" , i , ":" , g[i] )
    return g


###################################################################################
## This problem's size is small, so we don't need to use heap in dijkstra algorihtm
## -- An dij algorihtm's implementation using heap is in
## ---- hackerrank.com Project Euler Plus Problem 083
###################################################################################
def shortestPath( g ):

    N = len(g)
    #print(N)

    INF = ( 10**9 + 1 ) * N * N
    
    dis = [INF] * N
    used = [False] * N

    dis[0] = 0

    while True:

        node = -1
        minDis = INF
        for i in range( N ):
            if not used[i] and dis[i] < minDis:
                minDis = dis[i]
                node = i
        used[node] = True
                
        if node == N-1:
            return minDis

        for i in range( len(g[node]) ):
            nextDis , nextNode = g[node][i]
            if not used[nextNode]:
                dis[ nextNode ] = min( dis[nextNode] , minDis + nextDis )

    return INF
        
    
if __name__ == "__main__":

    fp = open("083-Path-Sum-Four-Ways.txt")
    #fp = open("083-Path-Sum-Four-Ways-test.txt")
    m = []
    while True:
        line = str( fp.readline() ).strip()
        if line == "":
            break
        #print(line)
        #input()
        m.append( [int(x) for x in line.split(",")] )

    #m = [[0]*len(m[0])] + m
    #m = m + [[0]*len(m[0])]
    print("%d * %d matrix" % ( len(m) , len(m[0]) ) )
    #print(m)
    
    g = establishGraph( m )
    print( shortestPath( g ) + m[0][0] )
    
