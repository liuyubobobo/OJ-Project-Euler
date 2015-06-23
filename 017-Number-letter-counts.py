if __name__ == "__main__":

    numbers20 = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
    numbers20 += ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
    #print(numbers20)

    numbers100 = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    #print(numbers100)

    dp = [0]*1001
    
    res = 0
    for i in range(1,20):
        res += len(numbers20[i])
        dp[i] = len(numbers20[i])

    for i in range(20,100):
        if i%10 == 0:
            tres = len(numbers100[i//10])
        else:
            tres = len(numbers100[i//10]) + len(numbers20[i%10])
        dp[i] = tres
        res += tres

    
    
    for i in range(100,1000):
        if i%100 == 0:
            tres = len(numbers20[i//100]) + len("hundred")
        else:
            tres = len(numbers20[i//100]) + len("hundred") + len("and") + dp[i%100]
        dp[i] = tres
        res += tres

    res += len(numbers20[1]) + len("thousand")

    print(res)
            
