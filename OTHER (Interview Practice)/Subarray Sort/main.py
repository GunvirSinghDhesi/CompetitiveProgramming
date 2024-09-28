def subarraySort(array):
    newArr = sorted(array)
    print(array)
    print(newArr)
    if array == newArr:
        return [-1,-1]

    

    leftIndex = 0
    rightIndex = 0
    ans = []
    for i in range(0,len(array)-1):
        if (array[i] != newArr[i]):
            leftIndex = i
            break
    for i in range(len(array)-1,0,-1):
        if (array[i] != newArr[i]):
            rightIndex = i
            break
    ans= [leftIndex, rightIndex]
    print(len(newArr))

    return ans
        

