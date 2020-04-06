import sys

x ,y = map(int,sys.stdin.readline().strip().split(" "))

board = [[] for _ in range(x)]

for i in range(x):
    line = sys.stdin.readline().strip()
    for c in line:
        board[i].append(c)

lineList = []

for i in range(x):
    for j in range(y):



print(board)

