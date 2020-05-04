import sys

num = sys.stdin.readline()
socks = list(map(int, sys.stdin.readline().strip().split(" ")))
dic = dict()
for sock in socks:
    try:
        dic[sock] +=1
    except KeyError:
        dic[sock] = 1

result = 0

for key in dic.keys():
    result += (dic[key]//2)

print(result)