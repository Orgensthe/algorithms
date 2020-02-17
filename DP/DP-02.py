import sys

num = int(sys.stdin.readline().strip())


def solution(target,n_1,n_2,num):

    if  target-1 == n_1:
        return n_1+n_2
    else:

print(solution(num,1,2,1)%10007)