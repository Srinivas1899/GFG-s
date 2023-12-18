#User function Template for python3

class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        ans = 0
        for lst in adj:
            ans += len(lst)
        return ans
