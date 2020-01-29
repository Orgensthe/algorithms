

def solution():
    word_list = set()
    for i in range(int(input())):
        word_list.add(input())

    word_list = list(word_list)
    word_list.sort()
    word_list = sorted(word_list,key=len)


    for word in word_list:
        print(word)

solution()