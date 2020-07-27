def rotLeft(a, d):
    lenOfList = len(a)


    if d == lenOfList:
        return a
    for i in range(d % lenOfList):
        tmp = a.pop(0)
        a.append(tmp)
    return a

print(rotLeft([1,2,3,4,5,6,7,8,9],9))