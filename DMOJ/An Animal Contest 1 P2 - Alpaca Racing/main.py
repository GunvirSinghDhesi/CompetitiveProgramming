myAlpaca=0
otherAlpacas=[]
inp1 = input().split()
inp1 = [int(x) for x in inp1]
for i in range(int(inp1[0])+1):
    if i == int(inp1[0]):
        myAlpaca = int(input())
    else:
        otherAlpacas.append(int(input()))
def check():
    for i in range(len(otherAlpacas)):
        if otherAlpacas[i] < myAlpaca:
            del otherAlpacas[i]
            check()
            break

check()
otherAlpacas.sort()

for i in range(int(inp1[2])):
    otherAlpacas[0] = otherAlpacas[0]*((100-inp1[3])/100)
    check()

if len(otherAlpacas) == 0:
    print("YES")
else:
    print("NO")