class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for index,char in enumerate(alphabets):
            d[index] = char
        if not root.left and not root.right:
            return d[root.val]
        def desc(node, res):
            if node:
                res = d[node.val] + res
                if not node.left and not node.right:
                    return res
                l,r = desc(node.left, res), desc(node.right, res)
                if l<r : return l 
                else: return r
            else:
                return 'z'*1000
        return desc(root,"")
