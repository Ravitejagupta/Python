def findBottomLeftValue(self, root):
        queue = [root]
        for r in queue:
            if r.right:
                queue.append(r.right)
            if r.left:
                queue.append(r.left)
        return r.val
