a = [1,2,3,4]

def problem(a,i):
  if i==-1:
    a = [1]+ [0]*len(a)
    return a
  if a[i] != 9:
    a[i] = a[i]+1
    return a
  else:
    a[i] = 0
    return problem(a,i-1)
