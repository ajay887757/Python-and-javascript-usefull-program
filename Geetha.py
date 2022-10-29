
my_dict1 = [
    {
        "name": "mike",
        "age": 21,
        "dept": "ece",
        "city": "Chennai",
        "mark": [
            {"sub": "maths", "score": 53},
            {"sub": "eng", "score": 73},
            {"sub": "eng", "score": 33},
            {"sub": "maths", "score": 23},
        ],
    },
    {
        "name": "will",
        "age": 22,
        "dept": "cse",
        "city": "Madurai",
        "mark": [
            {"sub": "maths", "score": 53},
            {"sub": "eng", "score": 33},
            {"sub": "maths", "score": 23},
        ],
    },
    {
        "name": "john",
        "age": 23,
        "dept": "ece",
        "city": "Chennai",
        "mark": [
            {"sub": "maths", "score": 53},
            {"sub": "phy", "score": 73},
            {"sub": "eng", "score": 23},
        ],
    },
]
# my_dict2 = []

# for items in my_dict1:
#     for key,value in items.items():
#         # print(key)
#         if isinstance(value,list):
#             # print(value)
            
#             notpresent=[]
#             present=[]
#             for listOfSubjectData in value:
#                 # print(listOfSubjectData)

#                 if listOfSubjectData["sub"] not in notpresent:
#                     notpresent.append(listOfSubjectData["sub"])\
                
#                 else:
#                     present.append(listOfSubjectData["sub"])
#             if present !=[]:
#                 my_dict2.append({
#                     "name":items["name"],
#                     "dublicateSub":present
#                 })

# print(my_dict2)



my_dict1 = [
    {
        "name": "mike",
        "age": 21,
        "dept": "ece",
        "city": "Chennai",
        "mark": [
            {"sub": "maths", "score": 53},
            {"sub": "eng", "score": 73},
            {"sub": "eng", "score": 33},
            {"sub": "maths", "score": 23},
        ],
    },
    {
        "name": "will",
        "age": 22,
        "dept": "cse",
        "city": "Madurai",
        "mark": [
            {"sub": "maths", "score": 53},
            {"sub": "eng", "score": 33},
            {"sub": "maths", "score": 23},
        ],
    },
    {
        "name": "john",
        "age": 23,
        "dept": "ece",
        "city": "Chennai",
        "mark": [
            {"sub": "maths", "score": 53},
            {"sub": "phy", "score": 73},
            {"sub": "eng", "score": 23},
        ],
    },
]
class FindDublicate():
    def findSubDublicate(self,my_dict1):
        self.my_dict2 = []
        self.my_dict1=my_dict1
        for items in my_dict1:
            for key,value in items.items():
                # print(key)
                if isinstance(value,list):
                    # print(value)
                    
                    notpresent=[]
                    present=[]
                    for listOfSubjectData in value:
                        # print(listOfSubjectData)

                        if listOfSubjectData["sub"] not in notpresent:
                            notpresent.append(listOfSubjectData["sub"])\
                        
                        else:
                            present.append(listOfSubjectData["sub"])
                    if present !=[]:
                        self.my_dict2.append(listOfSubjectData)

        # print(my_dict2)
        return self.my_dict2

obj=FindDublicate()
result=obj.findSubDublicate(my_dict1)
print(result)


            


