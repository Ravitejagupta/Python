def verticals_sum(root):
  d = {}
  cal_sum(root,d,0)
  return d
  
  def cal_sum(root,d,index):
    if index in d:
      d[index] += root.value
    else:
      d[index] = root.value
    if root.left:
      return cal_sum(root.left,d,index-1)
    if root.right:
      return cal_sum(root.right,d,index+1)
