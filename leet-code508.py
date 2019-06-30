# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.d = {}
        
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            total = l + r + root.val
            self.d[total] = self.d.get(total, 0) + 1
            return total
        helper(root)
        print(self.d)
        ans = []
        m = -1
        for key in self.d:
            if self.d[key] > m:
                ans = [key]
                m = max(m,self.d[key])
            elif self.d[key] == m:
                ans.append(key)
        return ans
