
def findFactors(num):
    factors = []
    answer = []
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)

    for i in range(len(factors)):
        for j in range(len(factors)):
            if(factors[i]*factors[j] == num):
                answer.append([factors[i]-1, factors[j]-1])

    fAnswer=[]
    for sets in answer:
        for row in mp:
            if sets[0] <= len(row):
                if sets[1] <= len(mp):
                    fAnswer.append(sets)

    return fAnswer


mp = [
    [3,10,8,14],
    [1,11,12,12],
    [6,2,3,9]
]

pos = [[0,0]]
tempVar = []
while True:
    for i in range(len(pos)):
        print(i, " - ", pos, " - ", pos[i][0], " - ", pos[i][1], " - ", len(mp), " - ", len(mp[i]))
        tempVar+=findFactors( mp[pos[i][0]][pos[i][1]] )
    pos = tempVar
    tempVar = []
    for i in range(len(pos)):
        for j in range(len(pos[i])):
            if pos[i][0] == len(mp) and pos[i][1] == len(mp[-1]):
                print("yes")
                break



