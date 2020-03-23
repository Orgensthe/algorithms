import sys
def next_permutation(x):

    len_ = len(x)-1
    next_ = 0
    for i in range(len_,0,-1):
        if x[i] > x[i-1]:
            next_ = i-1
            break
        
    if next_  == 0 : return False
    j = len_

    while x[next_] > x[j]:
        j-=1
    
    x[next_] , x [j] = x [j] ,x[next_]

    x[next_+1:] =  sorted(x[next_+1:])
    return x


input()
target = list(map(int , sys.stdin.readline().strip("").split(" ")))

result = next_permutation(target)
if result:
    for i in result:
        print(i, end=' ')
    print()
else:
    print(-1)