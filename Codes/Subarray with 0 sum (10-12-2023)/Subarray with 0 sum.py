#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        sum_set = set()
        sum_of_ele = arr[0]
        for i in range(1, n):
            sum_set.add(sum_of_ele)
            sum_of_ele += arr[i]
            if sum_of_ele == 0 or sum_of_ele in sum_set:
                return True
        return False
