def check_path(s,d,g,path = []):
  path.append(s)
  for v in g[s]:
    if v == d:
      path.append(d)
      return path
    else:
      return check_path(v,d,g,path)

g = {1:[2,3],2:[4,5],3:[4,5],4:[5],5:[1],6:[]}

print(check_path(1,5,g))
