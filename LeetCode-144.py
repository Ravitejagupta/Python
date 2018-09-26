class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        '''if not root:
            return []
        elif not root.left and not root.right:
            res = [root.val]
            return  res
        l = self.preorderTraversal(root.left)
        r = self.preorderTraversal(root.right)
        return [root.val]+l + r'''
