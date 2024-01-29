#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
    arr=[]
    if root:
        arr.append(root.data)
        arr+=preorder(root.left)
        arr+=preorder(root.right)
    return arr
  

