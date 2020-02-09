import sys



len_of_row , len_of_col =  list(map(int, sys.stdin.readline().strip().split(" ") ))

board = []

for i in range(len_of_row):
    for character in sys.stdin.readline().strip():
        if character == "W":
            board.append(1)
        else:
            board.append(0)


def print_board(board):

    for i in range(len(board)):
    
        if i%len_of_col != len_of_col-1:
            print(board[i], end=" ")
        else: 
            print(board[i])

# 0 0 0 1 0 1 0 1 
# 

### 두가지 방법 존대  1로 시작 혹은 0으로 시작
### 따라서 시작점의 인덱스로 1로시작할 떄와 0을로 시작할때의 최소 값을 그곳에서의 최솟값으로 설정


def check_board(start_value,index_of_start,board):

    count = 0
    start = start_value
    for i in range(64):
       
        if i%8 != 7:
            if board[index_of_start+i] != start:
                count += 1
            
            start = not start
            print(board[index_of_start+i],bool(board[index_of_start+i]) and start ,end = " ")
            
        else:
            print(board[index_of_start+i],bool(board[index_of_start+i]) and start)

            if board[index_of_start+i] != start:
            
                count += 1
        
    return count

min_change = 64

print_board(board)
# for i in range(len_of_col-7):
    
#     for j in range(len_of_row-7):
#         temp_min_of_zero = check_board(True,(j*8+i),board)
#         temp_min_of_one = check_board(False,(j*8+i),board)

#         print(j*8+i,temp_min_of_one,temp_min_of_zero)

check_board(True,5,board)