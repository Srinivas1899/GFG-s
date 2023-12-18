#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        N = len(Arr)
        if K > N:
            return -1 
        max_sum = sum(Arr[:K])
        current_sum = max_sum
        for i in range(K, N):
            current_sum = current_sum - Arr[i - K] + Arr[i]
            max_sum = max(max_sum, current_sum)
        return max_sum
