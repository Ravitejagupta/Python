# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.check(root.left,root.right)
    
    def check(self,left,right):
        if not left and not right:
            return True
        if (left and not right ) or (right and not left):
            return False
        if left is not None and right is not None:
            if left.val == right.val:
                return self.check(left.left,right.right) and self.check(left.right,right.left)
        return False
        
