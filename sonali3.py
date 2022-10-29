# listData=[2,4,6,8,10,12]
listData=[2,4,6,8,10]

newList=[]

j=0
k=len(listData)//2

for i in range(len(listData)-1,k-1,-1):
    if listData[i]==listData[j]:
        newList.append(listData[i])
    else:
        newList.append(listData[i])
        newList.append(listData[j])

    j+=1

print(newList)







