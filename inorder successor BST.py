#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        successor = None
        while root is not None:
            if x.data >= root.data:
                root = root.right
                
            else:
                successor = root
                root = root.left
                
        return successor
