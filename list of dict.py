jsonData = [
    {"Dog set": "Diesel generator"},
    {"Organization": "Organization"},
    {"Group": "Organization"},
    {"Orange": "Kinnu"},
    {"Orange": "narangi"},
]

result=[]

for i in jsonData:
    temp=[]
    for k,v in i.items():
        temp.append(k)
        temp.append(v)
        appendstatus=False
        for d in result:
            if k in d :
                index=result.index(d)
                print(index)
                appendstatus=True
                result[index].append(v)
                
            elif v in d:
                appendstatus=True
                index=result.index(d)
                print(index)

                result[index].append(v)

    # print(temp)
    if appendstatus==False:
        result.append(temp)
    
print(result)