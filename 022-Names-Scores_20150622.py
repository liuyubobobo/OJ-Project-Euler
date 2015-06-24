if __name__ == "__main__":

    fp = open("022-Names-Scores.txt")

    line = fp.readline().strip()
    names = [x[1:len(x)-1] for x in line.split(",")]

    names.sort()
    #print("sort complete!",len(names))
    #print(names)

    res = 0
    for i in range(len(names)):
        res += (i+1)*sum([ord(x)-ord('A')+1 for x in names[i]])
    print(res)
