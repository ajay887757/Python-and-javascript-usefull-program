listData=[2,4,6,8,10]

newList=[]

i=0
j=len(listData)-1
for data in range(j,j//2-1,-1):
    if listData[data]==listData[i]:

        newList.append(listData[data])
    else:
        newList.append(listData[data])
        newList.append(listData[i])
   
    i=i+1

print(newList)