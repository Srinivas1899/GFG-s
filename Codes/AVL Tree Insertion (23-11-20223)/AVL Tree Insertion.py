#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insertToAVL(self, root, key):
        if not root:
            return Node(key)

        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        elif key > root.data:
            root.right = self.insertToAVL(root.right, key)
        else:
            return root  


        root.height = 1 + max(self.height(root.left), self.height(root.right))


        balance = self.balance_factor(root)


        if balance > 1:
            if key < root.left.data:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.data:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root  
            
            
            
            
            
            
            
            
            
            
            
            

