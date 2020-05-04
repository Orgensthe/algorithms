from collections import deque

def countingValleys(n, s):
    height = 0
    result = 0
    for step in s:
        if step is "U":
            height +=1
            if height == 0:
                result += 1
        else:
            height -=1

    return result


print(countingValleys(12,"DDUUDDUDUUUD"))