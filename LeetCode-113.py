# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        temp = []
        self.method(root,sum,temp,res)
        return res
    
    def method(self,root,sum,temp,res):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            res.append(temp + [root.val])
            return
        self.method(root.left, sum - root.val, temp + [root.val], res)
        self.method(root.right, sum - root.val, temp + [root.val], res)
