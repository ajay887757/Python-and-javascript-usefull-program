
# vowels=["A","E","I","O","U"]
# String="AIEBIEODCFG"

# count=0
# res=0
# for i in String:
#     if i in vowels:
#         count+=1

#         # print(count)
#     else:
#         res = max(res, count)
#         count=0
    
   
# print(res)

        

arry=[1,2,3,51,67,71,72,73,74,89,76,1,2,3,4,5,6,97,98,99,100,101,102,103,104]

res,count=0,0
dataDict={}
for i in range(0,len(arry)-1):
    data=arry[i]-1
    arrydata=str(arry[i])
    if arry[i]+1==arry[i+1]:
        count+=1
        
        # dataDict[arrydata]=dataDict.get(arrydata,0)+1
        dataDict[arrydata]=count
    

    else:
        dataDict[arrydata]=count+1
        res=max(res,count)
        # dataDict[arry[i]]=res
        count=0

dict_value_list=list(dataDict.values())
print(type(dict_value_list))
max_value=max(dict_value_list)
index_of_max_value=dict_value_list.index(max_value)
print("max_value",max_value)
list_data_dict_values=list(dataDict)
max_key=list_data_dict_values[index_of_max_value]
print("max_key",max_key)
print(int(max_key)-(max_value-1))



