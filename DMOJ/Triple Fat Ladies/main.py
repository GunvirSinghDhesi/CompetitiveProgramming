

# Time - 9:20

testCases = int(input())
for i in range(testCases):    
    num = int(input())
    tempVar=num+1
    while str(tempVar**3)[-3:] != "888":
        tempVar+=1
    print(tempVar)