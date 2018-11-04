# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,root,arr):
        if not root:
            return
        elif not root.left and not root.right:
            arr.append(root.val)
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)
        return arr
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        #print(self.dfs(root1, []))
        return self.dfs(root1, []) == self.dfs(root2, [])
