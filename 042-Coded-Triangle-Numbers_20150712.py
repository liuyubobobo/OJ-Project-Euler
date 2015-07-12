import functools

def calcTriangleNumbersTable( N ):

    res = []
    for i in range(1,N+1):
        res.append( i*(i+1)//2 )
    return res

def binarySearch( arr , t ):
    ## assume the arr is sorted
    l = 0
    u = len(arr)-1
    ## {invariant: arr[l] <= t <= arr[u]}

    while l <= u:
        m = (l+u)//2
        if arr[m] == t:
            return m
        elif arr[m] > t:
            u = m - 1
        else:
            l = m + 1

    return -1

if __name__ == "__main__":

    triangleNumbers = calcTriangleNumbersTable( 100 )
    
    fp = open("042-Coded-Triangle-Numbers.txt")

    res = 0
    aline = fp.readline()

    words = [x[1:-1] for x in aline.strip().split(",")]
    for word in words:
        num = sum([ord(x)-ord('A')+1 for x in word])
        #print( word , ":" , num )
        if binarySearch( triangleNumbers , num ) != -1:
            res += 1

    print(res)
    fp.close()
