def ok( num ):

    n = len(str(num))
    if n != len(str(6*num)):
        return False

    digits = []
    for i in range( 1 , 7 ):
        digits.append( sorted([c for c in str(i*num)]) )

    for j in range( n ):
        for i in range( 1 , len(digits) ):
            if digits[i][j] != digits[0][j]:
                return False

    return True

if __name__ == "__main__":

    num = 1
    while True:
        if ok(num):
            print(num)
            break
        num += 1
