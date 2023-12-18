#User function Template for python3

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        return self.Symmetric(root,root)
    def Symmetric(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.data != root2.data:
            return False
        else:
            ls = self.Symmetric(root1.left,root2.right)
            rs = self.Symmetric(root1.right,root2.left)
            return ls and rs
