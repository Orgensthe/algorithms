import sys

people , numFirend = map(int,sys.stdin.readline().strip().split(" "))
lineList = [[] for x in range(people)]
check = [ False for x in range(people)]

for i in range(numFirend):
    startpoint , endpoint = map(int,sys.stdin.readline().strip().split(" "))
    lineList[startpoint].append((startpoint,endpoint))
    lineList[endpoint].append((endpoint,startpoint))


def dfs(point, depth):
    if depth >= 4 : return True
    if check[point] == True: return

    check[point] = True
    for line in lineList[point] :
        if (dfs(line[1],depth+1)):
            return True

for i in range(people):
    if dfs(i,0):
        print(1) 
        break
    if i == people-1: print(0) 
