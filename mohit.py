def distinct_pairs(A):
    s = set()
    lenData=len(A)
 
    for i in range(lenData):
        for j in range(lenData):
            s.add((A[i], A[j]))

    return len(s)
 


x=distinct_pairs([1,2,3])
# arry=list(input())
# x=int(input())
# x=distinct_pairs(x)
print(x)