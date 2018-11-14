# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = 0
        return self.helper(root, s)
    
    def helper(self, root, ans):
        if not root:
            return ans
        if not root.left and not root.right:
            return ans*10 + root.val
        elif root.right and root.left:
            return self.helper(root.left, ans * 10 + root.val) + self.helper(root.right, ans*10 + root.val)
        elif root.right:
            return self.helper(root.right, ans*10 + root.val)
        else:
            return self.helper(root.left, ans*10 + root.val)
        
