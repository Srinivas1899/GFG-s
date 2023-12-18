#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def countPairs(self, root1, root2, x): 
        #code here.
        stack1, stack2 = [], []
        count = 0
    
        while stack1 or stack2 or root1 or root2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.right
    
            if not stack1 or not stack2:
                break
    
            top1, top2 = stack1[-1], stack2[-1]
            current_sum = top1.data + top2.data
    
            if current_sum == x:
                count += 1
                stack1.pop()
                stack2.pop()
                root1 = top1.right
                root2 = top2.left
            elif current_sum < x:
                stack1.pop()
                root1 = top1.right
            else:
                stack2.pop()
                root2 = top2.left
    
        return count
