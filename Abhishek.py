

# def MirrorSentence(S):

#     splitData=S.split()
#     splitData.reverse()
#     # reverseData=list(reversed(splitData))
#     # newString=" ".join(reverseData)
#     newString=" ".join(splitData)
#     return newString



# # stringData="Hello World"
# # stringData="Hello World"
# stringData="Mindtree Software Engineer"
# X=MirrorSentence(stringData)
# print(X)






# def countNonDecreasing(n):
     
#     # dp[i][j] contains total count
#     # of non decreasing numbers ending
#     # with digit i and of length j
#     dp = [[0 for i in range(n + 1)]
#              for i in range(10)]
              
#     # Fill table for non decreasing
#     # numbers of length 1.
#     # Base cases 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
 
#     for i in range(10):
#         dp[i][1] = 1
 
#     # Fill the table in bottom-up manner
#     for digit in range(10):
         
#         # Compute total numbers of non
#         # decreasing numbers of length 'len'
#         for len in range(2, n + 1):
             
#             # sum of all numbers of length
#             # of len-1 in which last
#             # digit x is <= 'digit'
#             for x in range(digit + 1):
#                 dp[digit][len] += dp[x][len - 1]
#     count = 0
     
#     # There total nondecreasing numbers
#     # of length n won't be dp[0][n] +
#     # dp[1][n] ..+ dp[9][n]
#     for i in range(10):
#         count += dp[i][n]
#     return count
     
# # Driver Code
# n = 90
# print(countNonDecreasing(n))
 

# import numpy as np
# def nonDecNums(n) :
         
#     # a[i][j] = count of all possible number
#     # with i digits having leading digit as j
#     a = np.zeros((n + 1, 10))
 
#     # Initialization of all 0-digit number
#     for i in range(10) :
#         a[0][i] = 1
 
#     # Initialization of all i-digit
#     # non-decreasing number leading with 9
#     for i in range(1, n + 1) :
#         a[i][9] = 1
 
#     # for all digits we should calculate
#     # number of ways depending upon
#     # leading digits
#     for i in range(1, n + 1) :
#         for j in range(8, -1, -1) :
#             a[i][j] = a[i - 1][j] + a[i][j + 1]
 
#     return int(a[n][0])



# def countNonDecreasing(n):
     

#     dp = [[0 for i in range(n + 1)]
#              for i in range(10)]
              
#     for i in range(10):
#         dp[i][1] = 1
#     for digit in range(10):
#         for len in range(2, n + 1):
#             for x in range(digit + 1):
#                 dp[digit][len] += dp[x][len - 1]
#     count = 0

#     for i in range(10):
#         count += dp[i][n]
#     return count

    
# # # Driver Code
# # n = 90
# # print(countNonDecreasing(n))
 


# def generateUtil(x, arr, curr_sum,
#                          curr_idx):
 
# # If current sum is equal to x,
# # then we found a sequence
#     if (curr_sum == x):
#         printArr(arr, curr_idx)
#         return
 
 
#     # Try placing all numbers from
#     # 1 to x-curr_sum at current
#     # index
#     num = 1
     
#     # The placed number must also be
#     # smaller than previously placed
#     # numbers and it may be equal to
#     # the previous stored value, i.e.,
#     # arr[curr_idx-1] if there exists
#     # a previous number
#     while (num <= x - curr_sum and
#                 (curr_idx == 0 or
#            num <= arr[curr_idx - 1])):
 
#         # Place number at curr_idx
#         arr[curr_idx] = num
     
#         # Recur
#         generateUtil(x, arr,
#             curr_sum + num, curr_idx + 1)
     
#         # Try next number
#         num += 1
 
 
 
# # A wrapper over generateUtil()
# def generate(x):
 
#     # Array to store sequences
#     # on by one
#     arr = [0] * x
#     generateUtil(x, arr, 0, 0)
 
 
# # Driver program
# x = 5
# generate(x)


import numpy as np;

def count(n) :  
  c=np.zeros((n+1,10))
  print(c)
  for i in range(10): 
    c[0][i] = 1
  for i in range(1,n+1): 
    c[i][9]=1
  for i in range(1,n+1): 
    for j in range(8,-1,-1): 
        if i>j:
            c[i][j]=c[i-1][j]+c[i][j+1]
  result=int(c[n][0])
#   print(c)
#   data=c.find(result)
#   print(data)
  return result


n=input("Enter number of digits:")
no=int(n)
print("Total no. of non-decreasing digits is ",count(no)) 