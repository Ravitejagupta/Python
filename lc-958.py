# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        status = True
        arr = [root]
        while len(arr) > 0:
            node = arr.pop(0)
            if node.left and node.right:
                arr += [node.left, node.right]
            elif not node.left and node.right:
                return False
            else:
                if node.left:
                    arr += [node.left]
                for n in arr:
                    if n.left or n.right:
                        return False
        return True
