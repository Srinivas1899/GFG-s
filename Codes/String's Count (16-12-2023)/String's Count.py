#User function Template for python3


class Solution:
   def countStr(self, n):
        if n==1:
            return 3
        if n==2:
            return 8
        result=(n-1)*(n)+2*n+1+(n*(n-1)/2)+(n*(n-1)*(n-2))/2
        return int(result)
