# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        return max(l,r,self.height(root.left) + self.height(root.right))
    
    def height(self,root):
        if not root:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
        
