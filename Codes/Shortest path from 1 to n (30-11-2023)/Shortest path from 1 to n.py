#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        if n < 3:
            return n-1
        return 2 + self.minimumStep(n//3) + self.minimumStep(n%3)
