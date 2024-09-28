def twoNumberSum(array, targetSum):
    tempSum = 0
    for i in range(len(array)):
        for j in range (1, len(array)):
            if array[i]+array[j] == targetSum and i!=j:
                return [array[i], array[j]]
    return []