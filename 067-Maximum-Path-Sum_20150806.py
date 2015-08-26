import functools

if __name__ == "__main__":

    fp = open( "067-Maximum-Path-Sum.txt" )
    triangles = []
    while True:
        line = fp.readline().strip()
        if line == "":
            break
        triangles.append( [int(num) for num in line.split()] )

    #print( triangles )
    for i in range( 1 , len(triangles) ):
        triangles[i][0] += triangles[i-1][0]
        for j in range( 1 , len(triangles[i]) - 1 ):
            triangles[i][j] += max( triangles[i-1][j-1] , triangles[i-1][j] )
        triangles[i][-1] += triangles[i-1][-1]

    res = functools.reduce( max , triangles[-1] , -1 )
    print( res )
