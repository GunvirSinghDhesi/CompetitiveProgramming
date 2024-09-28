def threeNumberSum(array, targetSum):

    ans = []
    array.sort()
    print(array)
    for i in range(len(array)-1):
        leftIndex = i+1
        rightIndex = len(array)-1
        tempArr=[]
        for j in range(i,len(array)):
            if leftIndex >= rightIndex:
                break
            elif array[i]+array[leftIndex]+array[rightIndex] == targetSum:
                tempArr.append([array[i],array[leftIndex],array[rightIndex]])
                ans.append(tempArr)
                tempArr=[]
                leftIndex+=1
                rightIndex-=1
            elif array[i]+array[leftIndex]+array[rightIndex]<targetSum:
                leftIndex+=1
            
            elif array[i]+array[leftIndex]+array[rightIndex]>targetSum:
                rightIndex-=1

            
            
    return ans
                    
                
                
