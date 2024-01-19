
def addToList(isMirrored):
    if isMirrored:
        result.append("Mirrored pair")
    else:
        result.append("Ordinary pair")
result=["Ready"]
while True:
    tempVar = input()
    if tempVar != "  ":
        if tempVar[0] == 'd' and tempVar[1] == 'b':
            addToList(True)
        elif tempVar[0] == 'b' and tempVar[1] == 'd':
            addToList(True)
        elif tempVar[0] == 'q' and tempVar[1] == 'p':
            addToList(True)
        elif tempVar[0] == 'p' and tempVar[1] == 'q':
            addToList(True)
        else:
            addToList(False)
    else:
        break 

for i in range(len(result)):
    print(result[i])