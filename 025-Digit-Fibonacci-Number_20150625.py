def solve( num ):
    if num == 1:
        return 1

    a = 1
    b = 1
    index = 2
    while True:
        index += 1
        c = a + b
        if len(str(c)) == num:
            return index

        a,b = b,c

    return -1
        
    
if __name__ == "__main__":

    print( solve(1000) )
