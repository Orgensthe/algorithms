
def solution():

    position  = []
    for i in range(int(input())):
        x , y =  str(input()).split(" ")
        position.append((x,y))


    position= sorted(position,key=lambda x:(x[0],x[1] ))
   
    for p in position:
        print(p[0]+" "+p[1])

solution()
