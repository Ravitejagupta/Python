# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        q = []
        q.append(root)
        q.append(None)
        level = []
        while len(q) != 0:
            curr = q[0]
            if curr is None:
                ans.append(level)
                level = []
                q = q[1:]
                if len(q) !=0:
                    q.append(None)
            else:
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                q = q[1:]
        return ans
