from collections import  deque




def recursive(list, result):
    if len(list) == 1 :return result
    if len(list) == 2: return result +1
    if list[2] == 0: return recursive(list[2:], result +1)
    return  recursive(list[1:], result +1)
def jumpingOnClouds(c):
    return recursive(c, 0)

print(jumpingOnClouds([0, 0,1, 0, 0 ,0 , 0 ,1 , 0,0]))

print(jumpingOnClouds([0 ,0 ,1 ,0 ,0 ,1 ,0]))

# 0 ,0 ,1 ,0 ,0 ,1 ,0 0
#
# 0 ,1 ,0 ,0 ,1 ,0  1