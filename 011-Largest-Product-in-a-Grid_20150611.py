D = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def inArea( x , y , N , M ):
    return x >= 0 and x < N and y >= 0 and y < M

if __name__ == "__main__":
    fp = open("011-Largest-Product-in-a-Grid.in")

    g = []
    while True:
        aline = fp.readline()
        if not aline:
            break
        g.append([int(x) for x in aline.strip().split()])

    N = len(g)
    M = len(g[0])
    
    #print(g)
    res = 0
    for i in range(N):
        for j in range(M):
            for k in range(len(D)):
                if inArea( i + 3*D[k][0] , j + 3*D[k][1] , N , M ):
                    a = g[i + 0*D[k][0]][j + 0*D[k][1]]
                    b = g[i + 1*D[k][0]][j + 1*D[k][1]]
                    c = g[i + 2*D[k][0]][j + 2*D[k][1]]
                    d = g[i + 3*D[k][0]][j + 3*D[k][1]]
                    res = max(res , a*b*c*d )
    print(res)

    
