n = int(input())
for i in range(n):
    hexa = input()
    num = str(int(hexa[2])-1)
    if num=="1":
        print(hexa)
    else:
        ans=""
        for i in range(len(hexa)):
            if i!=2:
                ans+=hexa[i]
            else:
                ans+=num
        ans+=f" {hexa}"
        print(ans)
