num = int(input())

answer=[]

if(num%5 == 0):
    answer.append([5 for x in range(num//5)])
if(num%4 == 0):
    answer.append([4 for x in range(num//4)])

if (num%5)%4==0: 
    tempVar = [5]
    tempNum = num
    tempNum-=5
    good = True
    while tempNum%4 != 0:
        if tempNum < 0:
            tempNum=0
            good = False
        else:
            tempNum-=5
            tempVar.append(5)
    
    while tempNum != 0:
        if tempNum < 0:
            tempNum=0
            good = False
        else:
            tempNum-=4
            tempVar.append(4)
    if good:
        answer.append(tempVar)
elif (num%4)%5 == 0:
    tempVar = [4]
    tempNum = num
    tempNum-=4
    good = True
    while tempNum%5 != 0:
        if tempNum < 0:
            tempNum=0
            good = False
        else:
            tempNum-=4
            tempVar.append(4)
        
    while tempNum != 0:
        if tempNum < 0:
            tempNum=0
            good = False
        else:
            tempNum-=5
            tempVar.append(5)
    if good:
        answer.append(tempVar)

tempNum = num
tempVar = []
for i in range(1,num):
    tempNum=num
    tempNum-=i*5
    if tempNum%4 == 0 and tempNum>0:
        for y in range(i):
            tempVar.append(5)
        for x in range(tempNum//4):
            tempVar.append(4)
        answer.append(tempVar)
    tempVar=[] 
            
answer = list(set(tuple(x) for x in answer))
print(len(answer))

