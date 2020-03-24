import sys
from collections import deque

people , numFirend = map(int,sys.stdin.readline().strip().split(" "))
lineList = [[] for x in range(people)]
check = [ False for x in range(people)]



for i in range(numFirend):
    startpoint , endpoint = map(int,sys.stdin.readline().strip().split(" "))
    lineList[startpoint].append((startpoint,endpoint))


q = deque()
q.append(0)
check[0] = True
count = 0
while q:
    point = q.popleft()
    print(q)
    for _set in lineList[point]:
        if not check [_set[1]] :
            check [_set[1]] = True
            count +=1
            q.append(_set[1])


if count >= 4:
    print(1)
else:
    print(0)



