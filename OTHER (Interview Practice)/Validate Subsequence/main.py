def isValidSubsequence(array, sequence):
    testArr = []
    if len(sequence) == 0:
        return True
    curr=0
    for i in range (len(array)):
        if curr<len(sequence):
            if array[i] == sequence[curr]:
                curr+=1
                testArr.append(array[i])
    return (testArr==sequence)
