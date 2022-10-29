listData = ["T", "h", "I", "s", " ", " ", " ", " ", " ", " ", "i", "s", " ", " ", " ", "a", " ", " ", " ", " ", " ", " ", " ", " ", "t", "r", "e", "e"]
newlist=[]

for i in range(len(listData)):
    if listData[i]==" ":
        if listData[i-1]==" ":
            continue
        else:
            newlist.append(listData[i])
    
    elif listData[i]!=" ":
        newlist.append(listData[i])
    
print(newlist)