obs = int(input())

comp = []
for i in range(obs):
    comp.append([int(x) for x in input().split()])
comp.sort()

speed = []
for i in range(1,len(comp)):
    speed.append((abs(comp[i][1] - comp[i-1][1])/(comp[i][0] - comp[i-1][0])))

speed.sort()
print(speed[-1])