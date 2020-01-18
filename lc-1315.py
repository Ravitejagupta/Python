# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        visited = set()
        if not root:
            return 0
        ans = 0
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            l,r = node.left, node.right
            if l: q.append(l)
            if r: q.append(r)
            if node.val%2 == 0:
                if l:
                    if l.left and l.left not in visited:
                        ans += l.left.val
                        visited.add(l.left)
                    if l.right and l.right not in visited:
                        ans += l.right.val
                        visited.add(l.right)
                if r:
                    if r.left and r.left not in visited:
                        ans += r.left.val
                        visited.add(r.left)
                    if r.right and r.right not in visited:
                        ans += r.right.val
                        visited.add(r.right)
        return ans
