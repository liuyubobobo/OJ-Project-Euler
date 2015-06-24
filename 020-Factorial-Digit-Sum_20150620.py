if __name__ == "__main__":
    res = 1
    for i in range(2,100+1):
        res *= i
    print( sum([int(x) for x in str(res)]) )
