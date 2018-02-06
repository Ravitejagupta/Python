def my_tree(inorder,preorder):
  if len(inorder) != len(preorder):
    return False
  if inorder:
    root = TreeNode(preorder[0])
    pos = inorder.index(preorder[0])
    root.left = my_tree(preorder[1:1+pos],inorder[:pos])
    root.right = my_tree(preorder[pos+1:],inorder[pos+1:])
  return root
