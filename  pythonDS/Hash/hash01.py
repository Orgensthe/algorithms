def solution(participant, completion):
    answer = ''


    result = dict()

    for name in participant:
        try:
            result[name] +=1
        except KeyError:
            result[name] = 1

    for name in completion:
        if result[name] > 1:
            result[name] -=1
        else:
            result.pop(name)

    answer = list(result.keys())[0]

    return answer






solution( ["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"])