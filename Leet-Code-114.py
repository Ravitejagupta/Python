# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            stack = []
            stack.append(root)
            while stack:
                top = stack.pop()
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
                if top != root:
                    root.right = top
                    root.left = None
                    root = root.right
