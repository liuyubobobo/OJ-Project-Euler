import functools

if __name__ == "__main__":

    cubeDigitsDict = dict()
    smallestRes = dict()
    i = 1
    while True:

        key = functools.reduce( lambda x,y:x+y , sorted(str(i**3)) , "")
        if key in cubeDigitsDict:
            cubeDigitsDict[key] += 1
            if cubeDigitsDict[key] == 5:
                print( i , ":" , i**3 )
                print( smallestRes[key] )
                break
        else:
            cubeDigitsDict[key] = 1
            smallestRes[key] = i**3

        i += 1
