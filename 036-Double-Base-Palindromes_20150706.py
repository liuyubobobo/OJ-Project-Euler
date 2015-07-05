import functools

def isPalindrome( num , base ):

    numDigits = []
    while num != 0:
        numDigits.append( num%base )
        num //= base

    n = len(numDigits)
    for i in range(0,n//2):
        if numDigits[i] != numDigits[n-i-1]:
            return False

    return True


if __name__ == "__main__":

    res = 0
    for i in range(1,1000):
        digits= [int(x) for x in str(i)]

        aDigits = digits + list(reversed(digits[:len(digits)-1]))
        aNum = functools.reduce( lambda x,y:10*x+y , aDigits , 0 )
        if isPalindrome( aNum , 2 ):
            res += aNum
            
        bDigits = digits + list(reversed(digits[:]))
        bNum = functools.reduce( lambda x,y:10*x+y , bDigits , 0 )
        if isPalindrome( bNum , 2 ):
            res += bNum

    print(res)
        
