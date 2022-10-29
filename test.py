# listData=[
#     {
#         'a': 1,
#         'b': 2,
#         'c': 5,
#     },
#     {
#         'a': 6,
#         'b': 3,
#         'c': 7,
#     },
#     {
#         'a': 8,
#         'b': 1,
#         'c': 4,
#     },
#     {
#         'a': 3,
#         'b': 0,
#         'c': 2,
#     }
# ]

# listNew=sorted(listData,key=lambda x:x["b"])
# print(listNew)


# tempList=["helo", "Hello"]
# # tempList=["hello", "hey"]
# # tempList=["Alien","line"]

# def testfunc(datalist):
#     firstString=datalist[0].lower()
#     secondString=datalist[1].lower()


#     isTrue=True
#     listfirst=list(firstString)

#     for i in secondString:
    
#         if i in listfirst:
#             listfirst.remove(i)
#             isTrue=True
#         else:
#             isTrue=False
#             break
        
#     return isTrue
    

# x=testfunc(tempList)
# print(x)




# def checkstring(checkbrckets):

#     lenData=len(checkbrckets)

#     # if lenData %2==0:
#     #     return "Not ok"

#     i=0
#     lentemp=lenData-1
#     while(i<lentemp):
#         if checkbrckets[i]=="[" and checkbrckets[lentemp]=="]":
#             i=i+1
#             lentemp=lentemp-1
#         else:
#             return "Not Ok"
            
#     return "Ok"
#     # for i in range(lenData//2):
#     #     startwith=checkbrckets.startswith("[")
#     #     endwith=checkbrckets.endswith("]")
#     #     isok="Ok"

#     #     if startwith and endwith:
#     #         checkbrckets.replace("[","")
#     #         checkbrckets.replace("]","")

#     #         isok="Ok"

#     #     else:
#     #         isok="Not Ok"
#     #         break
        
#     # return isok

# inputData=input("Enter string")
# x=checkstring(inputData)
# print(x)



# def areBracketsBalanced(expr):
#     stack = []
 
#     # Traversing the Expression
#     for char in expr:
#         if char in ["(", "{", "["]:
 
#             # Push the element in the stack
#             stack.append(char)
#         else:
 
#             # IF current character is not opening
#             # bracket, then it must be closing.
#             # So stack cannot be empty at this point.
#             if not stack:
#                 return False
#             current_char = stack.pop()
#             if current_char == '(':
#                 if char != ")":
#                     return False
#             if current_char == '{':
#                 if char != "}":
#                     return False
#             if current_char == '[':
#                 if char != "]":
#                     return False
 
#     # Check Empty Stack
#     if stack:
#         return False
#     return True

# tempdata=areBracketsBalanced("[][][]")
# print(tempdata)


# tempList=["helo", "Hello"]  #False
# tempList=["hello", "Hello"]  #True
# tempList=["hello", "hey"]     #False
# tempList=["Alien","line"]   #True


# def check(listData):
#     FirstListData=listData[0].lower()
#     SecondListData=listData[1].lower()
    
#     ispresent=True
#     for i in SecondListData:
#         if i in FirstListData:
#             FirstListData=FirstListData.replace(i,"",1)
        
#         else:
#             ispresent=False
#             break

#     return ispresent 

# x=check(tempList)
# print(x)





# def check_brackets(string):

#     is_ok="Ok"

#     for i in range(len(string)//2):
#         if string.startswith("[") and string.endswith("]"):
#             is_ok="Ok"
            
            
#         else:
#             is_ok="Not Ok"
#             break
        
#     return is_ok
# x=check_brackets("[[]")
# print(x)


open_list = ["[","{","("]
close_list = ["]","}",")"]
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Not Ok"
    if len(stack) == 0:
        return "oK"
    else:
        return "Not Ok"

x=check(input("Enter String :"))
print(x)