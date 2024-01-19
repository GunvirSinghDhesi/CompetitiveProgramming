pairs = [['A','B'],['G','L'],['J','K']]
# for i in range(int(input())):
#     pairs.append([input().split()])

npairs = [['D','F'],['D','G']]
# for i in range(int(input())):
#     npairs.append([input().split()])


gpairs = [['A','C','G'],['B','D','F'],['E','H','I'],['J','K','L']]
# for i in range(int(input())):
#     gpairs.append([input().split()])


problem=0
for pair in range(len(pairs)):
    for i in range(len(gpairs)):
        tg = [False for x in range(len(pairs[pair]))]
        for element in range(len(pairs[pair])):
            if (pairs[pair][element]) in gpairs[i]:
                tg[element] = True
     
        if False in tg:
            print(tg, pairs[pair], gpairs[i])
            if tg != [False for x in range(len(pairs[pair]))]:
                pairs.remove(pairs[pair])
                problem+=1
                pair=0
                i=0
                element=0


print(problem)