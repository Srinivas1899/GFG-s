#User function Template for python3

class Solution:
   def gameOfXor(self, N , A):
       #code here
       if N%2==0:
           return 0
       res=0
       for i in range(0,N,2):
           res=res^A[i]
       return res
