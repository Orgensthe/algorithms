def solution(x):

    if x <= 1 :return x

    return solution(x-1)+ solution(x-2)


print (solution(5))