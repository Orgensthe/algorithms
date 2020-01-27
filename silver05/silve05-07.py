from collections import Counter
import math
def solution():

    room_number = list(input())
    room_number
    count = Counter(room_number) 
    max_key = count.most_common(1)
    
    if max_key[0][0] == '9' or int(max_key[0][0]) == '6' :
      
        print(math.ceil( (count['6'] + count['9'])/2) )
        return
    
    if  count[max_key[0][0]] < (count['6'] + count['9'])//2 :
        print(math.ceil( (count['6'] + count['9'])/2) )
    else:
        print(max_key[0][1])


solution()