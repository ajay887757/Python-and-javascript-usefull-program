# def chkPair(size,A , x):
#     for i in range(0, size - 1):
#         for j in range(i + 1, size):
#             if (A[i] + A[j] == x):
#                 # print(f"Pair with a given sum {x} is ({A[i]},{A[j]})")
 
#                 return "Yes"
#     return "No"


# A=[1,2,3,4]
# x=chkPair(4,A,7)
# print(x)




def Solution(S):
    max_diff = S[1] - S[0]
    arr_size = len(S)
      
    for i in range( arr_size ):
        for j in range( i+1, arr_size ):
            if(S[j] - S[i] > max_diff): 
                max_diff = S[j] - S[i]
      
    return max_diff
      
arr = [2, 3, 10, 6, 4, 8, 1]
data=Solution(arr)
print(data)




# def CountPS(str, n):
  
#     # create empty 2-D matrix that counts
#     # all palindrome substring. dp[i][j]
#     # stores counts of palindromic
#     # substrings in st[i..j]
#     dp = [[0 for x in range(n)]
#           for y in range(n)]
  
#     # P[i][j] = true if substring str[i..j]
#     # is palindrome, else false
#     P = [[False for x in range(n)]
#          for y in range(n)]
  
#     # palindrome of single length
#     for i in range(n):
#         P[i][i] = True
  
#     # palindrome of length 2
#     for i in range(n - 1):
#         if (str[i] == str[i + 1]):
#             P[i][i + 1] = True
#             dp[i][i + 1] = 1
  
#     # Palindromes of length more than 2. This
#     # loop is similar to Matrix Chain Multiplication.
#     # We start with a gap of length 2 and fill DP
#     # table in a way that the gap between starting and
#     # ending indexes increase one by one by
#     # outer loop.
#     for gap in range(2, n):
  
#         # Pick a starting point for the current gap
#         for i in range(n - gap):
  
#             # Set ending point
#             j = gap + i
  
#             # If current string is palindrome
#             if (str[i] == str[j] and P[i + 1][j - 1]):
#                 P[i][j] = True
  
#             # Add current palindrome substring ( + 1)
#             # and rest palindrome substring (dp[i][j-1] +
#             # dp[i+1][j]) remove common palindrome
#             # substrings (- dp[i+1][j-1])
#             if (P[i][j] == True):
#                 dp[i][j] = (dp[i][j - 1] +
#                             dp[i + 1][j] + 1 - dp[i + 1][j - 1])
#             else:
#                 dp[i][j] = (dp[i][j - 1] +
#                             dp[i + 1][j] - dp[i + 1][j - 1])
  
#     # return total palindromic substrings
#     return dp[0][n - 1]
  

# str = "aaa"
# n = len(str)
# Data=CountPS(str,n)
# print(Data)


