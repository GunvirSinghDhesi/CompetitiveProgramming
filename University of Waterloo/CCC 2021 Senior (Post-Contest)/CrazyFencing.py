plankNum = 4
plankHeights = [6, 4, 9, 7, 3]
plankWidth = [5, 2, 4, 1]
totalArea=0

for i in range(len(plankWidth)):
    triangleArea = 0
    otherArea = 0
    triangleHeight = 0
    if plankHeights[i] > plankHeights[i+1]:
        triangleHeight = plankHeights[i]-plankHeights[i+1]
        triangleArea = (plankWidth[i]*triangleHeight)/2
        otherArea = plankHeights[i+1] * plankWidth[i]
    else:
        triangleHeight = plankHeights[i+1]-plankHeights[i]
        triangleArea = (plankWidth[i]*triangleHeight)/2
        otherArea = plankHeights[i] * plankWidth[i]    
    totalArea += triangleArea+otherArea
print(f"Total Area {totalArea}")


