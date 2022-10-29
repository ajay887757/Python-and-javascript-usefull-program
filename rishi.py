
import json
d={}
groupData = {
    # type: "groups",
    "data": [
      ["300", "Support Group", "201,202"],
      ["301", "Customer Service", "201,202,203"],
      ["302", "Collection", "201"],
      ["500", "General CS", "204,205"]
    ]
}

userData = {
    "data": [
      ["201", "James", "Registered", "", True],
      ["202", "John", "", "", False],
      ["203", "John Smith", "Offline", "", False],
      ["204", "Name 204", "Offline", "", False],
      ["205", "205 Name", "Offline", "", False],
      ["206", "206", "", "", True],
      ["207", "207", "Offline", "", False],
      ["208", "208", "", "", False],
      ["209", "209", "", "", False],
      ["2012", "2012", "", "", False],
      ["2013", "2013", "Offline", "", False],
      ["2015", "2015", "", "", False],
      ["2025", "henry", "", "", False]
    ]
}


for i in groupData.items():
    for j in i[1]:
        l=""
        # print(j[2])
        l=l+str(j[2])
        # print(l.split(","))
        l1=l.split(",")
        print(l1)
        
        user=userData["data"][0]
        
        for k in l1:
            try:
                f=user.index(k)
                print("f",f)
                
                data1=userData["data"][f]
                print("Data1",data1)
                
            except:
                break
        
        
        
        
        
# print(userData["data"][0])
    
































