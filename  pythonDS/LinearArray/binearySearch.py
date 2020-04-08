def solution(L, x):
    

    answer = -1
    bottom = 0 
    top =len(L)-1

    while bottom < top:
        mid = (top+bottom)//2
        if x == L[mid]: 
            return mid
        elif x < L[mid] : 
            top = mid -1
        elif x > L[mid] :
            bottom = mid +1
    
    return answer

print(solution( [2, 3, 5, 6, 9, 11, 15],6))