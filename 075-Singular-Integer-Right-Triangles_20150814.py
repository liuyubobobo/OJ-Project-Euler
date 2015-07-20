def allPrimitiveTriplesLessOrEqualThan( N ):

    res = []
    stack = [(3,4,5)]
    while len(stack) != 0:

        t = stack.pop()
        p = t[0] + t[1] + t[2]
        if p > N:
            continue
        res.append(t)

        stack.append( ( t[0]-2*t[1]+2*t[2] , 2*t[0]-t[1]+2*t[2] , 2*t[0]-2*t[1]+3*t[2] ) )
        stack.append( ( t[0]+2*t[1]+2*t[2] , 2*t[0]+t[1]+2*t[2] , 2*t[0]+2*t[1]+3*t[2] ) )
        stack.append( ( -t[0]+2*t[1]+2*t[2] , -2*t[0]+t[1]+2*t[2] , -2*t[0]+2*t[1]+3*t[2] ) )

    return res


if __name__ == "__main__":

    N = 1500000
    res = allPrimitiveTriplesLessOrEqualThan( N )
    #print( len(res) )
    triangleDict = dict()

    for triple in res:
        total = sum(triple)
        i = 1
        while i*total <= N:

            newTotal = i*total
            if newTotal in triangleDict:
                triangleDict[newTotal] += 1
            else:
                triangleDict[newTotal] = 1

            i += 1

    #print( len(triangleDict) )

    res = 0
    for l,num in triangleDict.items():
        if num == 1:
            res += 1

    print(res)
        
