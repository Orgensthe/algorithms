




def hourglassSum(arr):

    def countHourglass(arr, x, y):

        return sum(arr[x][y:y + 3]) + arr[x + 1][y + 1] + sum(arr[x + 2][y:y + 3])
    maxHourglassNum = -100

    for i in range(0,len(arr)-2):
        for j in range(0,len(arr[0])-2):
            tmp = countHourglass(arr,i,j)
            maxHourglassNum = tmp if tmp > maxHourglassNum else maxHourglassNum

    return  maxHourglassNum

def solution():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglassSum(arr))


solution()