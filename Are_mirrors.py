def are_mirrors(root1,root2):
  if root1 is None and root2 is None:
    return True
  if root2 is None or root1 is None:
    return False
  if root2.val == root1.val:
    return True
  if root2.val != root1.val:
    return False
  return are_mirrors(root1.left,root2.right) and are_mirrors(root2.left,root1.right)
