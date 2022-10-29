import copy
def astro(arr):
    for i in range(len(arr)):
        newList= copy.deepcopy(arr)
        newList.remove(arr[i])
        odd ,even=0,0
        for j in range(len(newList)):
            if j%2==0:
                odd+=newList[j]
            
            else:
                even+=newList[j]
        if odd==even:
            return i+1


# data=[2,5,3,1]   # 2
data=[2,4,6,3,4]   # 4
arryData=astro(data)
print(arryData)

