# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l > 0 and r > 0:
            return 1 + min(l,r)
        elif l > 0 :
            return 1 + l
        else:
            return 1 + r
        
