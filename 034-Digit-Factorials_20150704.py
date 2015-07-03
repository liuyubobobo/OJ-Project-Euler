import functools

def findFirstNonZeroIndex( nums ):
    for i in range(len(nums)):
        if nums[i] != 0:
            return i
    return len(nums)


if __name__ == "__main__":
    
    fac = [1]*10
    for i in range(1,10):
        fac[i] = fac[i-1]*i
    print(fac)
    
    res = 0
    digits = [0,0,0,0,0,0,3]
    while True:
        
        firstNonZeroIndex = findFirstNonZeroIndex( digits )
        thenum = functools.reduce( lambda x, y: 10*x + y , digits[firstNonZeroIndex:] , 0 )

        tres = 0
        i = firstNonZeroIndex
        while i < len(digits):
            tres += fac[ digits[i] ]
            if tres > thenum:
                break
            i += 1

        if tres == thenum:
            res += tres
            print("Found",tres)

        if i-1 >= 0:
            digits[i-1] += 1
        else:
            break

        j = i-1
        extra = 0
        while j >= 0:
            newextra = ( digits[j] + extra ) // 10
            digits[j] = ( digits[j] + extra ) % 10
            extra = newextra
            j -= 1

        if extra == 1:
            break

        for j in range(i,len(digits)):
            digits[j] = 0
            

    print(res)

        
