if __name__ == "__main__":

    fp = open("018-Maximum-Path-Sum-I.in")
    triangle = []

    while True:
        aline = fp.readline()
        if not aline:
            break
        triangle.append( [int(x) for x in aline.strip().split()] )

    #print(triangle)
    res = [ [0]*len(triangle) for i in range(len(triangle)) ]

    res[0][0] = triangle[0][0]
    printRes = 0
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                res[i][j] = res[i-1][j] + triangle[i][j]
            elif j == i:
                res[i][j] = res[i-1][j-1] + triangle[i][j]
            else:
                res[i][j] = max(res[i-1][j],res[i-1][j-1]) + triangle[i][j]

        printRes = max( [printRes] + res[i] )

    print( printRes )
                
