import math

def p_count(s):
  d ={}
  ans = 0
  for i in s:
    if i not in d:
      d[i] = 1
    else:
      d[i] +=1
  if len(d) == 1:
    return 1
  if len(d) ==2:
    return math.factorial(len(s))/ math.factorial(d["1"])*math.factorial(d["0"])
  else:
    for j in range(d["?"]+1):
      ans += math.factorial(len(s)) / ( math.factorial(d["1"] + j) * math.factorial(len(s) - d["1"] - j))
    return ans
