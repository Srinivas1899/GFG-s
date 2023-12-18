#User function Template for python3
class Solution:

    def nthRowOfPascalTriangle(self,n):
        # code here
       if n==1:
           return [1]
       lst=[]
       n-=1
       def rec(n,lst):
           ans=[]
           if not n:
               return
           for i in range(len(lst)-1):
               s=lst[i]+lst[i+1]
               ans.append(s%(10**9+7))
           lst[:]=[1]+ans[:]+[1]
           rec(n-1,lst)
       rec(n,lst)
       return lst

        
