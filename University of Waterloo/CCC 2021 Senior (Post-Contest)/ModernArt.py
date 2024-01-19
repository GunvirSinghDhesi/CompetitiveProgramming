checkersMap = []
row =int(input())
col =int(input())
changes = int(input())
optionChanges = []
gCount=0
for i in range(changes):
    optionChanges.append(input().split(" "))

for x in range(row):
    checkersMap.append([])
    for y in range(col):
        checkersMap[x].append('B')

for i in range(len(optionChanges)):
    if optionChanges[i][0] == "R":
        for y in range(len(checkersMap[0])):
            if checkersMap[int(optionChanges[i][1])-1][y] == "G":
                checkersMap[int(optionChanges[i][1])-1][y] = "B"
                gCount-=1
            else:
                checkersMap[int(optionChanges[i][1])-1][y] = "G"
                gCount+=1
            
    else:
        for x in range(len(checkersMap)):
            if checkersMap[x][int(optionChanges[i][1])-1] == "G":
                checkersMap[x][int(optionChanges[i][1])-1] = "B"
                gCount-=1
            else:
                checkersMap[x][int(optionChanges[i][1])-1] = "G"
                gCount+=1

print(gCount)