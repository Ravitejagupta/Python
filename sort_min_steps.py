a = [1,0,0,1,0,0,1]
ans = []
for i in range(len(a)):
  if a[i] == 0:
    ans.append(i)
if len(ans) == len(a) or len(ans) == 0:
  c = 0

index = len(ans)-1
k = len(a) - 1
c = 0
while index >= 0:
  c += k - ans[index]
  k -= 1
  index -= 1

print(c)
