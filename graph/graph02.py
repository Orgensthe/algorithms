import sys
from collections import deque

edgeNum ,lineNum,startPoint = map(int,sys.stdin.readline().strip().split(" "))
lineList = [[] for x in range(edgeNum+1)]
check = [ False for x in range(edgeNum+1)]

for i in range(lineNum):
    startpoint , endpoint = map(int,sys.stdin.readline().strip().split(" "))
    lineList[startpoint].append((startpoint,endpoint))
    lineList[endpoint].append((endpoint,startpoint))

for line in lineList:
    line.sort()

def dfs(point):
    if check[point] == True: return
    print(point,end=" ")

    check[point] = True
    for line in lineList[point] :
        dfs(line[1])

def bfs(point):
    q = deque()
    q.append(startPoint)

    while q:
        front = q.popleft()
        if not check[front]:
            check[front] = True
            print(front,end=" ")

            for start,end in lineList[front]:
                q.append(end)


dfs(startPoint)
check = [ False for x in range(edgeNum+1)]
print()
bfs(startPoint)
