def solution(L, x):
    answer = [];

    for key, value in enumerate(L):
        if value == x:
            answer.append(key)

    if len(answer) == 0:
        answer.append(-1)

    return answer

    