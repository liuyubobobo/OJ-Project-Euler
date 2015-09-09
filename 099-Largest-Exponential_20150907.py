import math


if __name__ == "__main__":

    fp = open( "099-Largest-Exponential.txt") 
    index = 0
    
    maxres = -1
    resline = -1
    while True:
        line = fp.readline().strip()
        if line == "":
            break

        a,b = [int(x) for x in line.split(",")]
        index += 1

        tres = b*math.log( a )
        if tres > maxres:
            maxres = tres
            resline = index

    print( resline )

    fp.close()
