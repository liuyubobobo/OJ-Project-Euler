from math import sqrt

def getRidOffFactor(num,factor):
    while num%factor==0:
        num = num/factor
    return num

if __name__ == "__main__":

    num = 600851475143
    res = 1

    if num % 2 == 0:
        res = 2
        num = getRidOffFactor(num,2)

    i = 3
    while i*i <= num:
        if num%i == 0:
            res = max( res , i )
            num = getRidOffFactor(num,i)
        i = i + 2

    res = max(res,num)
    print(res)
