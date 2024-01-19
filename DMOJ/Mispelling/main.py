num = int(input())
answerLst = []
for i in range(num):
    tempVar = []
    inp = input()
    tempVar.append(inp[:inp.find(" ")])
    tempVar.append(inp[inp.find(" ")+1:])
    tempVar[0] = int(tempVar[0])
    if tempVar[0] != 0 and tempVar[0] < len(tempVar[1])+1:
        tempVar[1] = tempVar[1][:tempVar[0]-1] + tempVar[1][tempVar[0]:]
    answerLst.append(tempVar[1])


for i in range(len(answerLst)):
    print(i+1, answerLst[i])